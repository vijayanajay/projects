"""
Stock Trading App - Interactive Dashboard

This app provides an interactive UI for:
1. Fetching and visualizing stock data
2. Generating technical indicators
3. Backtesting trading strategies
4. Visualizing performance metrics
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import yf
from datetime import datetime, timedelta
import os
import logging
import sys

# Add the app directory to the path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import our modules
from src.data_fetcher import get_stock_data
from src.feature_factory import FeatureFactory
from src.backtester import (
    SMACrossoverStrategy,
    RSIStrategy,
    run_backtest,
    generate_backtest_report,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# App configuration
st.set_page_config(
    page_title="Stock Trading App",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)


def main():
    # App title and description
    st.title("Stock Trading App")
    st.markdown(
        """
        An interactive dashboard for stock analysis, technical indicators, and backtesting.

        **Features:**
        - Fetch historical stock data
        - Generate and visualize technical indicators
        - Backtest trading strategies
        - Analyze performance metrics
        """
    )

    # Sidebar for user inputs
    with st.sidebar:
        st.header("Settings")

        # Data fetch settings
        st.subheader("Stock Data")
        ticker = st.text_input("Ticker Symbol", value="RELIANCE.NS")
        period_options = ["1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "max"]
        period = st.selectbox("Time Period", period_options, index=3)
        interval_options = ["1d", "5d", "1wk", "1mo"]
        interval = st.selectbox("Interval", interval_options, index=0)

        # Technical indicators selection
        st.subheader("Technical Indicators")
        use_sma = st.checkbox("Simple Moving Average (SMA)", value=True)
        use_ema = st.checkbox("Exponential Moving Average (EMA)", value=False)
        use_rsi = st.checkbox("Relative Strength Index (RSI)", value=True)
        use_macd = st.checkbox("MACD", value=True)
        use_bollinger = st.checkbox("Bollinger Bands", value=False)

        # Backtesting settings
        st.subheader("Backtesting")
        strategy_options = ["SMA Crossover", "RSI Strategy"]
        selected_strategy = st.selectbox(
            "Trading Strategy", strategy_options, index=0
        )
        initial_capital = st.number_input(
            "Initial Capital", value=100000.0, step=10000.0
        )
        commission_fixed = st.number_input(
            "Fixed Commission", value=20.0, step=5.0
        )
        commission_pct = (
            st.number_input(
                "Commission %", value=0.03, step=0.01, format="%.2f"
            )
            / 100
        )
        slippage_pct = (
            st.number_input("Slippage %", value=0.1, step=0.05, format="%.2f")
            / 100
        )
        position_size_pct = (
            st.number_input(
                "Position Size %", value=25.0, step=5.0, format="%.1f"
            )
            / 100
        )

        # Strategy-specific parameters
        if selected_strategy == "SMA Crossover":
            st.subheader("SMA Crossover Parameters")
            fast_sma = st.slider(
                "Fast SMA Window", min_value=5, max_value=100, value=50, step=5
            )
            slow_sma = st.slider(
                "Slow SMA Window",
                min_value=20,
                max_value=300,
                value=200,
                step=10,
            )
            if fast_sma >= slow_sma:
                st.error(
                    f"Fast SMA window ({fast_sma}) must be less than Slow SMA window ({slow_sma})."
                )
                return  # Stop further processing
        elif selected_strategy == "RSI Strategy":
            st.subheader("RSI Strategy Parameters")
            rsi_window = st.slider(
                "RSI Window", min_value=7, max_value=21, value=14, step=1
            )
            rsi_oversold = st.slider(
                "RSI Oversold Threshold",
                min_value=20,
                max_value=40,
                value=30,
                step=1,
            )
            rsi_overbought = st.slider(
                "RSI Overbought Threshold",
                min_value=60,
                max_value=80,
                value=70,
                step=1,
            )
            if rsi_oversold >= rsi_overbought:
                st.error(
                    f"RSI Oversold threshold ({rsi_oversold}) must be less than RSI Overbought threshold ({rsi_overbought})."
                )
                return  # Stop further processing

        # Action button
        fetch_data = st.button("Fetch Data & Run Analysis")

    # Main content area
    if fetch_data:
        # Fetch stock data
        with st.spinner(f"Fetching {ticker} data..."):
            data = get_stock_data(ticker, period, interval)
            if data is None or len(data) == 0:
                st.error(
                    f"Failed to fetch data for {ticker}. Please check the ticker symbol and try again."
                )
                return

        # Display raw data summary
        st.subheader("Stock Data Overview")
        st.write(
            f"**{ticker}** from {data.index[0].date()} to {data.index[-1].date()} ({len(data)} trading days)"
        )

        # Display basic price chart
        fig = go.Figure()
        fig.add_trace(
            go.Candlestick(
                x=data.index,
                open=data["Open"],
                high=data["High"],
                low=data["Low"],
                close=data["Close"],
                name="OHLC",
            )
        )
        fig.update_layout(
            title=f"{ticker} Price Chart",
            xaxis_title="Date",
            yaxis_title="Price",
            height=500,
        )
        st.plotly_chart(fig, use_container_width=True)

        # Generate technical indicators
        with st.spinner("Generating technical indicators..."):
            # Determine feature families to generate
            feature_families = []
            if use_sma:
                feature_families.append("sma")
            if use_ema:
                feature_families.append("ema")
            if use_rsi:
                feature_families.append("rsi")
            if use_macd:
                feature_families.append("macd")
            if use_bollinger:
                feature_families.append("bollinger_bands")

            # Generate features if any are selected
            if feature_families:
                factory = FeatureFactory(
                    data, feature_families=feature_families
                )
                features_df = factory.generate_features()
            else:
                features_df = data.copy()

            # Display generated features
            st.subheader("Technical Indicators")
            with st.expander("View Generated Indicators", expanded=False):
                st.dataframe(features_df.tail(10))

        # Create indicator charts
        with st.spinner("Creating indicator charts..."):
            # Show selected indicators
            indicators_to_plot = []

            if use_sma:
                # SMA Chart
                sma_fig = go.Figure()
                sma_fig.add_trace(
                    go.Scatter(
                        x=features_df.index,
                        y=features_df["Close"],
                        name="Price",
                    )
                )
                # Plot 50-day and 200-day SMAs if available
                if "sma_50" in features_df.columns:
                    sma_fig.add_trace(
                        go.Scatter(
                            x=features_df.index,
                            y=features_df["sma_50"],
                            name="SMA(50)",
                        )
                    )
                if "sma_200" in features_df.columns:
                    sma_fig.add_trace(
                        go.Scatter(
                            x=features_df.index,
                            y=features_df["sma_200"],
                            name="SMA(200)",
                        )
                    )
                sma_fig.update_layout(
                    title="Price with Simple Moving Averages", height=400
                )
                indicators_to_plot.append(("Simple Moving Averages", sma_fig))

            if use_rsi:
                # RSI Chart
                rsi_fig = go.Figure()
                rsi_window = 14  # Default RSI window
                rsi_col = f"rsi_{rsi_window}"
                if rsi_col in features_df.columns:
                    rsi_fig.add_trace(
                        go.Scatter(
                            x=features_df.index,
                            y=features_df[rsi_col],
                            name=f"RSI({rsi_window})",
                        )
                    )
                    # Add overbought/oversold lines
                    rsi_fig.add_hline(
                        y=70,
                        line_dash="dash",
                        line_color="red",
                        annotation_text="Overbought",
                    )
                    rsi_fig.add_hline(
                        y=30,
                        line_dash="dash",
                        line_color="green",
                        annotation_text="Oversold",
                    )
                    rsi_fig.update_layout(
                        title=f"Relative Strength Index (RSI-{rsi_window})",
                        yaxis=dict(range=[0, 100]),
                        height=300,
                    )
                    indicators_to_plot.append(
                        ("Relative Strength Index", rsi_fig)
                    )

            if use_macd:
                # MACD Chart
                if (
                    "macd_line" in features_df.columns
                    and "macd_signal" in features_df.columns
                ):
                    macd_fig = make_subplots(
                        rows=2,
                        cols=1,
                        row_heights=[0.7, 0.3],
                        vertical_spacing=0.05,
                        shared_xaxes=True,
                    )

                    # Price chart on top
                    macd_fig.add_trace(
                        go.Scatter(
                            x=features_df.index,
                            y=features_df["Close"],
                            name="Price",
                        ),
                        row=1,
                        col=1,
                    )

                    # MACD lines
                    macd_fig.add_trace(
                        go.Scatter(
                            x=features_df.index,
                            y=features_df["macd_line"],
                            name="MACD Line",
                        ),
                        row=2,
                        col=1,
                    )
                    macd_fig.add_trace(
                        go.Scatter(
                            x=features_df.index,
                            y=features_df["macd_signal"],
                            name="Signal Line",
                        ),
                        row=2,
                        col=1,
                    )

                    # MACD Histogram
                    macd_fig.add_trace(
                        go.Bar(
                            x=features_df.index,
                            y=features_df["macd_line"]
                            - features_df["macd_signal"],
                            name="MACD Histogram",
                        ),
                        row=2,
                        col=1,
                    )

                    macd_fig.update_layout(title="MACD Indicator", height=500)
                    indicators_to_plot.append(("MACD", macd_fig))

            if use_bollinger:
                # Bollinger Bands
                if all(
                    col in features_df.columns
                    for col in ["bb_upper", "bb_middle", "bb_lower"]
                ):
                    bb_fig = go.Figure()
                    bb_fig.add_trace(
                        go.Scatter(
                            x=features_df.index,
                            y=features_df["Close"],
                            name="Price",
                        )
                    )
                    bb_fig.add_trace(
                        go.Scatter(
                            x=features_df.index,
                            y=features_df["bb_upper"],
                            name="Upper Band",
                            line=dict(dash="dash"),
                        )
                    )
                    bb_fig.add_trace(
                        go.Scatter(
                            x=features_df.index,
                            y=features_df["bb_middle"],
                            name="Middle Band",
                        )
                    )
                    bb_fig.add_trace(
                        go.Scatter(
                            x=features_df.index,
                            y=features_df["bb_lower"],
                            name="Lower Band",
                            line=dict(dash="dash"),
                        )
                    )
                    bb_fig.update_layout(title="Bollinger Bands", height=400)
                    indicators_to_plot.append(("Bollinger Bands", bb_fig))

            # Display all indicator charts
            tabs = st.tabs([name for name, _ in indicators_to_plot])
            for i, (name, fig) in enumerate(indicators_to_plot):
                with tabs[i]:
                    st.plotly_chart(fig, use_container_width=True)

        # Run backtest
        with st.spinner("Running backtest..."):
            st.subheader("Backtesting Results")

            # Create and apply trading strategy
            if selected_strategy == "SMA Crossover":
                # Make sure we have the required SMA columns
                if f"sma_{fast_sma}" not in features_df.columns:
                    st.error(
                        f"SMA column for {fast_sma} days not found. Please generate SMA indicators first."
                    )
                    return
                if f"sma_{slow_sma}" not in features_df.columns:
                    st.error(
                        f"SMA column for {slow_sma} days not found. Please generate SMA indicators first."
                    )
                    return

                strategy = SMACrossoverStrategy(
                    fast_window=fast_sma, slow_window=slow_sma
                )
                st.write(f"Strategy: **{strategy.name}**")

            elif selected_strategy == "RSI Strategy":
                # Make sure we have the required RSI column
                if f"rsi_{rsi_window}" not in features_df.columns:
                    st.error(
                        f"RSI column for {rsi_window} days not found. Please generate RSI indicators first."
                    )
                    return

                strategy = RSIStrategy(
                    rsi_window=rsi_window,
                    oversold_threshold=rsi_oversold,
                    overbought_threshold=rsi_overbought,
                )
                st.write(f"Strategy: **{strategy.name}**")

            # Generate signals
            features_with_signals = strategy.generate_signals(features_df)

            # Run backtest
            results = run_backtest(
                features_with_signals,
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
                st.metric("Win Rate", f"{results['win_rate']:.2f}%")

            with col2:
                st.metric("Number of Trades", f"{results['num_trades']}")
                st.metric(
                    "Buy & Hold Return",
                    f"{results['buy_hold_return_pct']:.2f}%",
                )
                st.metric("Profit Factor", f"{results['profit_factor']:.2f}")

            with col3:
                st.metric("Max Drawdown", f"{results['max_drawdown']:.2f}%")
                st.metric(
                    "Total Commission", f"${results['total_commission']:.2f}"
                )
                st.metric(
                    "Total Slippage", f"${results['total_slippage_cost']:.2f}"
                )

            # Display portfolio equity chart
            equity_fig = go.Figure()

            # Convert portfolio values to a Series with the same index as the dataframe
            portfolio_series = pd.Series(
                results["portfolio_values"], index=features_df.index
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
                    x=features_df.index,
                    y=portfolio_series,
                    name="Portfolio Value",
                    line=dict(color="blue", width=2),
                )
            )

            # Add buy/sell markers
            buy_points = features_df[features_df["buy_signal"] == True]
            sell_points = features_df[features_df["sell_signal"] == True]

            equity_fig.add_trace(
                go.Scatter(
                    x=buy_points.index,
                    y=portfolio_series[buy_points.index],
                    mode="markers",
                    marker=dict(symbol="triangle-up", size=10, color="green"),
                    name="Buy Signal",
                )
            )

            equity_fig.add_trace(
                go.Scatter(
                    x=sell_points.index,
                    y=portfolio_series[sell_points.index],
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

                # Convert completed trades to DataFrame for display
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

                # Calculate return percentage (profit_loss_pct)
                trades_df["cost_basis"] = (
                    trades_df["entry_price"] * trades_df["shares"]
                )
                trades_df["profit_loss_pct"] = trades_df.apply(
                    lambda row: (
                        (row["net_profit_loss"] / row["cost_basis"]) * 100
                        if row["cost_basis"] != 0
                        else 0
                    ),
                    axis=1,
                )

                # Select and rename columns for display
                display_trades = trades_df[
                    [
                        "entry_date",
                        "exit_date",
                        "holding_period",
                        "entry_price",
                        "exit_price",
                        "shares",
                        "net_profit_loss",
                        "profit_loss_pct",
                        "total_costs",
                    ]
                ].copy()

                display_trades.columns = [
                    "Entry Date",
                    "Exit Date",
                    "Days Held",
                    "Entry Price",
                    "Exit Price",
                    "Shares",
                    "Net P&L ($)",
                    "Return (%)",
                    "Costs ($)",
                ]

                # Format numeric columns
                display_trades["Entry Price"] = display_trades[
                    "Entry Price"
                ].map("${:,.2f}".format)
                display_trades["Exit Price"] = display_trades[
                    "Exit Price"
                ].map("${:,.2f}".format)
                display_trades["Net P&L ($)"] = display_trades[
                    "Net P&L ($)"
                ].map("${:,.2f}".format)
                display_trades["Return (%)"] = display_trades[
                    "Return (%)"
                ].map("{:,.2f}%".format)
                display_trades["Costs ($)"] = display_trades["Costs ($)"].map(
                    "${:,.2f}".format
                )

                st.dataframe(display_trades)

                # Performance distribution chart
                st.subheader("Trade Performance Distribution")

                profit_loss_hist = go.Figure()
                profit_loss_hist.add_trace(
                    go.Histogram(
                        x=trades_df["profit_loss_pct"],
                        nbinsx=20,
                        marker_color=[
                            "green" if x >= 0 else "red"
                            for x in trades_df["profit_loss_pct"]
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

                # Add a vertical line at 0%
                profit_loss_hist.add_vline(
                    x=0, line_dash="dash", line_color="black"
                )

                st.plotly_chart(profit_loss_hist, use_container_width=True)
            else:
                st.info("No completed trades in this period.")


if __name__ == "__main__":
    main()
