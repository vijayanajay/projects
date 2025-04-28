# Codebase Summary & Navigation Guide

**Purpose:**
This file provides a clear, single-point reference to understand the structure and intent of the codebase. It lists all important files, their key methods/functions, and a concise explanation of what each does and why it exists. This helps any developer, reviewer, or maintainer to quickly locate logic, understand responsibilities, and onboard or debug efficiently. Use this as the first place to look when searching for where a feature or logic is implemented.

---

## File: config.json
**Purpose:** Central configuration file for the backtesting engine. Defines parameters like the data period, initial cash, default position size, the strategy to run, and strategy-specific parameters (e.g., window sizes for SMA, RSI periods). Allows easy modification of backtest settings without changing code.

**Timeframe and Frequency:**
- `start_date`: Start of backtest (YYYY-MM-DD)
- `end_date`: End of backtest (YYYY-MM-DD)
- `frequency`: Data frequency/interval (e.g., '1d', '1h')

---

## Markdown Files in This Project

- `README-task-master.md`: Documentation for Task Master integration or usage.
- `readme.md`: Main project overview, setup, and usage instructions.
- `summary.md`: This codebase summary and navigation guide.
- `tasks.md`: Project task breakdown, progress tracking, and changelog.

---

## File: report_generator.py
**Purpose:** Generates the technical analysis Markdown report, including plots, metrics, regime summaries, trade logs, and now an analyst notes section. The Markdown report includes a cover page, table of contents, and section headers (Performance Metrics, Regime Summary, Strategy Parameters, Trade Log, Analyst Notes) for clarity and professional presentation. All charts use a consistent color palette and legends are always present, with section headers in bold for visual standardization. The trade log section robustly displays trade entry/exit data and PnL for each trade.

### Report Generation
- `generate_markdown_report(stats, bt)`: Generates a detailed technical analysis report as Markdown at `reports/portfolio_report.md`. Includes cover, table of contents, performance metrics, trade log, regime summary, strategy parameters, analyst notes, rationale summary, and embedded charts as images.

### Workflow
- After running the pipeline, the Markdown report is produced in the `reports/` directory.
- Charts are saved in `plots/` and referenced in the Markdown report.

### Test Coverage
- Tests ensure that the Markdown report is generated and contains all key sections (cover, table of contents, metrics, trade log, rationale, etc.).

### Update (2025-04-28): Slippage & Commission Assumptions
- The report_generator.py now programmatically adds an "Assumptions: Slippage and Commission" section to the Markdown report, using the commission value from the backtest engine and stating that no slippage is modeled. This ensures all reports are consistent and up-to-date with respect to transaction cost assumptions. TDD test verifies the section is present in the output.

---

## File: tech_analysis/backtest.py
**Purpose:** Contains all backtesting logic for trading strategies and performance analysis. Parameters like window sizes, initial cash, etc., are typically loaded from `config.json`.

- `sma_crossover_backtest(data, short_window, long_window)`: Simulates a simple moving average crossover strategy, returning a list of buy/sell trades. Core for strategy evaluation.
- `sma_crossover_backtest_with_log(data, short_window, long_window, strategy_params)`: Similar to above, but also returns a detailed trade log (entries, exits, PnL). Each trade log entry now also includes market context: regime (trend/range/volatile/calm, via `classify_market_regime`), volatility (rolling std), volume, and indicator values (short/long SMA at entry/exit) for rationale logging at decision points. Uses `strategy_params` (often from `config.json`) for configuration. Used for deeper analysis and reporting.
- `rsi_strategy_backtest(data, period, overbought, oversold)`: Simulates an RSI-based trading strategy, returning trade signals. Enables testing alternative strategies. Parameters often sourced from `config.json`.
- `calculate_performance_metrics(equity_curve, trade_log)`: Computes total return, win rate, Sharpe ratio, and max drawdown from results. Central for performance reporting and comparison.
- `export_backtest_results(trade_log, metrics, output_path)`: Exports all backtest results to a JSON file for later report generation or audit.
- `correlate_performance_with_regimes(trade_log)`: Groups trade results by detected market regime, summarizing mean PnL and trade count per regime. Supports regime-aware performance analysis.
- `portfolio_backtest(data_dict, initial_cash=10000, position_size=100, strategy_params=None)`: Unified portfolio-level backtest for multiple tickers, time-based iteration, buy preference, no short selling, rationale logging. Accepts a dict of ticker->DataFrame, uses PortfolioState for cash/holdings, and logs each completed trade (with action, qty, entry/exit, PnL, rationale, regime) for robust reporting and test compatibility. Initial cash and position size are now always sourced from the config file, and risk/position sizing logic is documented in the report. Returns the final state, trade log, and an explicit list of all assets traded (as `assets`). (Updated 2025-04-28)

---

## File: tech_analysis/data/fetcher.py
**Purpose:** Handles all data fetching, cleaning, caching, and loading for stock data.

- `fetch_stock_data(ticker, period)`: Downloads historical price data for a single stock from Yahoo Finance. Fundamental for all downstream analysis.
- `fetch_all_stocks_data(period)`: Fetches data for all stocks in the STOCKS_LIST. Automates batch data collection.
- `clean_and_validate_data(df)`: Cleans a DataFrame by filling missing values and capping outliers. Ensures data quality for reliable analysis.
- `cache_to_parquet(df, filename)`: Saves a DataFrame to a Parquet file for fast, persistent storage.
- `load_from_parquet(filename)`: Loads a DataFrame from a Parquet file. Supports efficient data reuse and pipeline speed.

---

## File: tech_analysis/data/stocks_list.py
**Purpose:** Contains a curated list of NSE stock symbols (large/mid-cap) for batch analysis. Used as the universe for data fetching and backtests.

- `STOCKS_LIST`: List of 20 stock symbols. No functions; used by fetchers and orchestrators.

---

## File: tech_analysis/market_regimes.py
**Purpose:** Implements market regime classification logic for price series.

- `classify_market_regime(prices)`: Analyzes a price series and returns a regime label ('trending', 'ranging', 'volatile', 'calm'). Enables regime-aware strategy analysis and reporting.

---

## File: tests/test_backtest_engine.py
**Purpose:** Tests all core backtesting logic and metrics for correctness and robustness.

- `test_sma_crossover_basic()`: Verifies SMA crossover strategy logic and trade signal generation.
- `test_rsi_strategy_basic()`: Validates RSI strategy logic and trade signal generation.
- `test_trade_execution_and_log()`: Checks that trade execution and logging works as expected.
- `test_performance_metrics_calculation()`: Ensures performance metrics are computed correctly.
- `test_export_backtest_results_for_report()`: Tests that backtest results can be exported for reporting.
- `test_correlate_performance_with_regimes()`: Confirms regime-based performance grouping works.

---

## File: tests/test_data_fetcher.py
**Purpose:** Tests all data fetching, cleaning, caching, and loading logic to ensure pipeline reliability.

- `test_fetch_reliance_daily()`: Tests fetching daily data for a specific stock.
- `test_clean_and_validate_data()`: Ensures cleaning logic fills missing values and caps outliers.
- `test_cache_to_parquet()`: Verifies DataFrame caching to Parquet.
- `test_load_from_parquet()`: Verifies loading DataFrame from Parquet.

---

## File: tests/test_market_regimes.py
**Purpose:** Tests market regime classification logic for accuracy and edge cases.

- `test_trending()`, `test_ranging()`, `test_volatile()`, `test_calm()`, `test_noisy_trending()`, `test_noisy_ranging()`, `test_calm_with_outlier()`, `test_long_trending()`: Each tests the regime classifier against different price patterns to ensure robust regime detection.

---

## File: tests/test_report_generation.py
**Purpose:** Tests that Markdown report generation includes all required data and formatting.

- `dummy_bt()`: Provides a mock backtesting object for report tests.
- `test_markdown_contains_regime_summary()`: Checks that the generated Markdown report includes the regime summary, validating the integration of regime analysis into reporting.
- `test_regime_table_filters_short_runs()`: Verifies that the regime table in the Markdown report only includes regime changes that persist for more than 3 days in a row.


**End of summary. Update this file as you add new modules or major features.**