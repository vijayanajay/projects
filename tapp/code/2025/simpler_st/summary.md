# Codebase Summary & Navigation Guide

## Project Completion

All core modules and features for the technical analysis PDF reporting system are complete as of 2025-04-27. The pipeline is now fully automated and batch-enabled: it fetches, cleans, backtests, and generates PDF reports for every stock in STOCKS_LIST with no user input required. All code follows TDD and minimal code principles. See tasks.md for a detailed completed tasks summary.

**Portfolio-Level Refactor in Progress (2025-04-27):**
- PRD updated to require a single portfolio-level backtest and unified PDF report (not per-ticker)
- See tasks.md for granular breakdown of pending and completed work

**PortfolioState class added (2025-04-27):**
- New `PortfolioState` class in `tech_analysis/portfolio.py` manages cash, holdings, and transaction log for unified portfolio-level backtest.
- See tasks.md for TDD and implementation details.

**Portfolio-Level Refactor (2025-04-27)**
- The codebase now performs unified portfolio-level backtesting and generates a single PDF report (portfolio_report.pdf) for all tickers in STOCKS_LIST.
- All per-ticker report generation logic has been removed or refactored.
- The pipeline fetches and cleans data for all tickers, runs portfolio_backtest, and passes results to generate_report.
- generate_report now takes aggregated stats and outputs a unified report; no ticker argument is required.
- Defensive filtering in the pipeline skips invalid tickers (e.g., '', '.', None).
- All related tests have been updated and pass, confirming TDD compliance.

**Bugfix (2025-04-27):**
- Fixed root cause of empty/zero reports: pipeline.py now computes and passes real portfolio stats, equity curve, and trade log to generate_report, ensuring the PDF report reflects actual backtest results and trades.

**Config-Driven Pipeline (2025-04-27):**
- Added config.json to centralize all key parameters (data period, strategy, cash, position size, etc.).
- pipeline.py now loads config.json and uses its values for all runs.
- Data fetch period defaults to 10 years for robust backtesting (was previously 1 year, which caused empty/flat results).
- Debug logging for data quality and parameter visibility added to pipeline.py.
- All features and tests remain TDD-compliant and minimal code.

**Recent Changes (2025-04-27)**
- Added `generate_markdown_report(stats, bt)` in `report_generator.py` to produce a Markdown report (`reports/portfolio_report.md`) with the same content and structure as the PDF report.
- Updated the pipeline to call both `generate_report` (PDF) and `generate_markdown_report` (Markdown) automatically after each run.
- Added a test in `tests/test_report_generation.py` to verify Markdown report generation and content (cover, table of contents, metrics, trade log, rationale, etc.).
- Updated `scripts/prd.txt` to reflect dual report output.
- All documentation and workflow now reflect the dual-report system for technical analysis reporting.

**Purpose:**
This file provides a clear, single-point reference to understand the structure and intent of the codebase. It lists all important files, their key methods/functions, and a concise explanation of what each does and why it exists. This helps any developer, reviewer, or maintainer to quickly locate logic, understand responsibilities, and onboard or debug efficiently. Use this as the first place to look when searching for where a feature or logic is implemented.

---

## Markdown Files in This Project

- `README-task-master.md`: Documentation for Task Master integration or usage.
- `pdf_report_outline.md`: The outline and structure for the PDF report template (design document).
- `readme.md`: Main project overview, setup, and usage instructions.
- `summary.md`: This codebase summary and navigation guide.
- `tasks.md`: Project task breakdown, progress tracking, and changelog.

---

## File: report_generator.py
**Purpose:** Generates the technical analysis PDF report, including plots, metrics, regime summaries, trade logs, and now an analyst notes section. Creates a structured PDF template with a cover page, table of contents, and section headers (Performance Metrics, Regime Summary, Strategy Parameters, Trade Log, Analyst Notes) for clarity and professional presentation. All charts use a consistent color palette and legends are always present, with section headers in bold Arial font for visual standardization (since 2025-04-30). The trade log section robustly displays trade entry/exit data and PnL for each trade (since 2025-04-27).

### Report Generation
- `generate_report(stats, bt)`: Generates a detailed technical analysis report as a PDF at `reports/portfolio_report.pdf`. Includes cover, table of contents, performance metrics, trade log, regime summary, strategy parameters, analyst notes, rationale summary, and embedded charts.
- `generate_markdown_report(stats, bt)`: Generates the same report in Markdown format at `reports/portfolio_report.md`. All sections and charts are included as Markdown, with image links for charts. Called automatically in the pipeline after PDF generation.

### Workflow
- After running the pipeline, both PDF and Markdown reports are produced in the `reports/` directory.
- Charts are saved in `plots/` and referenced in both reports.

### Test Coverage
- Tests ensure that both PDF and Markdown reports are generated and contain all key sections (cover, table of contents, metrics, trade log, rationale, etc.).

- `reusable_chart_component(pdf, image_path, x=10, y=None, w=190)`: Embeds a reusable chart image (such as an equity curve) into the PDF at the specified position and width. This function abstracts chart/image embedding for reuse across report sections, supporting the creation of modular PDF components. Always adds a legend caption below the chart for clarity.

---

## File: tech_analysis/backtest.py
**Purpose:** Contains all backtesting logic for trading strategies and performance analysis.

- `sma_crossover_backtest(data, short_window, long_window)`: Simulates a simple moving average crossover strategy, returning a list of buy/sell trades. Core for strategy evaluation.
- `sma_crossover_backtest_with_log(data, short_window, long_window)`: Similar to above, but also returns a detailed trade log (entries, exits, PnL). **As of 2025-04-27, each trade log entry now also includes market context: regime (trend/range/volatile/calm, via `classify_market_regime`), volatility (rolling std), volume, and indicator values (short/long SMA at entry/exit) for rationale logging at decision points.** Used for deeper analysis and reporting.
- `rsi_strategy_backtest(data, period, overbought, oversold)`: Simulates an RSI-based trading strategy, returning trade signals. Enables testing alternative strategies.
- `calculate_performance_metrics(equity_curve, trade_log)`: Computes total return, win rate, Sharpe ratio, and max drawdown from results. Central for performance reporting and comparison.
- `export_backtest_results(trade_log, metrics, output_path)`: Exports all backtest results to a JSON file for later report generation or audit.
- `correlate_performance_with_regimes(trade_log)`: Groups trade results by detected market regime, summarizing mean PnL and trade count per regime. Supports regime-aware performance analysis.
- `portfolio_backtest(data_dict, initial_cash=10000, position_size=100)`: Unified portfolio-level backtest for multiple tickers, time-based iteration, buy preference, no short selling, rationale logging. Accepts a dict of ticker->DataFrame, uses PortfolioState for cash/holdings, logs each trade with rationale, and returns the final state and trade log. (Added 2025-04-27)

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
**Purpose:** Tests that PDF report generation includes all required data and formatting.

- `dummy_bt()`: Provides a mock backtesting object for report tests.
- `test_pdf_contains_regime_summary()`: Checks that the generated PDF report includes the regime summary, validating the integration of regime analysis into reporting.

---

**End of summary. Update this file as you add new modules or major features.**
