# File Structure

This section describes the relevant directories and files within the codebase.

```
D:/Code/projects/mystockapp/
└── app/
    ├── data_fetcher.py
    ├── feature_factory.py
    └── main.py
```

**Directory:** `app/`
*   **Purpose:** This directory contains the core application logic and source code for the stock data fetching and feature generation tool.

**File:** `app/data_fetcher.py`
*   **Purpose:** This file is responsible for interacting with external data sources to retrieve historical stock market data. It specifically uses the `yfinance` library to fetch OHLCV data for a given ticker symbol, period, and interval. It also implements a simple caching mechanism to store downloaded data locally and reuse it if it's recent, reducing redundant API calls. It provides a general `fetch_stock_data` function and a convenience wrapper `get_reliance_data` for a specific ticker.

**File:** `app/feature_factory.py`
*   **Purpose:** This file contains the `FeatureFactory` class, which is dedicated to calculating various technical indicators from raw OHLCV data. Its primary role is to transform the basic price and volume data into a richer dataset by adding columns representing technical features. It supports multiple indicator types and allows for configuration of their parameters. The implementation focuses on using vectorized operations with pandas and numpy for performance.

**File:** `app/main.py`
*   **Purpose:** This file serves as the main entry point and command-line interface for the application. It handles parsing arguments provided by the user (such as the desired data period, interval, output file path, and which features to generate). It orchestrates the workflow by calling the `data_fetcher` to get the raw data, then using the `FeatureFactory` to add the technical features. Finally, it saves the resulting DataFrame to a CSV file and can optionally generate and save plots of key indicators.
