"""
Stock Scanner module.

This module provides functionality to scan stocks
for trading signals based on various strategies.
"""

import logging
import pandas as pd
import numpy as np
import os
import sys
import streamlit as st
import concurrent.futures
import time

# Add the src directory to the path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from src.data_fetcher import get_stock_data
from src.feature_factory import FeatureFactory
from src.strategies import SMACrossoverStrategy, RSIStrategy
from src.nan_handler import handle_nans  # Import the new nan_handler

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def scan_stocks(
    tickers,
    period="1y",
    interval="1d",
    strategy_name="SMA Crossover",
    **strategy_params,
):
    """
    Scan multiple stocks for trading signals based on the selected strategy.

    Args:
        tickers (list): List of stock ticker symbols
        period (str): Data period (default: "1y")
        interval (str): Data interval (default: "1d")
        strategy_name (str): Name of the strategy to use
        **strategy_params: Additional parameters for the strategy

    Returns:
        pd.DataFrame: DataFrame with scan results for each ticker
    """
    results = []
    for ticker in tickers:
        try:
            scan_result = scan_stock(
                ticker, period, interval, strategy_name, strategy_params
            )
            results.append(scan_result)
        except Exception as e:
            logger.error(f"Error scanning {ticker}: {str(e)}")
            results.append(
                {
                    "ticker": ticker,
                    "status": "error",
                    "message": str(e),
                    "signal": "none",
                }
            )

    # Convert results to DataFrame
    results_df = pd.DataFrame(results)
    return results_df


def scan_stock(ticker, period, interval, strategy_name, strategy_params):
    """
    Scan a single stock for trading signals based on the selected strategy.

    Args:
        ticker (str): Stock ticker symbol
        period (str): Data period
        interval (str): Data interval
        strategy_name (str): Name of the strategy to use
        strategy_params (dict): Parameters for the strategy

    Returns:
        dict: Scan results including any trading signals
    """
    try:
        # Fetch stock data
        data = get_stock_data(ticker, period, interval)
        if data is None or len(data) < 50:  # Require at least 50 data points
            logger.warning(f"Insufficient data for {ticker}")
            return {
                "ticker": ticker,
                "status": "error",
                "message": "Insufficient data",
                "signal": "none",
            }

        # Determine which feature families to generate based on strategy
        feature_families = []
        if strategy_name == "SMA Crossover":
            feature_families = ["sma"]
        elif strategy_name == "RSI Strategy":
            feature_families = ["rsi"]

        # Generate features
        factory = FeatureFactory(data, feature_families=feature_families)
        features_df = factory.generate_features(
            drop_na=False
        )  # Generate features but don't drop NaNs yet

        # Define critical columns based on the strategy
        critical_columns = ["Close", "Open", "High", "Low"]
        if strategy_name == "SMA Crossover":
            fast_sma = strategy_params.get("fast_sma", 50)
            slow_sma = strategy_params.get("slow_sma", 200)
            critical_columns.extend([f"sma_{fast_sma}", f"sma_{slow_sma}"])
        elif strategy_name == "RSI Strategy":
            rsi_period = strategy_params.get("rsi_period", 14)
            critical_columns.append(f"rsi_{rsi_period}")

        # Use the standardized NaN handling
        original_features_len = len(features_df)
        features_df, nan_stats = handle_nans(
            features_df,
            method="drop",
            drop_na_threshold=0.25,  # Default threshold
            critical_columns=critical_columns,
        )

        # Log NaN handling results
        if nan_stats["rows_dropped"] > 0:
            logger.warning(
                f"Dropped {nan_stats['rows_dropped']} rows ({nan_stats['pct_dropped']:.2f}%) with NaN values "
                f"for {ticker} after feature generation."
            )

        if features_df.empty:
            logger.warning(
                f"No data remaining for {ticker} after dropping NaN values. Cannot generate signals."
            )
            return {
                "ticker": ticker,
                "status": "error",
                "message": "No data after NaN handling",
                "signal": "none",
            }

        # Create and apply strategy
        if strategy_name == "SMA Crossover":
            fast_sma = strategy_params.get("fast_sma", 50)
            slow_sma = strategy_params.get("slow_sma", 200)

            # Check if we have the required columns
            if (
                f"sma_{fast_sma}" not in features_df.columns
                or f"sma_{slow_sma}" not in features_df.columns
            ):
                logger.warning(
                    f"Missing required SMA indicators for {ticker} after NaN handling."
                )
                return {
                    "ticker": ticker,
                    "status": "error",
                    "message": f"Missing SMA indicators for {ticker}",
                    "signal": "none",
                }

            strategy = SMACrossoverStrategy(
                fast_window=fast_sma, slow_window=slow_sma
            )
            features_with_signals = strategy.generate_signals(features_df)

        elif strategy_name == "RSI Strategy":
            rsi_period = strategy_params.get("rsi_period", 14)
            overbought = strategy_params.get("overbought", 70)
            oversold = strategy_params.get("oversold", 30)

            # Check if we have the required column
            if f"rsi_{rsi_period}" not in features_df.columns:
                logger.warning(
                    f"Missing required RSI indicator for {ticker} after NaN handling."
                )
                return {
                    "ticker": ticker,
                    "status": "error",
                    "message": f"Missing RSI indicator for {ticker}",
                    "signal": "none",
                }

            strategy = RSIStrategy(
                rsi_window=rsi_period,
                overbought_threshold=overbought,
                oversold_threshold=oversold,
            )
            features_with_signals = strategy.generate_signals(features_df)
        else:
            logger.error(f"Unknown strategy: {strategy_name}")
            return {
                "ticker": ticker,
                "status": "error",
                "message": f"Unknown strategy: {strategy_name}",
                "signal": "none",
            }

        # Get the last row to check current signal
        if len(features_with_signals) > 0:
            last_row = features_with_signals.iloc[-1]

            if "buy_signal" in last_row and last_row["buy_signal"]:
                signal = "buy"
                signal_details = (
                    f"Buy signal at {last_row.name.strftime('%Y-%m-%d')}"
                )

                # Add strategy-specific details
                if strategy_name == "SMA Crossover":
                    signal_details += f" - Fast SMA ({fast_sma}) crossed above Slow SMA ({slow_sma})"
                elif strategy_name == "RSI Strategy":
                    signal_details += f" - RSI ({rsi_period}) below {oversold} (oversold condition)"

            elif "sell_signal" in last_row and last_row["sell_signal"]:
                signal = "sell"
                signal_details = (
                    f"Sell signal at {last_row.name.strftime('%Y-%m-%d')}"
                )

                # Add strategy-specific details
                if strategy_name == "SMA Crossover":
                    signal_details += f" - Fast SMA ({fast_sma}) crossed below Slow SMA ({slow_sma})"
                elif strategy_name == "RSI Strategy":
                    signal_details += f" - RSI ({rsi_period}) above {overbought} (overbought condition)"
            else:
                signal = "none"
                signal_details = "No active signal"

                # Add current indicator values
                if strategy_name == "SMA Crossover":
                    if all(
                        col in last_row.index
                        for col in [f"sma_{fast_sma}", f"sma_{slow_sma}"]
                    ):
                        fast_val = last_row[f"sma_{fast_sma}"]
                        slow_val = last_row[f"sma_{slow_sma}"]
                        signal_details += f" - Fast SMA: {fast_val:.2f}, Slow SMA: {slow_val:.2f}"

                elif strategy_name == "RSI Strategy":
                    if f"rsi_{rsi_period}" in last_row.index:
                        rsi_val = last_row[f"rsi_{rsi_period}"]
                        signal_details += f" - Current RSI: {rsi_val:.2f}"

                        # Add trending information
                        if rsi_val < 50:
                            signal_details += " (Potentially bearish)"
                        else:
                            signal_details += " (Potentially bullish)"

            # Get the last price
            last_price = last_row["Close"] if "Close" in last_row else None

            return {
                "ticker": ticker,
                "status": "success",
                "signal": signal,
                "signal_details": signal_details,
                "last_price": last_price,
                "as_of_date": last_row.name.strftime("%Y-%m-%d"),
            }
        else:
            return {
                "ticker": ticker,
                "status": "warning",
                "message": "Data available but no signals generated",
                "signal": "none",
            }
    except Exception as e:
        logger.error(f"Error scanning {ticker}: {str(e)}")
        return {
            "ticker": ticker,
            "status": "error",
            "message": str(e),
            "signal": "none",
        }


def run_scanner():
    """
    Run the scanner with Streamlit interface.
    """
    st.title("Stock Scanner")
    st.write("Scan multiple stocks for trading signals")

    # Input for tickers
    tickers_input = st.text_input(
        "Enter ticker symbols (comma-separated)", "AAPL,MSFT,GOOGL,AMZN,META"
    )
    tickers = [t.strip() for t in tickers_input.split(",") if t.strip()]

    # Strategy selection
    selected_strategy = st.selectbox(
        "Select strategy", ["SMA Crossover", "RSI Strategy"]
    )

    # Strategy parameters
    strategy_params = {}
    with st.expander("Strategy Parameters"):
        if selected_strategy == "SMA Crossover":
            st.subheader("SMA Crossover Strategy Parameters")
            fast_sma = st.slider(
                "Fast SMA Window", min_value=5, max_value=50, value=20, step=1
            )
            slow_sma = st.slider(
                "Slow SMA Window",
                min_value=20,
                max_value=200,
                value=50,
                step=1,
            )
            strategy_params = {"fast_sma": fast_sma, "slow_sma": slow_sma}
        elif selected_strategy == "RSI Strategy":
            st.subheader("RSI Strategy Parameters")
            rsi_period = st.slider(
                "RSI Period", min_value=7, max_value=21, value=14, step=1
            )
            overbought = st.slider(
                "RSI Overbought Threshold",
                min_value=60,
                max_value=80,
                value=70,
                step=1,
            )
            oversold = st.slider(
                "RSI Oversold Threshold",
                min_value=20,
                max_value=40,
                value=30,
                step=1,
            )
            strategy_params = {
                "rsi_period": rsi_period,
                "overbought": overbought,
                "oversold": oversold,
            }

    # Data parameters
    with st.expander("Data Parameters"):
        period = st.selectbox(
            "Data Period",
            ["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"],
            index=3,
        )
        interval = st.selectbox(
            "Data Interval",
            ["1d", "5d", "1wk", "1mo"],
            index=0,
        )

    # Run scan button
    if st.button("Run Scan"):
        with st.spinner(f"Scanning {len(tickers)} stocks..."):
            results = scan_stocks(
                tickers,
                period=period,
                interval=interval,
                strategy_name=selected_strategy,
                **strategy_params,
            )

            # Display results
            st.subheader("Scan Results")

            # Filter by signal type
            buy_df = results[results["signal"] == "buy"]
            sell_df = results[results["signal"] == "sell"]
            none_df = results[results["signal"] == "none"]

            # Display buy signals
            if not buy_df.empty:
                st.success(f"Found {len(buy_df)} buy signals")

                # Format the DataFrame for display
                display_columns = ["ticker", "last_price", "signal_details"]

                buy_display = buy_df[display_columns].copy()
                rename_map = {
                    "ticker": "Ticker",
                    "last_price": "Last Price",
                    "signal_details": "Signal Details",
                }
                buy_display = buy_display.rename(columns=rename_map)

                st.dataframe(buy_display, use_container_width=True)
            else:
                st.info("No buy signals found")

            # Display sell signals
            if not sell_df.empty:
                st.warning(f"Found {len(sell_df)} sell signals")

                # Format the DataFrame for display
                display_columns = ["ticker", "last_price", "signal_details"]

                sell_display = sell_df[display_columns].copy()
                rename_map = {
                    "ticker": "Ticker",
                    "last_price": "Last Price",
                    "signal_details": "Signal Details",
                }
                sell_display = sell_display.rename(columns=rename_map)

                st.dataframe(sell_display, use_container_width=True)
            else:
                st.info("No sell signals found")

            # Display errors and no signals
            if not none_df.empty:
                # Separate errors from no signals
                error_df = none_df[none_df["status"] == "error"]
                no_signal_df = none_df[none_df["status"] != "error"]

                if not error_df.empty:
                    st.error(f"Found {len(error_df)} errors")
                    error_display = error_df[["ticker", "message"]].copy()
                    error_display = error_display.rename(
                        columns={
                            "ticker": "Ticker",
                            "message": "Error Message",
                        }
                    )
                    st.dataframe(error_display, use_container_width=True)

                if not no_signal_df.empty:
                    st.info(
                        f"Found {len(no_signal_df)} stocks with no signals"
                    )
                    no_signal_display = no_signal_df[
                        ["ticker", "last_price", "as_of_date"]
                    ].copy()
                    no_signal_display = no_signal_display.rename(
                        columns={
                            "ticker": "Ticker",
                            "last_price": "Last Price",
                            "as_of_date": "As of Date",
                        }
                    )
                    st.dataframe(no_signal_display, use_container_width=True)


if __name__ == "__main__":
    if st.runtime.exists():
        run_scanner()
    else:
        # Example usage from command line
        tickers = ["AAPL", "MSFT", "GOOGL", "AMZN", "META"]
        results = scan_stocks(
            tickers,
            period="1y",
            interval="1d",
            strategy_name="SMA Crossover",
            fast_sma=50,
            slow_sma=200,
        )
        print(results)
