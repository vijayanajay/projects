# Reliance Stock Technical Indicator Generator and Backtester

This project downloads historical Reliance Industries stock data from Yahoo Finance, generates a comprehensive set of technical indicators using a configurable `FeatureFactory`, and provides a framework for backtesting trading strategies.

## Features

- Download historical Reliance stock data using yfinance (maximum available period)
- Generate technical indicators including:
  - Moving Averages (SMA, EMA)
  - RSI (Relative Strength Index)
  - MACD (Moving Average Convergence Divergence)
  - Bollinger Bands
  - ATR (Average True Range)
  - Volume indicators (OBV, Volume MA, etc.)
- Vectorized and optimized calculations using Pandas/NumPy
- Configurable indicator parameters and feature families
- Data type optimization (float32) for memory efficiency
- Data caching to avoid redundant API calls
- Visualization of key indicators
- Backtesting framework for trading strategies with:
  - In-sample and out-of-sample testing
  - Performance metrics (total return, win rate, max drawdown, etc.)
  - Strategy signal visualization
  - Comparison reporting between periods

## Requirements

- Python 3.7+
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository
2. Create a virtual environment (recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Basic Usage

Run the main script to download Reliance stock data and generate all technical indicators:

```bash
python main.py
```

This will:
1. Download the maximum available historical data for Reliance Industries (NSE)
2. Generate all technical indicators
3. Save the results to `data/reliance_features.csv`

### Command-line Options

```
python main.py [OPTIONS]
```

Available options:
- `--period`: Data period (default: 'max')
  - Valid values: '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'
- `--interval`: Data interval (default: '1d')
  - Valid values: '1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'
- `--output`: Output CSV file path (default: 'data/reliance_features.csv')
- `--plot`: Generate plots of key indicators
- `--features`: Comma-separated list of feature families to generate (default: 'all')
  - Valid values: 'sma', 'ema', 'rsi', 'macd', 'bollinger_bands', 'atr', 'volume'
  - Example: `--features sma,rsi,macd`
- `--no-cache`: Disable data caching

### Backtesting Options

- `--split-date`: Date to split data into in-sample and out-of-sample periods (YYYY-MM-DD format)
- `--initial-capital`: Initial capital for backtesting (default: 100000.0)
- `--strategy`: Trading strategy to backtest (default: 'sma_crossover')
- `--fast-sma`: Fast SMA window size for crossover strategy (default: 50)
- `--slow-sma`: Slow SMA window size for crossover strategy (default: 200)

### Examples

Generate only Moving Averages and RSI indicators:
```bash
python main.py --features sma,ema,rsi
```

Download data for the last 5 years with weekly intervals and generate plots:
```bash
python main.py --period 5y --interval 1wk --plot
```

Save output to a custom location:
```bash
python main.py --output results/reliance_indicators.csv
```

Run a backtest with SMA crossover strategy (50 and 200 periods) using 2019-01-01 as the split date:
```bash
python main.py --period max --interval 1d --split-date 2019-01-01 --initial-capital 100000 --strategy sma_crossover --plot
```

Backtest with custom SMA parameters:
```bash
python main.py --split-date 2019-01-01 --fast-sma 20 --slow-sma 100 --plot
```

## Project Structure

- `main.py`: Main script to download data, generate features and run backtests
- `data_fetcher.py`: Module for fetching historical stock data using yfinance
- `feature_factory.py`: Implementation of the `FeatureFactory` component
- `backtester.py`: Implementation of the backtesting framework
- `data/`: Directory for cached data and output files
- `plots/`: Directory for generated plots (when using `--plot` option)

## `FeatureFactory` Component

The `FeatureFactory` class is a configurable and extensible component for generating technical indicators. It takes OHLCV data (in the form of a Pandas DataFrame) as input and generates a comprehensive set of technical indicators.

Features:
- Configurable feature families
- Customizable parameters for each indicator
- Optimized data types (float32 by default)
- Vectorized calculations for performance
- Clear column naming conventions

Usage:
```python
from feature_factory import FeatureFactory

# Create a feature factory with default settings (all features)
factory = FeatureFactory(ohlcv_data)

# Generate features
features_df = factory.generate_features()

# Create a feature factory with custom feature families
factory = FeatureFactory(
    ohlcv_data,
    feature_families=['sma', 'rsi', 'bollinger_bands']
)

# Create a feature factory with custom parameters
custom_params = {
    'sma': {'windows': [10, 30, 60]},
    'rsi': {'windows': [7, 14]}
}
factory = FeatureFactory(
    ohlcv_data,
    params=custom_params
)
```

## Backtesting Framework

The backtesting framework provides tools to:

1. Generate trade signals based on technical indicator strategies
2. Run a backtest simulation over a specified period
3. Calculate performance metrics
4. Generate human-readable reports

Currently supported strategies:
- **SMA Crossover**: Generate buy signals when a fast SMA crosses above a slow SMA, and sell signals when it crosses below.

Example usage in Python:
```python
from backtester import add_sma_crossover_signals, run_backtest, generate_backtest_report

# Add SMA crossover signals to a DataFrame
data_with_signals = add_sma_crossover_signals(features_df, fast_window=50, slow_window=200)

# Run a backtest simulation
results = run_backtest(data_with_signals, initial_capital=100000)

# Generate a report
generate_backtest_report(results, period_name="Backtest Results")
```

## License

MIT
