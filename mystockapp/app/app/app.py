import streamlit as st
import pandas as pd
import plotly.graph_objects as go


def main():
    # Initialize session state
    if "data" not in st.session_state:
        st.session_state.data = None
    if "features_df" not in st.session_state:
        st.session_state.features_df = None
    if "features_with_signals" not in st.session_state:
        st.session_state.features_with_signals = None
    if "backtest_results" not in st.session_state:
        st.session_state.backtest_results = None
    if "last_app_inputs" not in st.session_state:
        st.session_state.last_app_inputs = None

    # Sidebar for user inputs
    with st.sidebar:
        # ... existing sidebar inputs ...
        pass  # Keep existing sidebar code

    # Main content area
    if fetch_data or st.session_state.last_app_inputs != current_app_inputs:
        # ... existing data fetching and feature generation ...

        # Run backtest
        with st.spinner("Running backtest..."):
            st.subheader("Backtesting Results")

            # Create and apply trading strategy
            # ... existing strategy creation and signal generation ...

            # --- START FIX FOR ISSUE 3: CONSISTENT NAN HANDLING BEFORE BACKTEST ---
            original_features_len = len(features_df)
            features_with_signals = (
                features_with_signals.dropna()
            )  # Drop any row with any NaN
            rows_dropped_nan = original_features_len - len(
                features_with_signals
            )
            if rows_dropped_nan > 0:
                st.warning(
                    f"Dropped {rows_dropped_nan} rows with NaN values after feature generation."
                )
            if features_with_signals.empty:
                st.error(
                    "No data remaining after dropping NaN values. Cannot run backtest."
                )
                return
            # --- END FIX FOR ISSUE 3 ---

            # Run backtest
            results = run_backtest(
                features_with_signals,  # Use the DataFrame after NaN handling
                initial_capital=initial_capital,
                commission_fixed=commission_fixed,
                commission_pct=commission_pct,
                slippage_pct=slippage_pct,
                position_size_pct=position_size_pct,
            )

            if results is None:
                st.error(
                    "Backtest failed. Please check your data and parameters."
                )
                return

            # Display results in columns
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric(
                    "Final Portfolio Value", f"${results['final_value']:,.2f}"
                )
                st.metric(
                    "Total Return", f"{results['total_return_pct']:.2f}%"
                )
                st.metric(
                    "Max Drawdown", f"{results['max_drawdown']:.2f}%"
                )  # Moved Max Drawdown here
            with col2:
                st.metric(
                    "Total Transactions (Buy/Sell)", f"{results['num_trades']}"
                )  # Updated label
                st.metric(
                    "Completed Trades (Round Trips)",
                    f"{results['closed_trade_count']}",
                )  # Added metric
                st.metric(
                    "Buy & Hold Return",
                    f"{results['buy_hold_return_pct']:.2f}%",
                )
            with col3:
                st.metric(
                    "Win Rate", f"{results['win_rate']:.2f}%"
                )  # Moved Win Rate here
                st.metric("Profit Factor", f"{results['profit_factor']:.2f}")
                st.metric(
                    "Total Commission Paid",
                    f"${results['total_commission']:.2f}",
                )  # Updated label

            # Display portfolio equity chart
            equity_fig = go.Figure()

            # Convert portfolio values to a Series with the same index as the dataframe
            portfolio_series = pd.Series(
                results["portfolio_values"], index=features_with_signals.index
            )

            # Add baseline initial capital
            equity_fig.add_hline(
                y=initial_capital,
                line_dash="dash",
                line_color="gray",
                annotation_text="Initial Capital",
            )

            # Add portfolio equity curve
            equity_fig.add_trace(
                go.Scatter(
                    x=portfolio_series.index,  # Use the index from the series
                    y=portfolio_series,
                    name="Portfolio Value",
                    line=dict(color="blue", width=2),
                )
            )

            # Add buy/sell markers - Use the DataFrame *after* NaN handling
            buy_points = features_with_signals[
                features_with_signals["buy_signal"] == True
            ]
            sell_points = features_with_signals[
                features_with_signals["sell_signal"] == True
            ]

            equity_fig.add_trace(
                go.Scatter(
                    x=buy_points.index,
                    y=portfolio_series.loc[
                        buy_points.index
                    ],  # Get portfolio value at signal date
                    mode="markers",
                    marker=dict(symbol="triangle-up", size=10, color="green"),
                    name="Buy Signal",
                )
            )

            equity_fig.add_trace(
                go.Scatter(
                    x=sell_points.index,
                    y=portfolio_series.loc[
                        sell_points.index
                    ],  # Get portfolio value at signal date
                    mode="markers",
                    marker=dict(symbol="triangle-down", size=10, color="red"),
                    name="Sell Signal",
                )
            )

            equity_fig.update_layout(
                title="Portfolio Equity Curve",
                xaxis_title="Date",
                yaxis_title="Portfolio Value ($)",
                height=500,
            )

            st.plotly_chart(equity_fig, use_container_width=True)

            # Display trades table
            if results["completed_trades"]:
                st.subheader("Completed Trades")

                trades_df = pd.DataFrame(results["completed_trades"])
                trades_df["entry_date"] = pd.to_datetime(
                    trades_df["entry_date"]
                ).dt.date
                trades_df["exit_date"] = pd.to_datetime(
                    trades_df["exit_date"]
                ).dt.date
                trades_df["holding_period"] = (
                    pd.to_datetime(trades_df["exit_date"])
                    - pd.to_datetime(trades_df["entry_date"])
                ).dt.days

                display_trades = trades_df[
                    [
                        "entry_date",
                        "exit_date",
                        "holding_period",
                        "entry_price",
                        "exit_price",
                        "shares",
                        "net_profit_loss",
                        "return_pct",
                        "total_costs",
                    ]
                ].copy()
                display_trades.columns = [
                    "Entry Date",
                    "Exit Date",
                    "Days Held",
                    "Avg Entry Price ($)",
                    "Avg Exit Price ($)",
                    "Shares",
                    "Net P&L ($)",
                    "Return (%)",
                    "Total Costs ($)",
                ]
                display_trades["Avg Entry Price ($)"] = display_trades[
                    "Avg Entry Price ($)"
                ].map("${:,.2f}".format)
                display_trades["Avg Exit Price ($)"] = display_trades[
                    "Avg Exit Price ($)"
                ].map("${:,.2f}".format)
                display_trades["Net P&L ($)"] = display_trades[
                    "Net P&L ($)"
                ].map("${:,.2f}".format)
                display_trades["Return (%)"] = display_trades[
                    "Return (%)"
                ].map("{:,.2f}%".format)
                display_trades["Total Costs ($)"] = display_trades[
                    "Total Costs ($)"
                ].map("${:,.2f}".format)

                st.dataframe(display_trades, use_container_width=True)

                st.subheader("Trade Performance Distribution")
                profit_loss_hist = go.Figure()
                profit_loss_hist.add_trace(
                    go.Histogram(
                        x=trades_df["return_pct"],
                        nbinsx=20,
                        marker_color=[
                            "green" if x >= 0 else "red"
                            for x in trades_df["return_pct"]
                        ],
                    )
                )
                profit_loss_hist.update_layout(
                    title="Trade Return Distribution (%)",
                    xaxis_title="Return (%)",
                    yaxis_title="Number of Trades",
                    height=400,
                    bargap=0.1,
                )
                profit_loss_hist.add_vline(
                    x=0, line_dash="dash", line_color="black"
                )
                st.plotly_chart(profit_loss_hist, use_container_width=True)
            else:
                st.info("No completed trades in this period.")

        # ... rest of the function ...

    # Capture current inputs to check for changes
    # ... existing input capture ...

    if fetch_data or st.session_state.last_app_inputs != current_app_inputs:
        st.session_state.last_app_inputs = current_app_inputs

        # ... existing code for fetching and processing ...

        # --- START FIX FOR ISSUE 3: CONSISTENT NAN HANDLING AFTER FEATURE GENERATION ---
        original_features_len = len(features_df)
        features_df = features_df.dropna()
        rows_dropped_nan = original_features_len - len(features_df)
        if rows_dropped_nan > 0:
            st.warning(
                f"Dropped {rows_dropped_nan} rows with NaN values after feature generation."
            )
        if features_df.empty:
            st.error(
                "No data remaining after dropping NaN values. Cannot proceed."
            )
            return
        # --- END FIX FOR ISSUE 3 ---

        # ... existing code for displaying results ...


# ... existing code after the main function ...
