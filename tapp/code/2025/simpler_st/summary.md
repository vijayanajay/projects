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

**Update:**
- Now includes `commission` and `slippage` fields at both the root and within `strategy_params` for flexible transaction cost modeling.

---

## Markdown Files in This Project

- `README-task-master.md`: Documentation for Task Master integration or usage.
- `readme.md`: Main project overview, setup, and usage instructions.
- `summary.md`: This codebase summary and navigation guide.
- `tasks.md`: Project task breakdown, progress tracking, and changelog.

---

## File: report_generator.py
**Purpose:** Generates the technical analysis Markdown report, including plots, metrics, regime summaries, trade logs, and analyst notes.

**Update:**
- The "Assumptions: Slippage and Commission" section now reports the actual values used and clarifies their effect on trade execution and net results.
- All reported PnL and metrics are net of costs.
- **(2025-04-28):** Trade-level annotated charts are now generated and embedded for each ticker, with regime overlays and SMA crossover annotations. Charts are saved as static images and referenced in the Markdown report, following Kalish Nadh's Markdown visualization philosophy. TDD test verifies chart presence for all tickers. See tests/test_report_generation.py for test logic.
- **(2025-04-29):** Now generates and embeds a Drawdown Table section as a static image of all drawdown periods (start, trough, end, depth, recovery) in the Markdown report. Table is produced as drawdown_table.png and follows Kalish Nadh's Markdown visualization philosophy. TDD test verifies presence and correctness. See tech_analysis/backtest.py and tests/test_report_generation.py for details.
- **(2025-04-29):** Regime Breakdown section now includes both a barplot (mean PnL per regime) and a boxplot (PnL distribution per regime), embedded as static images in the Markdown report. All regime-specific performance metrics are summarized in a table and visualized, following Kalish Nadh's Markdown visualization philosophy. TDD test verifies both plots are present. See tests/test_report_generation.py.
- **(2025-04-29):** Parameter Sensitivity Analysis section now always included if parameter sweep results or plot are present. If results are provided, a Markdown table summarizing parameter sets and their metrics is generated and embedded, in addition to the static image. Fully TDD-compliant and minimal code. See tests/test_report_generation.py.

### Report Generation
- `generate_markdown_report(stats, bt, parameter_sensitivity_results=None)`: Generates a detailed technical analysis report as Markdown at `reports/portfolio_report.md`. Includes cover, table of contents, performance metrics, trade log, regime summary, strategy parameters, analyst notes, rationale summary, and embedded charts as images. Now generates and embeds a trade-level chart for each ticker, with regime overlays and SMA crossover annotations (2025-04-28). Now also embeds a parameter sensitivity table and plot if available (2025-04-29).
- `plot_parameter_sensitivity(eq1, eq2, label1, label2, save_path="plots/parameter_sensitivity.png")`: Plots and saves a static image comparing equity curves for two different parameter sets, used for sensitivity/robustness analysis. (Added 2025-04-28)

### Workflow
- After running the pipeline, the Markdown report is produced in the `reports/` directory.
- Charts are saved in `plots/` and referenced in the Markdown report.

### Test Coverage
- Tests ensure that the Markdown report is generated and contains all key sections (cover, table of contents, metrics, trade log, rationale, etc.).
- Test added to verify that the report includes a 'Parameter Sensitivity Analysis' section, table, and the correct plot if generated. (2025-04-29)

---

## File: tech_analysis/backtest.py
**Purpose:** Contains all backtesting logic for trading strategies and performance analysis. Parameters like window sizes, initial cash, etc., are typically loaded from `config.json`.

- `sma_crossover_backtest(data, short_window, long_window)`: Simulates a simple moving average crossover strategy, returning a list of buy/sell trades. Core for strategy evaluation.
- `sma_crossover_backtest_with_log(data, short_window, long_window, strategy_params)`: Similar to above, but also returns a detailed trade log (entries, exits, PnL). Each trade log entry now also includes market context: regime (trend/range/volatile/calm, via `classify_market_regime`), volatility (rolling std), volume, ATR at entry, and indicator values (short/long SMA at entry/exit) for rationale logging at decision points. Uses `strategy_params` (often from `config.json`) for configuration. Used for deeper analysis and reporting.
- `rsi_strategy_backtest(data, period, overbought, oversold)`: Simulates an RSI-based trading strategy, returning trade signals. Enables testing alternative strategies. Parameters often sourced from `config.json`.
- `calculate_performance_metrics(equity_curve, trade_log)`: Computes total return, win rate, Sharpe ratio, and max drawdown from results. Central for performance reporting and comparison.
- `extract_drawdown_periods(equity_curve)`: Extracts all drawdown periods from the equity curve, returning a list of dicts (start, trough, end, depth, recovery). Used for reporting and Drawdown Table (added 2025-04-29).
- `export_backtest_results(trade_log, metrics, output_path)`: Exports all backtest results to a JSON file for later report generation or audit.
- `correlate_performance_with_regimes(trade_log)`: Groups trade results by detected market regime, summarizing mean PnL and trade count per regime. Supports regime-aware performance analysis.
  - Updated (2025-04-28): Now expects trade_log as a list of dicts, not a DataFrame. All callers must convert DataFrames using .to_dict('records') before passing. This ensures robust handling and avoids iteration errors. TDD test coverage in tests/test_report_generation.py.
- `portfolio_backtest(data_dict, initial_cash=10000, position_size=100, strategy_params=None)`: Unified portfolio-level backtest for multiple tickers, time-based iteration, buy preference, no short selling, rationale logging. Accepts a dict of ticker->DataFrame, uses PortfolioState for cash/holdings, and logs each completed trade (with action, qty, entry/exit, PnL, rationale, regime) for robust reporting and test compatibility. Initial cash and position size are now always sourced from the config file, and risk/position sizing logic is documented in the report. Returns the final state, trade log, and an explicit list of all assets traded (as `assets`). (Updated 2025-04-28)

### Transaction Cost Utility
- `apply_transaction_costs(entry_price, exit_price, commission, slippage)`: Adjusts entry/exit prices for slippage, deducts commission, and returns net PnL. Used by all strategies.

### Backtest Functions
- `sma_crossover_backtest_with_log(...)`: Now applies costs using the utility. Trade logs include net PnL, commission cost, slippage-adjusted prices, ATR at entry, and volume at entry.
- `rsi_strategy_backtest(...)`: Now accepts `strategy_params` and applies transaction costs via the utility. Trade logs reflect all costs.
- `portfolio_backtest(...)`: Trade execution and logging use the same utility for cost handling.

### Indicator Summary Stats
- `calculate_indicator_summary_stats(trade_log)`: Computes mean, min, and max for ATR and volume at entry across all trades. Supports summary reporting of additional indicators. (Added 2025-04-29)

---

## Transaction Costs (Generic Handling)
**Update 2025-04-28:**
- All backtest strategies (SMA, RSI, portfolio, etc.) now apply slippage and commission using a generic utility function `apply_transaction_costs(entry_price, exit_price, commission, slippage)` in `tech_analysis/backtest.py`.
- This ensures that every trade, regardless of strategy, is cost-aware and net PnL is always reported after transaction costs.
- Commission and slippage parameters are configurable in `config.json` (both at root and in `strategy_params`).

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
- `test_drawdown_table()`: Verifies that the Markdown report includes a Drawdown Table section with the correct data. (Added 2025-04-29)

---

## File: tests/test_transaction_costs.py
**Purpose:** Dedicated tests for transaction cost logic.
- Unit tests for the utility function ensure correct adjustment of prices and PnL.
- Integration tests for SMA and RSI strategies verify that costs are always applied and reflected in trade logs.

---

## Changelog

- [x] 2025-04-28: Task 11 (Benchmark Comparison) complete. `tech_analysis/backtest.py` and `report_generator.py` updated to support benchmark equity curve, metrics, and strategy-vs-benchmark chart in Markdown report. All relevant tests pass. No new files or modules introduced; no changes to file responsibilities. See report_generator.py for Markdown/report logic and backtest.py for metrics logic.
- [x] 2025-04-28: Task 12.2 (Position Sizing & Risk Management Details) complete. The report's "Risk and Position Sizing Logic" section now explicitly documents % risked per trade, allocation rule, and max simultaneous positions (defaulting to cash-limited if not set). All changes are TDD-verified and minimal. Tests updated to assert new report format. No further action pending.
- [x] 2025-04-28: Task 12.3 (Benchmark Comparison) complete. Markdown report now includes a "Benchmark Comparison" section with a static image chart and table comparing portfolio and benchmark returns, following Kalish Nadh's Markdown visualization philosophy. TDD test added and all tests pass. See report_generator.py and tests/test_report_generation.py for details.
- [x] 2025-04-28: Transaction cost logic (slippage, commission) made generic and applied to all strategies. Utility function and tests added. Report and config updated. All changes TDD-verified.
- [x] 2025-04-29: Updated sma_crossover_backtest_with_log to include ATR at entry. Added calculate_indicator_summary_stats to the summary. Updated the relevant backtest functions description for completeness.
- [x] 2025-04-29: Added Drawdown Table feature to report_generator.py and extract_drawdown_periods function to tech_analysis/backtest.py. TDD test added to verify presence and correctness of Drawdown Table in Markdown report.
- [x] 2025-04-29: Regime Breakdown section in report_generator.py now includes both a barplot and boxplot for regime-specific performance, with TDD test coverage.

**End of summary. Update this file as you add new modules or major features.**