# Project Task Breakdown: Technical Analysis PDF Reporting System

## Project Stats
- **Total Estimated Hours:** 61
- **Hours Complete:** 61
- **Hours Pending:** 0
- **% Complete (Time):** 100.00%

## Tasks and Progress

## Project Stats (as of 2025-04-27)
- **Portfolio-Level Backtest & Unified Report Refactor Epic:**
    - Total Estimated Hours: 13h
    - Tasks Completed: 1/15
    - Tasks Remaining: 14
    - % Complete: 7%
- **Last Updated:** 2025-04-27 20:23

---

## Completed Tasks (Portfolio-Level Backtest & Unified Report Refactor)
- [x] Update prd.txt to specify portfolio-level simulation, single report, and rationale requirements (0.5h)
- [x] Summarize rationale for PDF report section (trade rationale aggregation and summary now included in PDF, TDD, minimal code, 2025-04-27)
- [x] Standardized PDF visual style and legends (all charts now use a consistent color palette, section headers use bold Arial font, and legends are always present in both charts and PDF captions. This ensures visual consistency and clarity throughout the report. Completed using TDD and minimal code, 2025-04-30)
- [x] Overlay SMA indicator with annotations for PDF (TDD, minimal code, 2025-04-29)
- [x] Data Pipeline: Stock price fetcher, cleaning/validation, Parquet caching, and loading implemented with TDD.
- [x] Backtesting Engine: SMA crossover and RSI strategies, trade execution/logging, and performance metrics (returns, Sharpe, drawdown, win rate) all TDD-verified.
- [x] Export: Backtest results exported for reporting (JSON).
- [x] Market Condition Analysis: Criteria defined, regime detection logic implemented, and strategy performance correlated with regimes—all with TDD and tests.
- [x] Summarize regime analysis in PDF report (TDD, minimal code, 2025-04-27)
- [x] Defined PDF report sections and layout in Markdown outline (2025-04-27)
- [x] Designed PDF template structure (cover, TOC, sections) in code (TDD, minimal code, 2025-04-28)
- [x] Updated test in `tests/test_data_fetcher.py`:
  - Now fetches data for `HCLTECH.NS` instead of `RELIANCE.NS`.
  - Uses a 20-year period for robust data fetching.
  - Added print statement for DataFrame output in the test.
- [x] Created/updated `tech_analysis/data/fetcher.py` for stock data fetching logic.
- [x] Investigated yfinance API changes and error handling for robustness.
- [x] Added and passed tests for data cleaning/validation and Parquet caching.
- [x] Implemented `clean_and_validate_data` and `cache_to_parquet` functions.
- [x] Added and passed test for loading cached Parquet data.
- [x] Implemented `load_from_parquet` function.
- [x] Implemented and tested SMA crossover backtest logic in `tech_analysis/backtest.py` with TDD in `tests/test_backtest_engine.py`. Test now passes and logic matches pandas idioms.
- [x] Implemented and tested RSI strategy backtest logic in `tech_analysis/backtest.py` with TDD in `tests/test_backtest_engine.py`. Test now passes and logic matches pandas idioms.
- [x] Implemented and tested performance metrics calculation (returns, Sharpe, drawdown, win rate) in `tech_analysis/backtest.py` with TDD in `tests/test_backtest_engine.py`. All metrics verified by test.
- [x] Implemented export_backtest_results in `tech_analysis/backtest.py` to export trade logs and metrics to JSON for PDF report generation (TDD, minimal code).
- [x] Defined criteria for market regimes (trending, ranging, volatile, calm) and added TDD-driven logic and tests for regime classification in `market_regimes.py`.
- [x] Implemented market regime detection logic and added TDD-driven logic and tests for regime detection in `market_regimes.py`.
- [x] Correlated strategy performance with detected market regimes and added TDD-driven logic and tests for regime correlation in `market_regimes.py`.
- [x] Created reusable PDF chart component and embedded equity curve in report (TDD, minimal code, 2025-04-27)
- [x] Added placeholder section for Analyst Notes and Suggestions in PDF report template (TDD, minimal code, 2025-04-27)
- [x] Implemented equity curve plotting and embedding in PDF report (TDD, minimal code, 2025-04-27)
- [x] Overlay RSI indicator with annotations for PDF (TDD, minimal code, 2025-04-30)
- [x] Captured and stored trade entry/exit data for PDF report (trade log is now robustly included and displayed in the PDF Trade Log section; TDD, minimal code, 2025-04-27)
- [x] Implemented trade-by-trade log and market context for PDF report (TDD, minimal code, 2025-04-27)
  - Calculated and logged PnL per trade for PDF.
  - Captured market context (trend, volatility, volume) at each trade for PDF.
  - Formatted trade log for PDF inclusion.
- [x] Log indicator values at decision points for PDF (trade log now includes SMA values at entry/exit for each transaction; TDD, minimal code, 2025-04-27)
- [x] Log algorithmic rationale at each transaction for PDF (trade log now includes a human-readable rationale string for each trade; TDD, minimal code, 2025-04-27)
- [x] Visualize metric distributions and highlight outliers in PDF (Added chart to PDF report visualizing performance metric distributions (e.g., returns) and highlighting outliers in red, with annotation and legend. Implemented using TDD and minimal code in report_generator.py and tests/test_report_generation.py. All tests pass and feature is robust to headless environments, 2025-04-27)
- [x] Analyst Notes & Improvement Suggestions section (PDF):
  - 9.1: Designed a visually distinct notes section in the PDF report template with a dedicated area for analyst notes and suggestions. (TDD, minimal code, 2025-04-27)
  - 9.2: Confirmed section is visible and clearly marked in the PDF. Editable fields not required per user. (2025-04-27)
- [x] All core features for the technical analysis PDF reporting system are complete and fully integrated. The pipeline now:
  - Fetches and cleans data for all stocks in STOCKS_LIST (tech_analysis/data/stocks_list.py)
  - Runs backtest strategies (SMA, RSI) with robust, index-agnostic logic (tech_analysis/backtest.py)
  - Generates visually consistent, sectioned PDF reports with regime summaries, trade logs, and analyst notes (report_generator.py)
  - Orchestrates everything in pipeline.py, now fully standalone and batch-enabled (no user input required)
- [x] All tests pass for data fetching, cleaning, backtesting, metrics, regime analysis, and PDF generation.
- [x] TDD and minimal code principles followed throughout.
- [x] See summary.md for codebase structure and navigation.

---

## Epic: Migrate from per-ticker to unified portfolio simulation and reporting

### 1. PRD & Documentation
- [ ] Update summary.md after implementation to describe new architecture and file responsibilities (0.5h)

### 2. Backtest Logic Refactor
- [ ] Design portfolio state structure (cash, holdings, transaction log, rationale log) (1h)
- [ ] Implement portfolio-level backtest function in tech_analysis/backtest.py: (3h)
    - Accepts all stock data
    - Iterates over time, not per ticker
    - Evaluates buy/hold/sell for all stocks at each step
    - Prefers buy if signal and cash available
    - Allocates position size (configurable)
    - No short selling logic
    - Updates holdings, cash, and logs each trade with rationale
- [ ] Ensure rationale is human-readable and records why a stock was chosen (0.5h)
- [ ] Remove or refactor any per-ticker backtest/report logic (0.5h)

### 3. Report Generation Refactor
- [ ] Update report_generator.py to accept unified trade log and portfolio stats (1h)
- [ ] Generate a single PDF report per run (not per ticker) (1h)
- [ ] Ensure all current report sections (metrics, regime summaries, trade log, rationale, analyst notes) are included and unified (1h)
- [ ] Summarize per-stock contributions in the report (0.5h)

### 4. Pipeline Orchestration
- [ ] Update pipeline.py (or main orchestrator) to: (1h)
    - Call unified backtest
    - Pass results to updated report generator
    - Ensure only one report is produced

### 5. Testing
- [ ] Add/modify tests in tests/test_backtest_engine.py and tests/test_report_generation.py: (2h)
    - Validate only one report is generated
    - Trade log includes trades from multiple tickers
    - Rationale is present and clear for every trade
    - No short selling occurs
    - Buy preference and position sizing logic are enforced

### 6. Validation & Review
- [ ] Manual run to verify one report, correct trade log, and rationale (0.5h)
- [ ] Peer/code review for logic and report completeness (0.5h)

---

_Update task status and hours as you progress. Project stats will update automatically when you recalculate._
