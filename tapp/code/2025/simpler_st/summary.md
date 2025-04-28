# Codebase Summary & Navigation Guide

**Purpose:**
A single-point reference for project structure, file responsibilities, and major logic. Use this to locate features or understand the codebase at a glance.

---

## config.json
Central configuration for backtests: period, cash, position size, strategy parameters, commission, and slippage. All run settings are sourced here.

---

## Markdown Files
- `README-task-master.md`: Task Master integration/usage.
- `readme.md`: Project overview, setup, usage.
- `summary.md`: Codebase map (this file).
- `tasks.md`: Task tracking and changelog.

---

## report_generator.py
Generates the Markdown report (`reports/portfolio_report.md`) with all key sections: cover, TOC, metrics, trade log, regime/parameter analysis, strategy/risk details, analyst notes, rationale, and all charts/visuals as static images (Kalish Nadh's philosophy). Now includes Out-of-Sample/Walk-Forward Validation, Drawdown Table, Regime Breakdown (with bar/box plots), Parameter Sensitivity (table + plot), and per-ticker trade markup visuals. All changes are TDD-compliant and tested in `tests/test_report_generation.py`.

---

## tech_analysis/backtest.py
All backtesting logic: SMA/RSI strategies, unified portfolio simulation, trade/rationale logging, performance metrics, regime detection, parameter sensitivity, and transaction cost handling. All trade logs and metrics are net of costs. Utility functions for drawdown, indicator stats, and exporting results. Test coverage for all features.

---

## tech_analysis/data/fetcher.py
Handles fetching, cleaning, caching, and loading of stock data. Batch and single-ticker support, robust validation, and Parquet caching for performance.

---

## tech_analysis/data/stocks_list.py
Curated list of NSE stock symbols for analysis and batch backtesting.

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

**End of summary. Update this file as you add new modules or major features.**