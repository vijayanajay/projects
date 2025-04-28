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
│   ├── backtest.py             # Backtesting, metrics, rationale
│   ├── data/
│   │   ├── .gitkeep
│   │   ├── __init__.py
│   │   ├── fetcher.py          # Data fetching, cleaning, caching
│   │   └── stocks_list.py      # List of NSE tickers
│   ├── market_regimes.py       # Regime classification logic
│   └── portfolio.py            # Portfolio state/logic
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
Generates the Markdown report (`reports/portfolio_report.md`) with all key sections: cover, TOC, metrics, trade log, regime/parameter analysis, strategy/risk details, analyst notes, rationale, and all charts/visuals as static images (Kalish Nadh's philosophy). Now includes Out-of-Sample/Walk-Forward Validation, Drawdown Table, Regime Breakdown (bar/box plots), Parameter Sensitivity (table + plot), per-ticker trade markup visuals. TDD-compliant and tested in `tests/test_report_generation.py`.

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
- **backtest.py:** All backtesting logic: SMA/RSI strategies, unified portfolio simulation, trade/rationale logging, performance metrics, regime detection, parameter sensitivity, transaction cost handling. Utility functions for drawdown, indicator stats, exporting results. All trade logs and metrics are net of costs. TDD test coverage.
- **market_regimes.py:** Implements market regime classification for price series.
- **portfolio.py:** Portfolio state management and logic.
- **data/fetcher.py:** Data fetching, cleaning, caching, and loading. Batch/single-ticker support, Parquet caching.
- **data/stocks_list.py:** Curated list of NSE stock symbols for batch analysis.

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

**End of summary. Update this file as you add new modules or major features.**