# File: D:/Code/projects/mystockapp/app/data_fetcher.py

This module is responsible for fetching historical stock data, primarily using the `yfinance` library. It includes functionality for specifying the ticker, time period, and interval, and incorporates a basic caching mechanism to store and retrieve recently downloaded data locally.

## Main Components:

1.  **`fetch_stock_data(ticker_symbol, period="max", interval="1d", save_to_csv=True, cache_dir="data")` Function:**
    *   **Purpose:** This is the core function for fetching data. It takes a stock ticker symbol and optional parameters for the data period, interval, whether to save/cache the data, and the directory for caching.
    *   **Inputs:**
        *   `ticker_symbol` (str): The symbol of the stock (e.g., 'RELIANCE.NS').
        *   `period` (str): The duration of data to fetch (e.g., '1y', 'max'). Defaults to 'max'.
        *   `interval` (str): The data frequency (e.g., '1d', '1h'). Defaults to '1d'.
        *   `save_to_csv` (bool): If True, data is saved to a CSV cache file and loaded from it if recent. Defaults to True.
        *   `cache_dir` (str): The directory path for storing cache files. Defaults to "data".
    *   **Logic:**
        *   It first constructs a cache file path based on the ticker, interval, and period within the specified `cache_dir`.
        *   If `save_to_csv` is True, it checks if the cache file exists and if its modification time is less than 24 hours ago.
        *   If a valid, recent cache file is found, it logs a message and loads the data directly from the CSV using `pd.read_csv`, setting the index to the date column and parsing dates.
        *   If no valid cache is found or `save_to_csv` is False, it proceeds to fetch data using `yfinance`. It creates a `yf.Ticker` object and calls its `history()` method with the specified `period` and `interval`.
        *   It checks if the returned DataFrame is empty, logging an error if no data was retrieved.
        *   If data is successfully fetched and `save_to_csv` is True, it saves the DataFrame to the constructed cache file using `data.to_csv`.
        *   Error handling is included to catch exceptions during the fetching process.
    *   **Output:** Returns a pandas DataFrame containing the historical OHLCV data, or `None` if fetching fails or no data is retrieved.

2.  **`get_reliance_data(period="max", interval="1d", save_to_csv=True)` Function:**
    *   **Purpose:** This is a convenience wrapper specifically designed to fetch data for Reliance Industries (using the 'RELIANCE.NS' ticker for the National Stock Exchange of India).
    *   **Inputs:** Takes the same `period`, `interval`, and `save_to_csv` arguments as `fetch_stock_data`.
    *   **Logic:** Simply calls `fetch_stock_data` with the hardcoded ticker 'RELIANCE.NS' and passes through the provided arguments.
    *   **Output:** Returns the pandas DataFrame fetched by `fetch_stock_data` for Reliance, or `None`.

The module also includes basic logging setup to provide feedback on the data fetching process, including cache usage and success/failure messages. The `if __name__ == "__main__":` block demonstrates how to use the `get_reliance_data` function to fetch and print sample data.
