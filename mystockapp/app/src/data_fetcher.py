"""
Module for fetching historical stock data using yfinance.
"""

import os
import logging
from datetime import datetime, timedelta
import pandas as pd
import warnings
import yfinance as yf
import requests
import streamlit as st

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

# Define a global constant for Streamlit cache TTL (1 day by default)
STREAMLIT_CACHE_TTL_DAYS = 1


@st.cache_data(ttl=timedelta(days=STREAMLIT_CACHE_TTL_DAYS))
def fetch_stock_data(
    ticker_symbol,
    period="max",
    interval="1d",
    save_to_csv=True,
    cache_dir="data",
    cache_expiry_days=1,
):
    """
    Fetch historical stock data using yfinance.

    Args:
        ticker_symbol (str): Stock ticker symbol (e.g., 'RELIANCE.NS' for Reliance NSE)
        period (str): Valid periods: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
        interval (str): Valid intervals: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
        save_to_csv (bool): Whether to save the data to a CSV file
        cache_dir (str): Directory to save the CSV file
        cache_expiry_days (int): Number of days before cached data expires (for file-based cache)

    Returns:
        pd.DataFrame: DataFrame containing the historical stock data or None if data fetching fails
    """
    # Validate inputs
    if not ticker_symbol:
        logger.error("No ticker symbol provided")
        return None

    valid_periods = [
        "1d",
        "5d",
        "1mo",
        "3mo",
        "6mo",
        "1y",
        "2y",
        "5y",
        "10y",
        "ytd",
        "max",
    ]
    if period not in valid_periods:
        logger.error(
            f"Invalid period: {period}. Valid options are: {valid_periods}"
        )
        return None

    valid_intervals = [
        "1m",
        "2m",
        "5m",
        "15m",
        "30m",
        "60m",
        "90m",
        "1h",
        "1d",
        "5d",
        "1wk",
        "1mo",
        "3mo",
    ]
    if interval not in valid_intervals:
        logger.error(
            f"Invalid interval: {interval}. Valid options are: {valid_intervals}"
        )
        return None

    # Check for incompatible period/interval combinations
    if period == "1d" and interval in ["1d", "5d", "1wk", "1mo", "3mo"]:
        logger.error(
            f"Incompatible period/interval combination: period={period}, interval={interval}"
        )
        logger.error(
            "For 1d period, interval must be 1m, 2m, 5m, 15m, 30m, 60m, 90m, or 1h"
        )
        return None

    logger.info(
        f"Fetching {ticker_symbol} data for period={period}, interval={interval}"
    )

    # Create cache directory if it doesn't exist
    if save_to_csv and not os.path.exists(cache_dir):
        try:
            os.makedirs(cache_dir)
            logger.info(f"Created cache directory: {cache_dir}")
        except Exception as e:
            logger.error(
                f"Failed to create cache directory {cache_dir}: {str(e)}"
            )
            logger.warning(
                "Will attempt to fetch data but won't be able to cache it"
            )
            save_to_csv = False

    # Define cache file path
    cache_file = None
    if save_to_csv:
        cache_file = os.path.join(
            cache_dir,
            f"{ticker_symbol.replace('.', '_')}_{interval}_{period}.csv",
        )

    # Check if cache file exists and is recent
    cache_is_valid = False
    if save_to_csv and cache_file and os.path.exists(cache_file):
        try:
            file_age = datetime.now() - datetime.fromtimestamp(
                os.path.getmtime(cache_file)
            )
            if file_age < timedelta(days=cache_expiry_days):
                logger.info(
                    f"Loading cached data from {cache_file} (age: {file_age.total_seconds()/3600:.1f} hours)"
                )
                try:
                    data = pd.read_csv(
                        cache_file, index_col=0, parse_dates=True
                    )
                    if not data.empty:
                        return data
                    logger.warning(
                        f"Cached file exists but is empty or invalid, fetching fresh data"
                    )
                except Exception as e:
                    logger.warning(
                        f"Failed to load cached data: {str(e)}, fetching fresh data"
                    )
            else:
                logger.info(
                    f"Cached data is too old ({file_age.days} days), fetching fresh data"
                )
        except Exception as e:
            logger.warning(f"Error checking cache file {cache_file}: {str(e)}")

    # Fetch data using yfinance
    try:
        logger.info(f"Downloading data from Yahoo Finance for {ticker_symbol}")
        ticker = yf.Ticker(ticker_symbol)
        data = ticker.history(period=period, interval=interval)

        # Check if data was retrieved successfully
        if data.empty:
            logger.error(f"No data retrieved for {ticker_symbol}")
            return None

        # Check if data contains NaN values in OHLCV columns
        ohlcv_nan_counts = (
            data[["Open", "High", "Low", "Close", "Volume"]].isna().sum()
        )
        if ohlcv_nan_counts.sum() > 0:
            logger.warning(
                f"Retrieved data contains NaN values in OHLCV columns: {ohlcv_nan_counts[ohlcv_nan_counts > 0].to_dict()}"
            )
            logger.warning(
                "NaN values may cause issues in downstream analysis. Consider dropping or filling NaN values."
            )

        logger.info(
            f"Successfully fetched {len(data)} rows of {ticker_symbol} data"
        )

        # Save to CSV if requested
        if save_to_csv and cache_file:
            try:
                data.to_csv(cache_file)
                logger.info(f"Saved data to {cache_file}")
            except Exception as e:
                logger.error(f"Failed to save data to {cache_file}: {str(e)}")

        return data

    except requests.exceptions.RequestException as e:
        logger.exception(
            f"Network error when fetching data for {ticker_symbol}: {str(e)}"
        )
        return None
    except ValueError as e:
        logger.exception(
            f"Invalid parameter when fetching {ticker_symbol}: {str(e)}"
        )
        return None
    except Exception as e:
        # Fallback for unexpected errors
        logger.exception(
            f"Unexpected error fetching data for {ticker_symbol}: {str(e)}"
        )
        return None


def get_stock_data(
    ticker_symbol, period="max", interval="1d", save_to_csv=True
):
    """
    Get stock data for any ticker symbol.

    This is the main entry point for fetching stock data.

    Args:
        ticker_symbol (str): Stock ticker symbol (e.g., 'RELIANCE.NS', 'AAPL')
        period (str): Data period
        interval (str): Data interval
        save_to_csv (bool): Whether to save to CSV

    Returns:
        pd.DataFrame: DataFrame with stock data or None if fetching failed

    Examples:
        >>> # Get Reliance data from NSE
        >>> reliance_data = get_stock_data("RELIANCE.NS")
        >>>
        >>> # Get Apple data with custom period and interval
        >>> apple_data = get_stock_data("AAPL", period="1y", interval="1d")
    """
    return fetch_stock_data(ticker_symbol, period, interval, save_to_csv)


def get_reliance_data(period="max", interval="1d", save_to_csv=True):
    """
    DEPRECATED: Convenience function to fetch Reliance Industries stock data.

    This function is DEPRECATED and will be removed in a future version.
    Use get_stock_data("RELIANCE.NS") instead.

    For NSE: 'RELIANCE.NS', for BSE: 'RELIANCE.BO'

    Args:
        period (str): Data period
        interval (str): Data interval
        save_to_csv (bool): Whether to save to CSV

    Returns:
        pd.DataFrame: DataFrame with Reliance stock data

    Deprecated since: v1.1.0
    Will be removed in: v2.0.0
    """
    warnings.warn(
        "get_reliance_data is deprecated and will be removed in v2.0.0. "
        'Use get_stock_data("RELIANCE.NS") instead.',
        DeprecationWarning,
        stacklevel=2,
    )

    logger.warning(
        "get_reliance_data is deprecated and will be removed in v2.0.0. "
        'Use get_stock_data("RELIANCE.NS") instead.'
    )

    # NSE ticker symbol for Reliance Industries
    ticker = "RELIANCE.NS"
    return fetch_stock_data(ticker, period, interval, save_to_csv)


if __name__ == "__main__":
    # Example usage
    # Get Reliance data (NSE)
    reliance_data = get_stock_data("RELIANCE.NS")
    if reliance_data is not None:
        print(f"Retrieved {len(reliance_data)} rows of Reliance data")
        print(reliance_data.head())

    # Get Tesla data
    tesla_data = get_stock_data("TSLA")
    if tesla_data is not None:
        print(f"Retrieved {len(tesla_data)} rows of Tesla data")
        print(tesla_data.head())
