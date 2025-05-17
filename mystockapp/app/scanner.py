"""
Stock Scanner - Identify Trading Opportunities

This module provides functionality to scan multiple stocks for trading opportunities
based on technical indicators and pre-defined strategies.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta
import os
import logging
import sys
import concurrent.futures
import time

# Add the app directory to the path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import our modules
from src.data_fetcher import get_stock_data
from src.feature_factory import FeatureFactory
from src.backtester import SMACrossoverStrategy, RSIStrategy

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# App configuration
st.set_page_config(
    page_title="Stock Scanner",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Default stock list - some popular Indian stocks as examples
DEFAULT_STOCKS = [
    "RELIANCE.NS",  # Reliance Industries
    "TCS.NS",  # Tata Consultancy Services
    "HDFCBANK.NS",  # HDFC Bank
    "INFY.NS",  # Infosys
    "BHARTIARTL.NS",  # Bharti Airtel
    "ITC.NS",  # ITC Limited
    "SBIN.NS",  # State Bank of India
    "HINDUNILVR.NS",  # Hindustan Unilever
    "AXISBANK.NS",  # Axis Bank
    "ICICIBANK.NS",  # ICICI Bank
]


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
        features_df = factory.generate_features()

        # Drop any row with any NaN
        original_features_len = len(features_df)
        features_df = features_df.dropna()
        rows_dropped_nan = original_features_len - len(features_df)
        if rows_dropped_nan > 0:
            logger.warning(
                f"Dropped {rows_dropped_nan} rows with NaN values for {ticker} after feature generation."
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

        elif strategy_name == "RSI Strategy":
            rsi_window = strategy_params.get("rsi_window", 14)
            oversold = strategy_params.get("oversold", 30)
            overbought = strategy_params.get("overbought", 70)

            # Check if we have the required column
            if f"rsi_{rsi_window}" not in features_df.columns:
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
                rsi_window=rsi_window,
                oversold_threshold=oversold,
                overbought_threshold=overbought,
            )
        else:
            logger.error(f"Invalid strategy: {strategy_name}")
            return {
                "ticker": ticker,
                "status": "error",
                "message": f"Invalid strategy: {strategy_name}",
                "signal": "none",
            }

        # Generate signals
        features_df = strategy.generate_signals(features_df)

        # Check last 5 days for signals
        last_n_days = min(5, len(features_df))
        recent_data = features_df.iloc[-last_n_days:]

        buy_signals = recent_data["buy_signal"].sum()
        sell_signals = recent_data["sell_signal"].sum()

        # Prepare result
        result = {
            "ticker": ticker,
            "status": "success",
            "last_price": features_df["Close"].iloc[-1],
            "date": features_df.index[-1].strftime("%Y-%m-%d"),
        }

        # Determine signal
        if buy_signals > 0:
            result["signal"] = "buy"
            result["signal_date"] = (
                recent_data[recent_data["buy_signal"]]
                .index[-1]
                .strftime("%Y-%m-%d")
            )

            # Add indicator values
            if strategy_name == "SMA Crossover":
                result["fast_sma"] = features_df[f"sma_{fast_sma}"].iloc[-1]
                result["slow_sma"] = features_df[f"sma_{slow_sma}"].iloc[-1]
            elif strategy_name == "RSI Strategy":
                result["rsi"] = features_df[f"rsi_{rsi_window}"].iloc[-1]

        elif sell_signals > 0:
            result["signal"] = "sell"
            result["signal_date"] = (
                recent_data[recent_data["sell_signal"]]
                .index[-1]
                .strftime("%Y-%m-%d")
            )

            # Add indicator values
            if strategy_name == "SMA Crossover":
                result["fast_sma"] = features_df[f"sma_{fast_sma}"].iloc[-1]
                result["slow_sma"] = features_df[f"sma_{slow_sma}"].iloc[-1]
            elif strategy_name == "RSI Strategy":
                result["rsi"] = features_df[f"rsi_{rsi_window}"].iloc[-1]

        else:
            result["signal"] = "none"

            # Add current indicator values anyway for reference
            if strategy_name == "SMA Crossover":
                result["fast_sma"] = features_df[f"sma_{fast_sma}"].iloc[-1]
                result["slow_sma"] = features_df[f"sma_{slow_sma}"].iloc[-1]
            elif strategy_name == "RSI Strategy":
                result["rsi"] = features_df[f"rsi_{rsi_window}"].iloc[-1]

        return result

    except Exception as e:
        logger.exception(f"Error scanning {ticker}: {str(e)}")
        return {
            "ticker": ticker,
            "status": "error",
            "message": str(e),
            "signal": "none",
        }


def scan_stocks(
    tickers, period, interval, strategy_name, strategy_params, max_workers=5
):
    """
    Scan multiple stocks in parallel.

    Args:
        tickers (list): List of ticker symbols
        period (str): Data period
        interval (str): Data interval
        strategy_name (str): Name of the strategy to use
        strategy_params (dict): Parameters for the strategy
        max_workers (int): Maximum number of parallel workers

    Returns:
        list: List of scan results
    """
    results = []

    # Use ThreadPoolExecutor for parallel processing
    with concurrent.futures.ThreadPoolExecutor(
        max_workers=max_workers
    ) as executor:
        # Submit tasks
        future_to_ticker = {
            executor.submit(
                scan_stock,
                ticker,
                period,
                interval,
                strategy_name,
                strategy_params,
            ): ticker
            for ticker in tickers
        }

        # Create a progress bar
        progress_bar = st.progress(0)
        total_tickers = len(tickers)
        completed = 0

        # Process results as they complete
        for future in concurrent.futures.as_completed(future_to_ticker):
            ticker = future_to_ticker[future]
            try:
                result = future.result()
                results.append(result)
            except Exception as e:
                logger.exception(f"Error processing {ticker}: {str(e)}")
                results.append(
                    {
                        "ticker": ticker,
                        "status": "error",
                        "message": str(e),
                        "signal": "none",
                    }
                )

            # Update progress bar
            completed += 1
            progress_bar.progress(completed / total_tickers)

    return results


def main():
    # App title and description
    st.title("Stock Scanner")
    st.markdown(
        """
        Scan multiple stocks for trading opportunities based on technical indicators.

        Enter stock symbols to scan, select your strategy, and find potential trading signals.
        """
    )

    # Sidebar for user inputs
    with st.sidebar:
        st.header("Scanner Settings")

        # Data fetch settings
        st.subheader("Stock Data")
        stocks_input = st.text_area(
            "Stock Tickers (one per line)",
            value="\n".join(DEFAULT_STOCKS),
            height=200,
            help="Enter one ticker symbol per line. Use .NS suffix for NSE stocks, .BO for BSE.",
        )
        period_options = ["1mo", "3mo", "6mo", "1y", "2y", "5y", "max"]
        period = st.selectbox("Time Period", period_options, index=2)
        interval_options = ["1d", "5d", "1wk", "1mo"]
        interval = st.selectbox("Interval", interval_options, index=0)

        # Strategy selection
        st.subheader("Strategy")
        strategy_options = ["SMA Crossover", "RSI Strategy"]
        selected_strategy = st.selectbox(
            "Trading Strategy", strategy_options, index=0
        )

        # Strategy-specific parameters
        strategy_params = {}
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
            strategy_params = {"fast_sma": fast_sma, "slow_sma": slow_sma}
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
            strategy_params = {
                "rsi_window": rsi_window,
                "oversold": rsi_oversold,
                "overbought": rsi_overbought,
            }

        # Concurrency setting
        max_workers = st.slider(
            "Max Concurrent Workers", min_value=1, max_value=10, value=3
        )

        # Action button
        run_scan = st.button("Scan Stocks")

    # Process the list of tickers
    tickers = [
        ticker.strip() for ticker in stocks_input.split("\n") if ticker.strip()
    ]

    # Main content area
    if run_scan:
        if not tickers:
            st.error("Please enter at least one valid ticker symbol.")
            return

        st.subheader("Scanning Stocks")
        st.write(
            f"Scanning {len(tickers)} stocks using {selected_strategy}..."
        )

        # Run the scanner
        scan_start_time = time.time()
        results = scan_stocks(
            tickers,
            period,
            interval,
            selected_strategy,
            strategy_params,
            max_workers=max_workers,
        )
        scan_duration = time.time() - scan_start_time

        st.success(f"Scan completed in {scan_duration:.2f} seconds")

        # Filter and organize results
        buy_signals = [r for r in results if r["signal"] == "buy"]
        sell_signals = [r for r in results if r["signal"] == "sell"]
        no_signals = [r for r in results if r["signal"] == "none"]
        errors = [r for r in results if r["status"] == "error"]

        # Display buy signals
        st.subheader(f"Buy Signals ({len(buy_signals)})")
        if buy_signals:
            buy_df = pd.DataFrame(buy_signals)

            # Format the DataFrame for display
            display_columns = ["ticker", "last_price", "signal_date"]

            # Add strategy-specific columns
            if selected_strategy == "SMA Crossover":
                display_columns.extend(["fast_sma", "slow_sma"])
            elif selected_strategy == "RSI Strategy":
                display_columns.append("rsi")

            buy_display = buy_df[display_columns].copy()

            # Format and rename columns
            rename_map = {
                "ticker": "Ticker",
                "last_price": "Last Price",
                "signal_date": "Signal Date",
                "fast_sma": f'SMA({strategy_params["fast_sma"]})',
                "slow_sma": f'SMA({strategy_params["slow_sma"]})',
                "rsi": f'RSI({strategy_params["rsi_window"]})',
            }
            buy_display = buy_display.rename(columns=rename_map)

            # Round numeric columns
            numeric_cols = buy_display.select_dtypes(
                include=[np.number]
            ).columns
            buy_display[numeric_cols] = buy_display[numeric_cols].round(2)

            st.dataframe(buy_display, use_container_width=True)
        else:
            st.info("No buy signals detected.")

        # Display sell signals
        st.subheader(f"Sell Signals ({len(sell_signals)})")
        if sell_signals:
            sell_df = pd.DataFrame(sell_signals)

            # Format the DataFrame for display
            display_columns = ["ticker", "last_price", "signal_date"]

            # Add strategy-specific columns
            if selected_strategy == "SMA Crossover":
                display_columns.extend(["fast_sma", "slow_sma"])
            elif selected_strategy == "RSI Strategy":
                display_columns.append("rsi")

            sell_display = sell_df[display_columns].copy()

            # Format and rename columns
            rename_map = {
                "ticker": "Ticker",
                "last_price": "Last Price",
                "signal_date": "Signal Date",
                "fast_sma": f'SMA({strategy_params["fast_sma"]})',
                "slow_sma": f'SMA({strategy_params["slow_sma"]})',
                "rsi": f'RSI({strategy_params["rsi_window"]})',
            }
            sell_display = sell_display.rename(columns=rename_map)

            # Round numeric columns
            numeric_cols = sell_display.select_dtypes(
                include=[np.number]
            ).columns
            sell_display[numeric_cols] = sell_display[numeric_cols].round(2)

            st.dataframe(sell_display, use_container_width=True)
        else:
            st.info("No sell signals detected.")

        # Display errors
        if errors:
            st.subheader("Errors")
            error_df = pd.DataFrame(errors)[["ticker", "message"]]
            error_df = error_df.rename(
                columns={"ticker": "Ticker", "message": "Error Message"}
            )
            st.dataframe(error_df, use_container_width=True)


if __name__ == "__main__":
    main()
