# Project Memory: Indian Stock Technical Analysis Tool

## Core Objective
Develop a Python-based tool to fetch historical data for Indian large and mid-cap stocks, backtest a simple trading strategy (initially Simple Moving Average Crossover), and generate a PDF report summarizing the backtest results and performance metrics.

## Key Components
1.  **Data Layer (`pipeline.py`):** Handles fetching data (using `yfinance`) and caching it locally (using Parquet format via `pandas`). Includes basic data validation. Note: Need to handle .NS suffix for NSE listings.
2.  **Backtesting Engine (`backtest.py`):** Implements trading strategies (starting with `SMACrossover`) using the `backtesting.py` library. Runs the backtest simulation.
3.  **Reporting (`report_generator.py`):** Generates a PDF report (using `fpdf2`) containing backtest results, key metrics (Return, Sharpe Ratio, Max Drawdown), and an equity curve plot.
4.  **Main Pipeline (`pipeline.py`):** Orchestrates the workflow, integrating the data, backtesting, and reporting steps.

## Technology Stack
*   **Language:** Python 3.x
*   **Data Fetching:** `yfinance` (with .NS suffix for Indian stocks)
*   **Data Handling:** `pandas`
*   **Data Caching:** Parquet (`pyarrow`)
*   **Backtesting:** `backtesting.py`
*   **Reporting:** `fpdf2`
*   **Plotting:** `bokeh` (via `backtesting.py`), `matplotlib` (potentially for static plots)
*   **Environment:** Virtual Environment (e.g., `venv`)

## Development Notes
*   Start with the defined project structure (`tech_analysis/`, `data/`, `plots/`, `reports/`).
*   Focus on implementing the SMA Crossover strategy first.
*   Ensure modularity between components.
*   Remember to append .NS to ticker symbols for NSE listed stocks.
*   Implement basic error handling and logging as development progresses.
*   Follow plan tasks for incremental development.
*   Keep documentation (docstrings, README, plan) updated.
*   **Prioritize simplicity in code and architecture (inspired by Kalish Nadh's philosophy).**

## Decisions Log
*   *(Empty - To be filled as decisions are made)*

## Open Questions / TODOs
*   Need to create/obtain list of Indian large and mid-cap stock tickers
*   Verify data availability and quality for Indian stocks on yfinance