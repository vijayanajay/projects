"""
Module for fetching historical stock data using yfinance.
"""

import os
import logging
from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


def fetch_stock_data(
    ticker_symbol,
    period="max",
    interval="1d",
    save_to_csv=True,
    cache_dir="data",
):
    """
    Fetch historical stock data using yfinance.

    Args:
        ticker_symbol (str): Stock ticker symbol (e.g., 'RELIANCE.NS' for Reliance NSE)
        period (str): Valid periods: 1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max
        interval (str): Valid intervals: 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
        save_to_csv (bool): Whether to save the data to a CSV file
        cache_dir (str): Directory to save the CSV file

    Returns:
        pd.DataFrame: DataFrame containing the historical stock data
    """
    logger.info(
        f"Fetching {ticker_symbol} data for period={period}, interval={interval}"
    )

    # Create cache directory if it doesn't exist
    if save_to_csv and not os.path.exists(cache_dir):
        os.makedirs(cache_dir)

    # Define cache file path
    cache_file = os.path.join(
        cache_dir, f"{ticker_symbol.replace('.', '_')}_{interval}_{period}.csv"
    )

    # Check if cache file exists and is recent (less than 1 day old)
    if (
        save_to_csv
        and os.path.exists(cache_file)
        and (
            datetime.now()
            - datetime.fromtimestamp(os.path.getmtime(cache_file))
        )
        < timedelta(days=1)
    ):
        logger.info(f"Loading cached data from {cache_file}")
        return pd.read_csv(cache_file, index_col=0, parse_dates=True)

    # Fetch data using yfinance
    try:
        ticker = yf.Ticker(ticker_symbol)
        data = ticker.history(period=period, interval=interval)

        # Check if data was retrieved successfully
        if data.empty:
            logger.error(f"No data retrieved for {ticker_symbol}")
            return None

        logger.info(
            f"Successfully fetched {len(data)} rows of {ticker_symbol} data"
        )

        # Save to CSV if requested
        if save_to_csv:
            data.to_csv(cache_file)
            logger.info(f"Saved data to {cache_file}")

        return data

    except Exception as e:
        logger.error(f"Error fetching data for {ticker_symbol}: {str(e)}")
        return None


def get_reliance_data(period="max", interval="1d", save_to_csv=True):
    """
    Convenience function to fetch Reliance Industries stock data.
    For NSE: 'RELIANCE.NS', for BSE: 'RELIANCE.BO'

    Args:
        period (str): Data period
        interval (str): Data interval
        save_to_csv (bool): Whether to save to CSV

    Returns:
        pd.DataFrame: DataFrame with Reliance stock data
    """
    # NSE ticker symbol for Reliance Industries
    ticker = "RELIANCE.NS"
    return fetch_stock_data(ticker, period, interval, save_to_csv)


if __name__ == "__main__":
    # Example usage
    data = get_reliance_data()
    if data is not None:
        print(f"Retrieved {len(data)} rows of data")
        print(data.head())
