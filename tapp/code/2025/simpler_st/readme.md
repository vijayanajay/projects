Stock Technical Analysis Tool - 130072f3f2
Here's a step-by-step breakdown of your stock technical analysis system, designed to be
simple yet extensible. I'll structure this as a lightweight Product Requirements Document
(PRD) with implementation guidance.
### 1. System Overview
A minimal Python-based technical analysis pipeline with:
- Data fetching (yfinance)
- Technical indicators (SMA crossover baseline)
- Backtesting (using `backtesting.py` library)
- Report generation (Markdown)
### 2. Core Components
#### 2.1 Data Layer
- **Fetcher**: `yfinance` for OHLCV data (NSE symbols via `.NS` suffix)
- **Cache**: Timestamped Parquet files (1 file per ticker)
- **Validation**: Basic checks for missing data/outliers
#### 2.2 Analysis Layer
- **Indicators**: SMA crossover (default 50/200 day)
- **Signals**: Buy/sell triggers based on crossover logic
#### 2.3 Backtesting
- **Engine**: `backtesting.py` (lightweight library)
- **Metrics**: Sharpe ratio, max drawdown, win rate
#### 2.4 Reporting
- **Format**: Markdown with:
- Equity curve
- Trade statistics
- Indicator visualization
- Decision rationale
### 3. File Structure
```
tech_analysis/
├── pipeline.py # Main workflow
├── backtest.py # Backtesting logic
├── report_generator.py # Report creation
└── data/ # Parquet cache
```
### 4. Implementation Steps
#### Step 1: Data Fetcher (pipeline.py) 
```python
import yfinance as yf
import pandas as pd
from pathlib import Path
from datetime import datetime

def fetch_data(ticker: str, period: str = "2y") -> pd.DataFrame:
    data = yf.download(f"{ticker}.NS", period=period)
    data = data.rename(columns=str.lower)
    return data

def cache_data(data: pd.DataFrame, ticker: str) -> str:
    Path("tech_analysis/data").mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    path = f"tech_analysis/data/{ticker}_{timestamp}.parquet"
    data.to_parquet(path)
    return path
```
#### Step 2: Data Validation (pipeline.py) 
```python
def validate_data(data: pd.DataFrame) -> pd.DataFrame:
    # Drop rows with any NaNs and print summary
    n_before = len(data)
    data_clean = data.dropna()
    n_after = len(data_clean)
    if n_before != n_after:
        print(f"Dropped {n_before - n_after} rows with NaNs.")
    # Optionally, add simple outlier removal here if needed
    return data_clean
```
#### Step 3: Backtesting (backtest.py) 
```python
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
import pandas as pd

def SMA(series, period):
    return series.rolling(window=period).mean()

class SMACrossover(Strategy):
    n1 = 50  # Fast SMA
    n2 = 200  # Slow SMA

    def init(self):
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)

    def next(self):
        if crossover(self.sma1, self.sma2):
            self.buy()
        elif crossover(self.sma2, self.sma1):
            self.sell()

def run_backtest(data: pd.DataFrame):
    bt = Backtest(data, SMACrossover, commission=.002)
    stats = bt.run()
    return stats, bt
```
#### Step 4: Report Generation (report_generator.py) 
- Now includes: equity curve, metrics, strategy parameters, commission, and trade log in Markdown.
- Minimal error handling for report generation.

```python
import matplotlib.pyplot as plt
import os

def generate_report(stats, bt, ticker: str):
    # Ensure plots and reports directories exist
    os.makedirs("plots", exist_ok=True)
    os.makedirs("reports", exist_ok=True)
    # Create plots
    bt.plot(filename=f"plots/{ticker}_equity.png")
    # Markdown Report
    with open(f"reports/{ticker}_report.md", "w") as f:
        f.write(f"# Technical Analysis Report: {ticker}\n")
        f.write("## Equity Curve\n")
        f.write(f"![Equity Curve]({ticker}_equity.png)\n")
        # Add metrics
        metrics = [
            f"Return: {stats['Return [%]']:.2f}%",
            f"Sharpe Ratio: {stats['Sharpe Ratio']:.2f}",
            f"Max Drawdown: {stats['Max. Drawdown [%]']:.2f}%",
            f"Commission: {bt._commission}"
        ]
        for metric in metrics:
            f.write(f"* {metric}\n")
        # Add strategy parameters
        f.write("\n## Strategy Parameters\n")
        params = getattr(bt.strategy, 'parameters', None)
        if params:
            for k, v in params.items():
                f.write(f"* {k}: {v}\n")
        # Add trade log
        f.write("\n## Trade Log\n")
        trades = stats.get('_trades') or stats.get('trades')
        if trades is not None and hasattr(trades, 'iterrows'):
            for idx, trade in trades.iterrows():
                summary = f"Entry: {trade['EntryTime']} @ {trade['EntryPrice']} | Exit: {trade['ExitTime']} @ {trade['ExitPrice']} | PnL: {trade['PnL']:.2f}"
                f.write(f"* {summary}\n")
        else:
            f.write("* No trades.\n")
```
#### Step 5: RSI Indicator & Strategy Extension (backtest.py) 
```python
def RSI(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

class SMARSICrossover(Strategy):
    n1 = 50  # Fast SMA
    n2 = 200  # Slow SMA
    rsi_period = 14
    rsi_overbought = 70
    rsi_oversold = 30

    def init(self):
        self.sma1 = self.I(SMA, self.data.Close, self.n1)
        self.sma2 = self.I(SMA, self.data.Close, self.n2)
        self.rsi = self.I(RSI, self.data.Close, self.rsi_period)

    def next(self):
        if crossover(self.sma1, self.sma2) and self.rsi[-1] < self.rsi_oversold:
            self.buy()
        elif crossover(self.sma2, self.sma1) and self.rsi[-1] > self.rsi_overbought:
            self.sell()
```
#### Step 6: MACD Indicator & Strategy Extension (backtest.py) 
```python
def MACD(series, fast=12, slow=26, signal=9):
    fast_ema = series.ewm(span=fast, adjust=False).mean()
    slow_ema = series.ewm(span=slow, adjust=False).mean()
    macd_line = fast_ema - slow_ema
    signal_line = macd_line.ewm(span=signal, adjust=False).mean()
    return macd_line, signal_line

class MACDCrossover(Strategy):
    fast = 12
    slow = 26
    signal = 9

    def init(self):
        self.macd, self.signal = MACD(self.data.Close, self.fast, self.slow, self.signal)

    def next(self):
        # Buy when MACD crosses above signal, sell when below
        if self.macd[-2] < self.signal[-2] and self.macd[-1] > self.signal[-1]:
            self.buy()
        elif self.macd[-2] > self.signal[-2] and self.macd[-1] < self.signal[-1]:
            self.sell()
```
### 5. Execution Flow
1. Fetch data → cache as Parquet
2. Load cached data → run backtest
3. Generate report with visualizations (Markdown)
### 6. Suggested Extensions
- Add more indicators (RSI, MACD) 
- Parameter optimization
- Live trading integration
- Sentiment analysis inputs
### 7. Dependencies
```python
# requirements.txt
yfinance==0.2.31
pandas==2.0.3
pyarrow==14.0.1
backtesting==0.3.3
matplotlib==3.7.2
