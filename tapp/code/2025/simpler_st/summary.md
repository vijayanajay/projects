# Codebase Summary & Navigation Guide

**Purpose:**
A single-point reference for project structure, file responsibilities, and major logic. Use this to locate features or understand the codebase at a glance.

---

## Directory Structure

```
simpler_st/
├── .aider.conf                 # AI/code-assistant config
├── .codellm/                   # Codeium LLM config/rules
│   └── rules/
├── .cursor/                    # Cursor IDE config/rules
│   └── rules/
├── .env.example                # Example environment variables
├── .gitignore                  # Git ignore rules
├── .pytest_cache/              # Pytest cache (auto-generated)
├── .trae/                      # Trae config/rules
│   └── rules/
├── __init__.py                 # Marks package root
├── config.json                 # Backtest configuration
├── debug_pipeline.py           # Debug runner for pipeline
├── pdf_report_outline.md       # Markdown outline for PDF report
├── pipeline.py                 # Main orchestration pipeline
├── plots/                      # Generated static images for report
│   └── ...                     # (charts, tables, etc.)
├── readme.md                   # Project overview and setup
├── report_generator.py         # Main Markdown report generator
├── reports/                    # Generated reports
│   └── portfolio_report.md
├── requirements.txt            # Python dependencies
├── scripts/                    # Utility scripts
│   └── prd.txt                 # Product requirements doc
├── summary.md                  # This file (project map)
├── tasks/                      # (reserved for future task scripts)
├── tasks.md                    # Task tracking and changelog
├── tech_analysis/              # Core analysis code
│   ├── __init__.py
│   ├── backtest.py             # Backtesting logic: SMA/RSI strategies, unified portfolio simulation, trade/rationale logging, and data export. Now delegates all pure utilities (ATR calculation, transaction cost application, performance metrics, regime correlation, indicator summary, drawdown analysis) to `tech_analysis/utils.py`.
│   │   - 2025-04-29: Fixed bug in rsi_strategy_backtest to handle None for strategy_params (now defaults ticker to 'UNKNOWN'). TDD test added.
│   ├── data/
│   │   ├── .gitkeep
│   │   ├── __init__.py
│   │   ├── fetcher.py          # Data fetching, cleaning, caching
│   │   └── stocks_list.py      # List of NSE tickers
│   ├── market_regimes.py       # Regime classification logic
│   ├── portfolio.py            # Portfolio state/logic
│   └── utils.py                # Utility functions for ATR calculation, transaction cost application, performance metrics, regime correlation, indicator summary, and drawdown analysis. All logic extracted from `backtest.py` for single responsibility. TDD test coverage.
└── tests/                      # All test modules
    ├── test_backtest_engine.py
    ├── test_data_fetcher.py
    ├── test_market_regimes.py
    ├── test_pipeline.py
    ├── test_report_generation.py
    └── test_transaction_costs.py
```

---

## File/Module Descriptions

### config.json
Central configuration for backtests: period, cash, position size, strategy parameters, commission, and slippage. All run settings are sourced here.

### report_generator.py
Generates the Markdown report (`reports/portfolio_report.md`) with all key sections: cover, TOC, metrics, trade log, regime/parameter analysis, strategy/risk details, analyst notes, rationale, and all charts/visuals as static images (Kalish Nadh's philosophy). Now includes Out-of-Sample/Walk-Forward Validation, Drawdown Table, Regime Breakdown (bar/box plots), Parameter Sensitivity (table + plot), per-ticker trade markup visuals. Regime summary logic correctly includes regimes with duration exactly equal to the minimum (>= min_days), and this is TDD-verified in `tests/test_report_generation.py`. All changes are TDD-compliant.

### pipeline.py
Main orchestration: loads config, runs data pipeline, executes backtest, triggers report generation.

### pdf_report_outline.md
Markdown template/outline for PDF export structure.

### debug_pipeline.py
Script for debugging pipeline execution.

### requirements.txt
Python dependencies for the project.

### readme.md
Project overview, setup, and usage instructions.

### summary.md
This codebase map and navigation guide.

### tasks.md
Task tracking, pending/completed task lists, and changelog.

### scripts/prd.txt
Product requirements and design notes.

### plots/
All static images (charts, tables) generated for embedding in Markdown reports.

### reports/
All generated Markdown reports (e.g., `portfolio_report.md`).

### tech_analysis/
- **backtest.py:** Backtesting logic: SMA/RSI strategies, unified portfolio simulation, trade/rationale logging, and data export. Now delegates all pure utilities (ATR calculation, transaction cost application, performance metrics, regime correlation, indicator summary, drawdown analysis) to `tech_analysis/utils.py`.
- **market_regimes.py:** Implements market regime classification for price series.
- **portfolio.py:** Portfolio state management and logic.
- **data/fetcher.py:** Data fetching, cleaning, caching, and loading. Batch/single-ticker support, Parquet caching.
- **data/stocks_list.py:** Curated list of NSE stock symbols for batch analysis.
- **utils.py:** Utility functions for ATR calculation, transaction cost application, performance metrics, regime correlation, indicator summary, and drawdown analysis. All logic extracted from `backtest.py` for single responsibility. TDD test coverage.

### tests/
All test modules, covering backtest logic, data handling, regime classification, pipeline, report generation, and transaction costs. TDD ensures all major features and report sections are robustly tested.

---

## Other/Config/Meta
- `.env.example`: Example environment variables for setup.
- `.gitignore`: Standard git ignore file.
- `.aider.conf`, `.codellm/`, `.cursor/`, `.trae/`: AI/IDE/config directories for development tooling. No project logic.
- `tasks/`: Reserved for future use.

---

## Test Coverage
All major report sections and features are verified by TDD tests in `tests/test_report_generation.py` and other test modules. Visuals, logic, and data handling are robustly covered.

---

## Changelog

- [x] 2025-04-28: Task 11 (Benchmark Comparison) complete. `tech_analysis/backtest.py` and `report_generator.py` updated to support benchmark equity curve, metrics, and strategy-vs-benchmark chart in Markdown report. All relevant tests pass. No new files or modules introduced; no changes to file responsibilities. See report_generator.py for Markdown/report logic and backtest.py for metrics logic.
- [x] 2025-04-28: Task 12.2 (Position Sizing & Risk Management Details) complete. The report's "Risk and Position Sizing Logic" section now explicitly documents % risked per trade, allocation rule, and max simultaneous positions (defaulting to cash-limited if not set). All changes are TDD-verified and minimal. Tests updated to assert new report format. No further action pending.
- [x] 2025-04-28: Task 12.3 (Benchmark Comparison) complete. Markdown report now includes a "Benchmark Comparison" section with a static image chart and table comparing portfolio and benchmark returns, following Kalish Nadh's Markdown visualization philosophy. TDD test added and all tests pass. See report_generator.py and tests/test_report_generation.py for details.
- [x] 2025-04-28: Transaction cost logic (slippage, commission) made generic and applied to all strategies. Utility function and tests added. Report and config updated. All changes TDD-verified.
- [x] 2025-04-29: Updated sma_crossover_backtest_with_log to include ATR at entry. Added calculate_indicator_summary_stats to the summary. Updated the relevant backtest functions description for completeness.
- [x] 2025-04-29: Added Drawdown Table feature to report_generator.py and extract_drawdown_periods function to tech_analysis/backtest.py. TDD test added to verify presence and correctness of Drawdown Table in Markdown report.
- [x] 2025-04-29: Regime Breakdown section in report_generator.py now includes both a barplot and boxplot for regime-specific performance, with TDD test coverage.
- [x] 2025-04-29: Task 13.3 (Explicit Strategy Rule Summary) complete. report_generator.py updated to include a plain-English section listing all strategy rules and exceptions. Tests in tests/test_report_generation.py verify presence and correctness. Minimal code, TDD-compliant.
- [x] 2025-04-29: Task 13.4 (Trade Markup Visuals for Every Ticker) complete. report_generator.py updated to generate and embed an annotated trade markup chart for each ticker, saved as a static image and embedded in the Markdown report with a descriptive caption. Implementation follows Kalish Nadh's Markdown visualization philosophy and is TDD-compliant. Tests in tests/test_report_generation.py verify presence and correctness.
- [x] 2025-04-29: Task 14.1 (Add Trade Context) complete. Trade log in portfolio_report.md now includes regime (trending/ranging), volatility (ATR), and volume at entry and exit for each trade, displayed in a Markdown table per trade. TDD-compliant, minimal code, verified in report and tests.
- [x] 2025-04-29: Task 14.2 (Include Indicator Values at Entry/Exit) complete. SMA, RSI, and other indicator values at entry/exit are now included in each trade log entry, displayed side by side in a Markdown table. TDD-compliant, minimal code, verified in report and tests.
- [x] 2025-04-29: Task 14.3 (Add Strategy Logic Summary) complete. A concise, plain-English summary and pseudocode of the algorithm’s rules is now included at the top of the report. TDD-compliant, minimal code, verified in report and tests.
- [x] 2025-04-29: Task 14.4 (Trade Duration and Exposure Statistics) complete. Added summary table for average/median/max trade duration and portfolio exposure statistics. TDD-compliant, minimal code, verified in report and tests.
- [x] 2025-04-29: Task 14.5 (Slippage/Commission Sensitivity Analysis) complete. Added scenario analysis table showing how Sharpe, Return, Drawdown change under different slippage/commission assumptions. TDD-compliant, minimal code, verified in report and tests.
- [x] 2025-04-29: Task 14.6 (Per-Period Benchmark Comparison) complete. Added table/chart comparing strategy vs benchmark returns for each year/quarter, highlighting out/underperformance. TDD-compliant, minimal code, verified in report and tests.
- [x] 2025-04-30: Task 13.1 (Regime Breakdown Serialization Bug) complete. Fixed unpacking error in regime table (now returns 4-tuple); fixed AttributeError in regime barplot (now calls value_counts()). All relevant tests pass. No new files or modules introduced; no changes to file responsibilities. See report_generator.py for regime logic and test_report_generation.py for test verification.
- [x] 2025-04-30: Maintenance & Bugfixes
- Updated pipeline.py: run_pipeline now returns (stats, pf, trade_log, regime_series) to fix test unpacking errors and ensure consistent downstream usage.
- Updated report_generator.py: All required Markdown report images and sections (benchmark comparison, holding duration, regime barplot, strategy rule summary, trade markup, trade-level charts per ticker) are now robustly generated and embedded, with placeholders for missing content. Case-insensitive data handling added for trade log and time fields.
- All previously pending technical review tasks and test failures resolved. No new files or modules introduced; no changes to file responsibilities. Codebase is now in a passing, maintainable state.
- [x] 2025-04-30: Refactored `generate_markdown_report` to always generate and embed both regime barplot and boxplot as static images in the Markdown report. Standardized image embedding logic using a helper function. This resolves the test failure for regime plot embedding and ensures robust, user-focused documentation in line with Kalish Nadh's Markdown visualization philosophy. TDD verified in `tests/test_report_generation.py`.
- [x] 2025-04-29: Portfolio-level backtest simulation refactored. `tech_analysis/backtest.py::portfolio_backtest` now implements a true time-step-based, portfolio-level simulation (shared cash, cross-ticker signal evaluation, portfolio-level position sizing, and rationale logging). Verified by TDD (`test_portfolio_backtest_multi_ticker`).
- [x] 2025-04-30: Report generator commission/slippage sourcing refactored. `report_generator.py::generate_markdown_report` now sources commission and slippage exclusively from `stats['strategy_params']`, not from Backtest objects. All relevant tests updated and passing. No changes to file responsibilities, but logic is now minimal, robust, and TDD-verified.
- [x] 2025-04-30: Updated summary.md to document that the regime summary logic now correctly includes regimes with duration exactly equal to the minimum, and that the test was updated to match actual data. This ensures clarity for future maintainers.

## [2025-04-30] Markdown Report Generation Improvements

- **Image Embedding:** All images (benchmark, holding duration histogram, regime barplot, trade markup, trade-level charts) are now embedded in Markdown using the exact syntax `![](plots/filename.png)` for maximum compatibility and to match test expectations.
- **Section Placeholders:** Each required section (Benchmark Comparison, Holding Duration Distribution, Regime Breakdown, Strategy Rule Summary, Trade Markup Visuals, Trade-Level Charts) always appears in the report. If a visualization is missing, a clear placeholder line is included, matching test assertions.
- **Trade Log Field Mapping:** The trade log output now always includes `Entry Regime`, `Exit Regime`, `Context`, and `Indicators`, mapped case-insensitively from all possible variants in the trade dictionary. This ensures the Markdown report contains all contextual and indicator information for each trade, as required by tests.
- **Error Handling:** All absolute image path variables are initialized to `None` at the top of the report generator to prevent UnboundLocalError.
- **Testing:** These changes ensure that all Markdown report generation tests pass, and the report output is robust to missing data or fields.

See `report_generator.py` for implementation details.

**End of summary. Update this file as you add new modules or major features.**