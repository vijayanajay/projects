import pandas as pd
import yfinance as yf

def fetch_ohlcv_data(tickers, start_date, end_date):
    """
    Fetches OHLCV data for given tickers and date range using yfinance.
    
    Args:
        tickers (str or list): Stock ticker symbol(s)
        start_date (str): Start date in 'YYYY-MM-DD' format
        end_date (str): End date in 'YYYY-MM-DD' format
        
    Returns:
        pd.DataFrame: DataFrame with OHLCV data. For single tickers, columns are ['Open', 'High', ...].
                     For multiple tickers, columns are MultiIndex with (Ticker, Metric).
        
    Raises:
        ValueError: If ticker is invalid or data is unavailable
    """
    # Convert single ticker to list
    if isinstance(tickers, str):
        tickers = [tickers]
    
    # Download data from yfinance
    try:
        data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=False, progress=False)
        
        # Validate data exists
        if data.empty:
            raise ValueError("No data found for the specified ticker(s) and date range.")

        required_columns = ['Open', 'High', 'Low', 'Close', 'Volume']

        if isinstance(data.columns, pd.MultiIndex):
            # Handle multi-index columns (multiple tickers)
            original_names = data.columns.names
            # Convert Price level (level 0) column names to title case for consistency
            data.columns = pd.MultiIndex.from_tuples([
                (price.title(), ticker) for price, ticker in data.columns
            ], names=original_names)
            
            # Filter columns where the Price level (level 0) is in required_columns
            data = data.loc[:, data.columns.get_level_values(0).isin(required_columns)]
            
            # Ensure all required columns are present for each ticker after filtering
            for ticker in tickers:
                # Check for (RequiredColumn, Ticker) tuples in the potentially filtered columns
                missing_cols = [col for col in required_columns if (col, ticker) not in data.columns]
                if missing_cols:
                    # Raise error showing which columns are missing for which ticker
                    raise ValueError(f"Missing required OHLCV columns {missing_cols} for ticker {ticker} after processing. Filtered columns: {list(data.columns)}")
        else:
            # Handle single-index columns (single ticker)
            # Convert column names to title case for consistency
            data.columns = [col.title() for col in data.columns]
            # Drop Adj Close column if present
            if 'Adj Close' in data.columns:
                data = data.drop(columns=['Adj Close'])
            # Ensure all required columns are present
            missing_cols = [col for col in required_columns if col not in data.columns]
            if missing_cols:
                raise ValueError(f"Missing OHLCV columns {missing_cols}. Columns received: {list(data.columns)}")
            # Filter to only required columns
            data = data[required_columns]

        # Ensure index is datetime type
        if not isinstance(data.index, pd.DatetimeIndex):
            data.index = pd.to_datetime(data.index)
        
        return data

    except Exception as e:
        # Convert yfinance exceptions to ValueError for interface consistency
        raise ValueError(f"Failed to fetch data for {tickers}: {str(e)}") from e

def detect_missing_data(data):
    """Check for gaps in time series data index or NaN values in the data.
    
    Args:
        data (pd.DataFrame): Time series data with datetime index
        
    Returns:
        bool: True if no gaps or NaN values are detected
        
    Raises:
        ValueError: If gaps or NaN values are found in the time series
    """
    try:
        if not isinstance(data.index, pd.DatetimeIndex):
            raise ValueError("Data must have datetime index")
            
        expected_dates = pd.date_range(
            start=data.index[0],
            end=data.index[-1],
            freq='B' if data.index.dayofweek.max() < 5 else 'D'
        )
        
        missing_dates = expected_dates[~expected_dates.isin(data.index)]
        
        if not missing_dates.empty:
            raise ValueError(f"Missing data detected: {len(missing_dates)} date gaps found.")

        # Check for NaN values within the DataFrame
        if data.isnull().values.any():
            raise ValueError("Missing data detected: NaN values found in data.")
            
        return True
    except Exception as e:
        # Keep the original exception context if possible, otherwise wrap
        if isinstance(e, ValueError): # Don't double-wrap ValueErrors
             raise e
        raise ValueError(f"Error during missing data detection: {str(e)}") from e
def handle_missing_data(data):
    """
    Handles missing data in a DataFrame using forward-fill.

    Args:
        data (pd.DataFrame): DataFrame with potential NaN values.

    Returns:
        pd.DataFrame: DataFrame with NaN values forward-filled.
    """
    # Check if there are any NaN values first (optional, but good practice)
    if data.isnull().values.any():
        # Apply forward fill
        filled_data = data.fillna(method='ffill')
        
        # Optional: Check if any NaNs remain (e.g., at the beginning)
        if filled_data.isnull().values.any():
            # Decide on a strategy: backfill, drop, raise error, or leave as is
            # For simplicity per Kailash Nadh philosophy, we'll leave initial NaNs for now.
            # A more robust solution might backfill or require complete data.
            pass # Or add logging/warning
            
        return filled_data
    else:
        # No NaNs found, return original data
        return data