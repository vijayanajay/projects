# Project Directory Structure

```
project_root/
├── Include/
├── Lib/
│   └── site-packages/
├── Scripts/
├── app/
│   ├── .pytest_cache/
│   ├── __pycache__/
│   ├── clinerules/
│   │   └── .clinerules
│   ├── config.ini
│   ├── config_loader.py
│   ├── data_handler.py
│   ├── productdescription.txt
│   ├── strategy_optimizer.py
│   ├── tasks.md
│   ├── test_config_loader.py
│   └── test_data_handler.py
├── pyvenv.cfg
```

---

# File Descriptions and Method Explanations

## app/config_loader.py
**Purpose:**
Loads and validates configuration parameters from an INI file for the application.

**Functions:**
- `load_config(config_path='config.ini')`
  - Loads configuration from the specified INI file.
  - Validates required parameters and types.
  - Returns a dictionary of configuration values.
  - Raises `ValueError` if any required section or parameter is missing or invalid.

---

## app/data_handler.py
**Purpose:**
Handles data fetching and validation for OHLCV (Open, High, Low, Close, Volume) stock data.

**Functions:**
- `fetch_ohlcv_data(tickers, start_date, end_date)`
  - Fetches OHLCV data for one or more tickers using yfinance.
  - Ensures required columns and correct formatting.
  - Handles both single and multiple ticker cases.
  - Raises `ValueError` if data is missing or invalid.

- `detect_missing_data(data)`
  - Checks for gaps in a datetime-indexed DataFrame.
  - Returns `True` if no gaps are found.
  - Raises `ValueError` if missing dates are detected.

---

## app/strategy_optimizer.py
**Purpose:**
Defines the `StrategyOptimizer` class for optimizing trading strategy parameters and backtesting.

**Classes and Methods:**
- `StrategyOptimizer(config)`
  - Initializes with configuration and loads OHLCV data.

- `calculate_moving_average(prices, window)`
  - Calculates a simple moving average over a specified window.

- `generate_signals(short_ma, long_ma)`
  - Generates trading signals based on moving average crossover logic (buy/sell).

- `calculate_position_size(portfolio_value, volatility)`
  - Calculates position size based on portfolio value and volatility.

- `backtest_strategy(signals)`
  - Runs a backtest using generated signals.
  - Computes total, annualized return, volatility, and Sharpe ratio.

- `optimize_parameters()`
  - Performs walk-forward optimization to find the best moving average parameters.
  - Returns best parameters and associated performance metrics.

---

## app/test_config_loader.py
**Purpose:**
Unit tests for configuration loading and validation logic.

**Functions:**
- `test_valid_config()`
  - Tests loading a valid configuration and type correctness.
- `test_missing_required_section()`
  - Tests error handling for missing `[DEFAULT]` section.
- `test_missing_required_parameter()`
  - Tests error handling for missing required parameters.

---

## app/test_data_handler.py
**Purpose:**
Unit tests for data fetching and validation functions.

**Functions:**
- `test_ohlcv_structure()`
  - Tests correct structure and columns of fetched OHLCV data.
- `test_data_fetching_error_handling()`
  - Tests error handling for invalid ticker symbols.
- `test_fetch_ohlcv_data_invalid_ticker()`
  - Tests graceful failure for invalid ticker input.
- `test_detect_missing_data_identifies_gaps()`
  - Tests that missing dates are detected in time series data.
- `test_detect_missing_data_passes_with_no_gaps()`
  - Tests that no error is raised when data has no missing dates.

---

## app/config.ini
**Purpose:**
Stores default configuration parameters for the application in INI format.

---

## app/clinerules/.clinerules
**Purpose:**
Project-specific rules or settings (details not shown).

---

## app/productdescription.txt
**Purpose:**
Contains a textual description of the product (details not shown).

---

## app/tasks.md
**Purpose:**
Tracks project tasks and progress (details not shown).

---

## pyvenv.cfg, Include/, Lib/, Scripts/
**Purpose:**
Standard Python virtual environment directories and files.
- `pyvenv.cfg`: Virtual environment configuration.
- `Include/`, `Lib/`, `Scripts/`: Standard venv structure for Python packages, binaries, and headers.

---

# Notes
- All code and tests are located in the `app/` directory.
- The project uses TDD principles and includes robust error handling and validation throughout.
