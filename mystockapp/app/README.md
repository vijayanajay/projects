# Stock Technical Indicator Generator, Backtester, and Trading Dashboard

This project downloads historical stock data from Yahoo Finance, generates comprehensive technical indicators using a configurable `FeatureFactory`, provides a framework for backtesting trading strategies, and includes an interactive dashboard for visualizing and analyzing results.

## Features

- Download historical stock data for any ticker using yfinance (maximum available period)
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
- Visualization of key indicators with dynamic column detection
- Realistic backtesting framework for trading strategies with:
  - Proper split of data to avoid look-ahead bias
  - Transaction costs (fixed and percentage-based commissions)
  - Slippage modeling
  - Position sizing
  - In-sample and out-of-sample testing
  - Performance metrics (total return, win rate, max drawdown, transaction costs, etc.)
  - Strategy signal visualization
  - Comparison reporting between periods
- Multiple trading strategies:
  - SMA Crossover Strategy
  - RSI Overbought/Oversold Strategy
- Interactive web dashboard (Streamlit) for:
  - Stock data visualization
  - Technical indicator display
  - Strategy backtesting
  - Performance analysis
- Multi-stock scanner for identifying trading opportunities
- Unified launcher for all components

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

### Interactive Dashboard

The easiest way to use the app is through the interactive dashboard:

```bash
python run.py --mode dashboard
```

This launches a Streamlit web application where you can:
- Enter any stock ticker symbol
- Select technical indicators to display
- Configure and run backtests
- Visualize results and performance metrics

### Stock Scanner

To scan multiple stocks for trading signals:

```bash
python run.py --mode scanner
```

The scanner allows you to:
- Enter a list of stock symbols to scan
- Select which strategy to use for scanning
- Configure strategy parameters
- View buy and sell signals across multiple stocks

### Command-Line Usage

Run the main script to download stock data and generate technical indicators:

```bash
python run.py --mode backtest --backtest-args "--ticker AAPL --period 1y --plot"
```

Or use directly:

```bash
python main.py --ticker AAPL --period 1y --plot
```

This will:
1. Download the specified historical data for the given ticker
2. Generate all technical indicators
3. Save the results to `data/stock_features.csv`

### Command-line Options

```
python main.py [OPTIONS]
```

Available options:
- `--ticker`: Stock ticker symbol (default: 'RELIANCE.NS')
  - Examples: 'AAPL', 'MSFT', 'RELIANCE.NS' (for NSE), 'RELIANCE.BO' (for BSE)
- `--period`: Data period (default: 'max')
  - Valid values: '1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'
- `--interval`: Data interval (default: '1d')
  - Valid values: '1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo'
- `--output`: Output CSV file path (default: 'data/stock_features.csv')
- `--plot`: Generate plots of key indicators
- `--features`: Comma-separated list of feature families to generate (default: 'all')
  - Valid values: 'sma', 'ema', 'rsi', 'macd', 'bollinger_bands', 'atr', 'volume'
  - Example: `--features sma,rsi,macd`
- `--no-cache`: Disable data caching
- `--drop-na-threshold`: Control NaN handling in the dataset (number or fraction)
  - If < 1: Drop rows with more than this fraction of columns containing NaN values
  - If >= 1: Drop rows with more than this number of columns containing NaN values
  - If not provided (default): Drop any row containing any NaN values

### Backtesting Options

- `--split-date`: Date to split data into in-sample and out-of-sample periods (YYYY-MM-DD format)
- `--initial-capital`: Initial capital for backtesting (default: 100000.0)
- `--strategy`: Trading strategy to backtest (default: 'sma_crossover')
  - Valid values: 'sma_crossover', 'rsi'

#### SMA Crossover Strategy Parameters
- `--fast-sma`: Fast SMA window size for crossover strategy (default: 50)
- `--slow-sma`: Slow SMA window size for crossover strategy (default: 200)

#### RSI Strategy Parameters
- `--rsi-window`: RSI window size for RSI strategy (default: 14)
- `--rsi-oversold`: RSI oversold threshold for buy signals (default: 30)
- `--rsi-overbought`: RSI overbought threshold for sell signals (default: 70)

### Transaction Cost and Position Sizing Options

- `--commission-fixed`: Fixed commission per trade in currency units (default: 20.0)
- `--commission-pct`: Percentage commission per trade as decimal (default: 0.0003 = 0.03%)
- `--slippage-pct`: Slippage as percentage of price (default: 0.001 = 0.1%)
- `--position-size-pct`: Percentage of available capital to use per trade (default: 0.25 = 25%)

### Configuration File

Instead of specifying all parameters via command line, you can use a YAML configuration file:

```bash
python main.py --config config_sample.yaml
```

See `config_sample.yaml` for a complete example with all available options. The configuration file allows fine-grained control over all aspects of data fetching, indicator parameters, backtesting options, and output settings.

Benefits of using a configuration file:
- Store and reuse complex parameter sets
- Configure specific indicator parameters (e.g., custom SMA windows, RSI periods)
- Run multiple experiments by maintaining different configuration files
- Keep command line simple while having full control over all parameters

### Examples

Generate only Moving Averages and RSI indicators:
```bash
python main.py --features sma,ema,rsi
```

Download data for the last 5 years with weekly intervals and generate plots:
```bash
python main.py --ticker AAPL --period 5y --interval 1wk --plot
```

Save output to a custom location:
```bash
python main.py --output results/apple_indicators.csv
```

Run a backtest with SMA crossover strategy (50 and 200 periods) using 2019-01-01 as the split date:
```bash
python main.py --ticker MSFT --period max --interval 1d --split-date 2019-01-01 --initial-capital 100000 --strategy sma_crossover --plot
```

Run a backtest with RSI strategy:
```bash
python main.py --ticker AAPL --period 2y --interval 1d --strategy rsi --rsi-window 14 --rsi-oversold 30 --rsi-overbought 70 --plot
```

Backtest with custom parameters and realistic transaction costs:
```bash
python main.py --ticker AMZN --split-date 2019-01-01 --fast-sma 20 --slow-sma 100 --commission-fixed 25 --commission-pct 0.0005 --slippage-pct 0.002 --position-size-pct 0.2 --plot
```

## Project Structure

- `run.py`: Unified launcher for all components
- `main.py`: Main script for command-line operation
- `app.py`: Interactive dashboard application (Streamlit)
- `scanner.py`: Stock scanner application (Streamlit)
- `src/`:
  - `data_fetcher.py`: Module for fetching historical stock data using yfinance
  - `feature_factory.py`: Implementation of the `FeatureFactory` component
  - `backtester.py`: Implementation of the backtesting framework and strategies
- `data/`: Directory for cached data and output files
- `plots/`: Directory for generated plots (when using `--plot` option)
- `tests/`: Directory for test files

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
from src.feature_factory import FeatureFactory

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
2. Run a backtest simulation over a specified period with realistic trading conditions:
   - Transaction costs (fixed fee plus percentage)
   - Slippage modeling
   - Position sizing (partial position allocation)
3. Calculate comprehensive performance metrics
4. Generate human-readable reports

Supported strategies:

### SMA Crossover Strategy
Generates buy signals when a fast SMA crosses above a slow SMA, and sell signals when it crosses below.

```python
from src.backtester import SMACrossoverStrategy, run_backtest

# Create the strategy
strategy = SMACrossoverStrategy(fast_window=50, slow_window=200)

# Generate signals
data_with_signals = strategy.generate_signals(features_df)

# Run a backtest simulation
results = run_backtest(
    data_with_signals,
    initial_capital=100000,
    commission_fixed=20.0,
    commission_pct=0.0003,
    slippage_pct=0.001,
    position_size_pct=0.25
)
```

### RSI Strategy
Generates buy signals when RSI crosses above an oversold threshold, and sell signals when it crosses below an overbought threshold.

```python
from src.backtester import RSIStrategy, run_backtest

# Create the strategy
strategy = RSIStrategy(rsi_window=14, oversold_threshold=30, overbought_threshold=70)

# Generate signals
data_with_signals = strategy.generate_signals(features_df)

# Run a backtest simulation
results = run_backtest(
    data_with_signals,
    initial_capital=100000,
    commission_fixed=20.0,
    commission_pct=0.0003,
    slippage_pct=0.001,
    position_size_pct=0.25
)
```

## Important Implementation Notes

### Avoiding Look-Ahead Bias

The system properly splits data before calculating technical indicators to prevent look-ahead bias. This ensures that:

1. Data is split into in-sample and out-of-sample periods based on the specified date
2. Technical indicators are calculated separately for each period
3. Only historical data available up to each point in time is used in indicator calculations

### Realistic Backtesting

The backtesting framework includes:

1. Transaction costs modeling:
   - Fixed commission per trade
   - Percentage-based commission
   - Maximum commission caps

2. Slippage modeling:
   - Buy orders execute at a slightly higher price than close
   - Sell orders execute at a slightly lower price than close

3. Position sizing:
   - Use a configurable percentage of available capital per trade
   - Prevents unrealistic "all-in/all-out" trading

4. Detailed performance metrics:
   - Transaction cost impact analysis
   - Slippage impact analysis
   - Realistic win rate calculation accounting for costs
   - Enhanced equity curves and comparison plots

## License

MIT
