import yfinance as yf
import numpy as np
import pandas as pd
from .stocks_list import STOCKS_LIST

# Fetch data for a single stock
# Now supports start_date, end_date, and frequency (preferred over period)
def fetch_stock_data(ticker, period=None, start_date=None, end_date=None, frequency=None):
    stock = yf.Ticker(ticker)
    if start_date and end_date:
        # yfinance expects interval for frequency (e.g., '1d', '1h')
        interval = frequency if frequency else '1d'
        return stock.history(start=start_date, end=end_date, interval=interval)
    else:
        period = period if period else '10y'
        return stock.history(period=period)

# Fetch data for all stocks in STOCKS_LIST
def fetch_all_stocks_data(period=None, start_date=None, end_date=None, frequency=None):
    data = {}
    for ticker in STOCKS_LIST:
        try:
            data[ticker] = fetch_stock_data(
                ticker,
                period=period,
                start_date=start_date,
                end_date=end_date,
                frequency=frequency
            )
        except Exception as e:
            print (f"Error fetching data for {ticker}: {e}")
            data[ticker] = f"Error: {e}"
    return data

def clean_and_validate_data(df):
    """
    Cleans and validates raw stock data by handling missing values and capping outliers.
    - Missing values: filled using forward fill, then backward fill as fallback.
    - Outliers: capped at 99th percentile for numeric columns.
    """
    # Fill missing values
    df_clean = df.ffill().bfill()
    # Cap outliers at 99th percentile for each column
    for col in df_clean.select_dtypes(include=[np.number]).columns:
        cap = df_clean[col].quantile(0.99)
        df_clean[col] = np.where(df_clean[col] > cap, cap, df_clean[col])
    return df_clean

def cache_to_parquet(df, filename):
    """
    Caches the given DataFrame to a Parquet file.
    """
    df.to_parquet(filename)

def load_from_parquet(filename):
    """
    Loads a DataFrame from a Parquet file.
    """
    return pd.read_parquet(filename)
