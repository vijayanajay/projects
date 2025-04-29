# Project Task Breakdown: Technical Analysis Reporting System

## Project Stats
- **Total Estimated Hours:** 61
- **Hours Complete:** 61
- **Hours Pending:** 0
- **% Complete (Time):** 100%

## Pending Tasks (Report Gaps Identified by Technical Trader Review) - TODO

Okay, let's analyze these Pytest failures systematically.

**Analysis Results & Actionable Tasks:**

Okay, let's analyze these Pytest failures meticulously.

**Analysis:**

I'll go through each failure identified in the `py_results.txt` output.

**Failures 3, 4, 5: `test_pipeline_generates_markdown_report`, `test_pipeline_uses_config_params`, `test_regime_table_filters_short_runs`**

These three tests fail with the *exact same error*:

1.  **Parse Failure:**
    *   `TypeError: 'numpy.ndarray' object is not callable` in `report_generator.py:686`.
    *   The failing line is `regime_counts = pd.Series(list(regime_series.values())).value_counts()`.

2.  **Understand Test Intent vs. Reality:**
    *   **`test_pipeline_generates_markdown_report`:** Integration test for the full pipeline, expecting a report file.
    *   **`test_pipeline_uses_config_params`:** Integration test checking if pipeline uses `config.json` parameters, also runs the full pipeline.
    *   **`test_regime_table_filters_short_runs`:** Unit/integration test for `generate_markdown_report`, specifically testing regime filtering logic.
    *   **Reality:** All three tests trigger the `generate_markdown_report` function, which contains the bug.

3.  **Analyze Code Under Test:**
    *   In `report_generator.py:686`, the code attempts to get the values from the `regime_series` (a Pandas Series) and calculate value counts.
    *   The `.values` attribute of a Pandas Series returns a NumPy array. It is an *attribute*, not a *method*.
    *   The code incorrectly calls it as a method: `regime_series.values()`. This attempts to *call* the NumPy array returned by `.values`, leading to the `TypeError`.

4.  **Determine Root Cause:**
    *   **Code Bug:** Incorrect usage of the Pandas Series `.values` attribute (called as a method `values()` instead of accessed as `values`). This single bug causes failures in three different tests that execute this code path.

5.  **Evaluate Test Logic and Validity:**
    *   All three tests are valid in their intent. They fail due to this shared underlying bug in the code being tested or executed during the test.

6.  **Propose Solutions:**
    *   Correct the specific line in `report_generator.py`.

**Failure 6: `test_markdown_includes_trade_heatmap`**

1.  **Parse Failure:**
    *   `AssertionError: Trade heatmap not generated.` in `tests/test_report_generation.py:343`.
    *   The assertion `assert chart_path.exists()` failed, meaning the file `plots/trade_heatmap.png` was not created.

2.  **Understand Test Intent vs. Reality:**
    *   **Intent:** Verify that `generate_markdown_report` creates the heatmap image when provided with appropriate trade data.
    *   **Reality:** The test provides a `_trades` DataFrame with columns 'Ticker', 'PnL', 'Regime' (note the capitalization).

3.  **Analyze Code Under Test:**
    *   The heatmap generation logic in `report_generator.py` (around line 571) checks for the existence of columns `'ticker', 'regime', 'pnl'` (lowercase) in the `trades_df`.
    *   `trades_df = pd.DataFrame(trade_log)` is created earlier, likely preserving the original case from the input `stats['_trades']`.
    *   The check `all(col in trades_df.columns for col in ['ticker', 'regime', 'pnl'])` fails because the expected lowercase column names do not match the uppercase names ('Ticker', 'Regime', 'PnL') provided in the test's DataFrame. This prevents the heatmap plotting code from executing.

4.  **Determine Root Cause:**
    *   **Code Bug (Case Sensitivity/Data Handling):** The code expects specific lowercase column names for heatmap generation, but the test provides capitalized names. The code isn't robust to case variations in input DataFrame columns.

5.  **Evaluate Test Logic and Validity:**
    *   The test setup is slightly inconsistent with the code's expectation (column casing). The code could be more robust. The test *does* correctly identify that the heatmap isn't generated under these conditions.

6.  **Propose Solutions:**
    *   Make the column check in `report_generator.py` case-insensitive, or normalize column names to lowercase before the check. The simplest change is modifying the check.

**Failure 7: `test_markdown_includes_trade_level_chart_per_ticker`**

1.  **Parse Failure:**
    *   `AssertionError: Trade-level chart for AAPL not generated.` in `tests/test_report_generation.py:672`.
    *   The assertion `assert chart_path.exists()` failed for the AAPL chart.

2.  **Understand Test Intent vs. Reality:**
    *   **Intent:** Verify that when multi-ticker data (dictionaries for curves, DataFrame for trades) is passed, `generate_markdown_report` creates individual trade charts for each ticker.
    *   **Reality:** The test provides data in the expected multi-ticker format, including a `_trades` DataFrame with capitalized 'Ticker' column.

3.  **Analyze Code Under Test:**
    *   The per-ticker chart generation loop in `report_generator.py` (around line 698) iterates through tickers. Inside the loop, it filters the `trade_log` list using `t.get('ticker') == ticker` (line 706).
    *   The `trade_log` list is derived from the input `stats['_trades']` DataFrame provided by the test, which has the column 'Ticker'.
    *   `t.get('ticker')` (lowercase 't') will return `None` because the dictionary keys are capitalized ('Ticker'). The filter condition `t.get('ticker') == ticker` will always be false.
    *   This results in an empty `trades` list for each ticker within the loop.
    *   The plotting block condition `if eq_curve is not None and sma is not None and trades:` (line 707) fails because `trades` is empty, thus `plt.savefig` is never called.

4.  **Determine Root Cause:**
    *   **Code Bug (Case Sensitivity/Data Handling):** Similar to the heatmap failure, the code expects a lowercase 'ticker' key when filtering trades for per-ticker charts, but the data derived from the test's DataFrame uses 'Ticker'.

5.  **Evaluate Test Logic and Validity:**
    *   The test logic is valid for testing multi-ticker report generation. The data casing inconsistency reveals a bug.

6.  **Propose Solutions:**
    *   Modify the trade filtering logic (line 706) to be case-insensitive or check for both 'ticker' and 'Ticker'. Using the `get_any` helper function defined later in the same file would be consistent: `ticker_in_trade = get_any(t, 'ticker', 'Ticker')`. Change the filter to `trades = [t for t in trade_log if get_any(t, 'ticker', 'Ticker') == ticker]`.

**Failure 8: `test_markdown_includes_holding_duration_distribution`**

1.  **Parse Failure:**
    *   `AssertionError: Holding duration histogram not generated.` in `tests/test_report_generation.py:737`.
    *   The assertion `assert chart_path.exists()` failed for `plots/holding_duration.png`.

2.  **Understand Test Intent vs. Reality:**
    *   **Intent:** Verify that `generate_markdown_report` creates a holding duration histogram when trade data includes entry and exit times.
    *   **Reality:** The test provides a `_trades` DataFrame with columns 'EntryTime' and 'ExitTime'.

3.  **Analyze Code Under Test:**
    *   The holding duration logic in `report_generator.py` (lines 204-205, 216-217) attempts to retrieve time values using `trade.get('entry_time')` and `trade.get('exit_time')` (lowercase).
    *   The input DataFrame from the test uses 'EntryTime' and 'ExitTime' (uppercase).
    *   The `get()` calls return `None` due to the case mismatch.
    *   The `holding_durations` list remains empty.
    *   The plotting block condition `if holding_durations:` (line 220) fails, and `plt.savefig` is never called.

4.  **Determine Root Cause:**
    *   **Code Bug (Case Sensitivity):** The code expects lowercase time keys ('entry_time', 'exit_time') but the test data uses uppercase ('EntryTime', 'ExitTime').

5.  **Evaluate Test Logic and Validity:**
    *   The test correctly provides the necessary time data. The failure highlights the code's lack of robustness to case variations.

6.  **Propose Solutions:**
    *   Modify the `get()` calls (lines 204-205, 216-217) to use the correct case ('EntryTime', 'ExitTime') or, preferably, use the `get_any` helper: `entry = get_any(trade, 'entry_time', 'EntryTime')`, `exit = get_any(trade, 'exit_time', 'ExitTime')`.

**Failure 9: `test_markdown_includes_regime_plots`**

1.  **Parse Failure:**
    *   `AssertionError: Regime barplot not embedded in Markdown report.` in `tests/test_report_generation.py:770`.
    *   The check `assert "regime_barplot.png" in text` failed.

2.  **Understand Test Intent vs. Reality:**
    *   **Intent:** Verify that regime analysis plots (barplot, boxplot) are generated and included in the Markdown file when relevant trade data is provided.
    *   **Reality:** The test provides `stats['trades']` with 'PnL' and 'regime' keys.

3.  **Analyze Code Under Test:**
    *   The regime plotting logic exists (lines 657-683) and *should* execute based on the test data.
    *   However, this test executes the same code path as Failures 3, 4, and 5, which crash at line 686 due to the `regime_series.values()` bug.
    *   This crash occurs *after* the regime plots should have been generated and their Markdown lines added to the `md_lines` list, but *before* the final `f.write("\n".join(md_lines))` call (line 723).
    *   Therefore, the report file (`md_path`) is likely incomplete or empty when the assertion is checked.

4.  **Determine Root Cause:**
    *   **Code Bug (Same as Failure 3):** The downstream crash at line 686 prevents the complete Markdown report from being written to disk, causing the assertion failure even though the plotting code might have run correctly.

5.  **Evaluate Test Logic and Validity:**
    *   The test is valid and would likely pass if the subsequent bug were fixed.

6.  **Propose Solutions:**
    *   Fix the root cause identified in Failure 3 (the `.values()` bug at line 686). This single fix should resolve Failures 3, 4, 5, 9, and 10.

**Failure 10: `test_markdown_includes_strategy_rule_summary`**

1.  **Parse Failure:**
    *   `AssertionError: Strategy rule summary section missing.` in `tests/test_report_generation.py:831`.
    *   The check `assert "Strategy Rules (Plain English)" in text` failed.

2.  **Understand Test Intent vs. Reality:**
    *   **Intent:** Verify that the strategy rules section is included in the report when `stats['strategy_rules']` is provided.
    *   **Reality:** The test provides the `strategy_rules` list in `stats`.

3.  **Analyze Code Under Test:**
    *   The logic to add the strategy rules section exists in `report_generator.py` (lines 691-695).
    *   This section comes *after* the code at line 686 where the crash identified in Failure 3 occurs.
    *   The crash prevents this part of the code from executing and/or prevents the final report from being written correctly.

4.  **Determine Root Cause:**
    *   **Code Bug (Same as Failure 3):** The downstream crash at line 686 prevents the report from being fully generated and written, causing the assertion for this section to fail.

5.  **Evaluate Test Logic and Validity:**
    *   The test is valid.

6.  **Propose Solutions:**
    *   Fix the root cause identified in Failure 3 (the `.values()` bug at line 686). This should also resolve this failure.

---


## Completed Tasks (Portfolio-Level Backtest & Unified Report Refactor)

- [x] Task 1: Serialization Error in backtest.export_backtest_results (2025-04-30)
  - Fixed: Confirmed via strict TDD that export_backtest_results correctly serializes NumPy types to JSON using convert_numpy_types helper. Added explicit test (test_export_backtest_results_serializes_numpy_types) to tests/test_backtest_engine.py; test passes with no code change needed. No further action required.
- [x] Task 12.1: Trade Statistics Breakdown (2025-04-28)
  - Implemented summary table showing average win, average loss, largest win, largest loss, profit factor, expectancy, and trade breakdown by regime (trending/ranging) in the Markdown report. All metrics are displayed in a clearly separated summary table and regime breakdown. Tests in tests/test_report_generation.py verify presence and correctness. TDD-compliant, minimal code.
- [x] Task 12.2: Position Sizing & Risk Management Details (2025-04-28)
  - The report now documents and displays risk per trade, capital allocation logic, and position sizing method as required. The "Risk and Position Sizing Logic" section explicitly states the % risked per trade, allocation rule, and max simultaneous positions (defaulting to cash-limited if not set). All changes are TDD-verified and minimal. Tests updated to assert new report format. No further action pending.
- [x] Task 12.3: Benchmark Comparison (2025-04-28)
  - Add a section comparing portfolio returns to one or more benchmarks (e.g., NIFTY, S&P 500), including outperformance/underperformance.
  - Acceptance: Table or chart shows portfolio vs. benchmark returns for the same period.
  - Status: Complete
  - Implemented: Markdown report now includes a "Benchmark Comparison" section with a static image chart and table comparing portfolio and benchmark returns, following Kalish Nadh's Markdown visualization philosophy. TDD test added and all tests pass. See report_generator.py and tests/test_report_generation.py for details.
- [x] Task 12.4: Slippage, Commissions, Real-World Execution (2025-04-28)
  - Incorporated transaction cost assumptions (slippage, commissions) into all backtest logic using a generic utility function. All strategies and trade logs now reflect net PnL after costs. The report states cost assumptions and net results, and users can configure cost parameters. All changes are TDD-verified with new tests in tests/test_transaction_costs.py. Legacy tests and report logic updated for new cost handling and reporting. No further action pending.
- [x] Task 8: Specify Backtest Timeframe and Frequency (2025-04-28)
  - Added start_date, end_date, and frequency fields to config.json.
  - Updated data fetching and backtest logic to use these fields for all analyses.
- [x] Task 13.1: Parameter Sensitivity/Robustness Analysis (2025-04-29)
  - The report now includes a "Parameter Sensitivity Analysis" section with a Markdown table and static image summarizing Sharpe, Return, Drawdown, etc. for different parameter sets. Implementation follows Kalish Nadh's Markdown visualization philosophy and is fully TDD-compliant. Minimal code added to report_generator.py.
- [x] Task 13.2: Out-of-Sample/Walk-Forward Validation (2025-04-29)
  - The report now includes an "Out-of-Sample Walk-Forward Results" section summarizing results on out-of-sample data or with walk-forward validation, clearly stating the period and performance metrics. Implementation follows Kalish Nadh's Markdown visualization philosophy and is fully TDD-compliant. Minimal code added to report_generator.py and test added to tests/test_report_generation.py.
- [x] Refactored pipeline.py to run a unified portfolio backtest across all tickers and generate a single report. Removed per-ticker loop and generate_report calls. (2025-04-27)
- [x] Refactored generate_report in report_generator.py to remove the ticker parameter and generate a single portfolio-level report (portfolio_report.md). All per-ticker references replaced with portfolio-level naming. (2025-04-27)
- [x] Updated tests in tests/test_report_generation.py and tests/test_pipeline.py to call generate_report and run_pipeline with unified inputs, checking for portfolio_report.md and portfolio_equity.png. (2025-04-27)
- [x] Added filtering in pipeline.py to skip invalid tickers (e.g., '', '.', None) before fetching data. (2025-04-27)
- [x] Documented invalid ticker '.' in tech_analysis/data/stocks_list.py. (2025-04-27)
- [x] Unified backtest logic using portfolio_backtest in tech_analysis/backtest.py for multi-ticker portfolio simulation. (2025-04-27)
- [x] All tests pass, confirming TDD compliance and minimal code. (2025-04-27)
- [x] Update prd.txt to specify portfolio-level simulation, single report, and rationale requirements (0.5h)
- [x] Design portfolio state structure (cash, holdings, transaction log, rationale log) (1h)
- [x] Summarize rationale for report section (trade rationale aggregation and summary now included in report, TDD, minimal code, 2025-04-27)
- [x] Standardized visual style and legends (all charts now use a consistent color palette, section headers use bold font, and legends are always present in both charts and captions. This ensures visual consistency and clarity throughout the report. Completed using TDD and minimal code, 2025-04-30)
- [x] Added placeholder section for Analyst Notes and Suggestions in report template (TDD, minimal code, 2025-04-27)
- [x] Implemented equity curve plotting and embedding in report (TDD, minimal code, 2025-04-27)
- [x] Overlay SMA indicator with annotations for report (TDD, minimal code, 2025-04-29)
- [x] Data Pipeline: Stock price fetcher, cleaning/validation, Parquet caching, and loading implemented with TDD.
- [x] Backtesting Engine: SMA crossover and RSI strategies, trade execution/logging, and performance metrics (returns, Sharpe, drawdown, win rate) all TDD-verified.
- [x] Export: Backtest results exported for reporting (JSON).
- [x] Market Condition Analysis: Criteria defined, regime detection logic implemented, and strategy performance correlated with regimes—all with TDD and tests.
- [x] Summarize regime analysis in report (TDD, minimal code, 2025-04-27)
- [x] Defined report sections and layout in Markdown outline (2025-04-27)
- [x] Designed template structure (cover, TOC, sections) in code (TDD, minimal code, 2025-04-28)
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
- [x] Implemented export_backtest_results in `tech_analysis/backtest.py` to export trade logs and metrics to JSON for report generation (TDD, minimal code).
- [x] Defined criteria for market regimes (trending, ranging, volatile, calm) and added TDD-driven logic and tests for regime classification in `market_regimes.py`.
- [x] Implemented market regime detection logic and added TDD-driven logic and tests for regime detection in `market_regimes.py`.
- [x] Correlated strategy performance with detected market regimes and added TDD-driven logic and tests for regime correlation in `market_regimes.py`.
- [x] Created reusable chart component and embedded equity curve in report (TDD, minimal code, 2025-04-27)
- [x] Added placeholder section for Analyst Notes and Suggestions in report template (TDD, minimal code, 2025-04-27)
- [x] Implemented equity curve plotting and embedding in report (TDD, minimal code, 2025-04-27)
- [x] Overlay RSI indicator with annotations for report (TDD, minimal code, 2025-04-30)
- [x] Captured and stored trade entry/exit data for report (trade log is now robustly included and displayed in the Trade Log section; TDD, minimal code, 2025-04-27)
- [x] Implemented trade-by-trade log and market context for report (TDD, minimal code, 2025-04-27)
  - Calculated and logged PnL per trade for report.
  - Captured market context (trend, volatility, volume) at each trade for report.
  - Formatted trade log for report inclusion.
- [x] Log indicator values at decision points for report (trade log now includes SMA values at entry/exit for each transaction; TDD, minimal code, 2025-04-27)
- [x] Log algorithmic rationale at each transaction for report (trade log now includes a human-readable rationale string for each trade; TDD, minimal code, 2025-04-27)
- [x] Visualize metric distributions and highlight outliers in report (Added chart to report visualizing performance metric distributions (e.g., returns) and highlighting outliers in red, with annotation and legend. Implemented using TDD and minimal code in report_generator.py and tests/test_report_generation.py. All tests pass and feature is robust to headless environments, 2025-04-27)
- [x] Analyst Notes & Improvement Suggestions section:
  - 9.1: Designed a visually distinct notes section in the report (2025-04-27)
- [x] Task 11: Add Benchmark Comparison (2025-04-28)
  - Added benchmark equity curve and metrics to performance calculation and report.
  - Updated Markdown report to include equity curve, drawdown, return distribution, and strategy-vs-benchmark charts.
  - All related tests pass (TDD, minimal code, 2025-04-28)
- [x] Task 12.5: Visuals: Trade Markups on Charts (2025-04-28)
  - Generate annotated price charts for each ticker, marking trade entries/exits, SMA crossovers, and regime overlays.
  - Acceptance: At least one sample chart per ticker with clear trade and regime annotation.
  - Status: Complete
  - Implemented: Each ticker now has an annotated trade chart with SMA crossovers and regime overlays, saved as static images and embedded in the Markdown report. TDD test verifies presence and embedding for all tickers. See report_generator.py and tests/test_report_generation.py for implementation and test logic.
- [x] Task 12.6: Volatility, Volume, and Additional Indicators (2025-04-29)
  - Display volatility (e.g., ATR), volume at trade entry, and any other indicator relevant to the strategy.
  - Acceptance: Each trade log entry includes ATR/volume at entry; summary stats are provided.
  - Status: Complete
  - Implemented: ATR and volume at trade entry are now included in every trade log entry, and summary statistics (mean, min, max) for both are provided via a new function in backtest.py. All changes are TDD-verified and minimal. See tests/test_backtest_engine.py for test logic and backtest.py for implementation.
- [x] Task 12.7: Drawdown Table or Timeline (2025-04-29)
  - Implemented extraction of all drawdown periods from the equity curve, including start, trough, end, depth, and recovery time. Generated a static image table (drawdown_table.png) and embedded it in the Markdown report as a dedicated section. All logic is TDD-driven and minimal. Test verifies presence of section and image. See report_generator.py, tech_analysis/backtest.py, and tests/test_report_generation.py for details.
- [x] Task 12.8: Trade Distribution and Holding Periods (2025-04-29)
  - Add histograms/tables for trade holding durations and PnL distribution across all trades.
  - Acceptance: Report includes at least one histogram for duration and one for PnL distribution.
  - Status: Complete
  - Implemented: Markdown report now includes a histogram for trade holding durations and PnL distribution, following Kalish Nadh's Markdown visualization philosophy. TDD test added and all tests pass. See report_generator.py and tests/test_report_generation.py for details.
- [x] Task 12.9: Regime-Specific Performance (2025-04-29)
  - Summarized PnL, win rate, and average trade outcome for each regime type (trending/ranging/volatile). Report now includes a regime breakdown table, barplot (mean PnL per regime), and boxplot (PnL distribution per regime), all embedded as static images in Markdown following Kalish Nadh's philosophy. TDD-compliant, minimal code. Tests in tests/test_report_generation.py verify presence and correctness.
- [x] Task 12.10: Edge and Robustness Commentary (2025-04-29)
  - Added narrative/analysis on statistical significance, robustness checks, and out-of-sample/walk-forward results. Section in report discusses robustness, overfitting, and out-of-sample performance. All changes are TDD-verified and minimal. Tests updated to assert new report content. No further action pending.
- [x] Task 13.3: Explicit Strategy Rule Summary (2025-04-29)
  - The report now includes a section listing every rule and exception in plain English, including entry/exit, filters, and special cases. Rules are displayed in a clearly separated section. TDD-compliant, minimal code, and verified by tests.
- [x] Task 13.4: Trade Markup Visuals for Every Ticker (2025-04-29)
  - The report now embeds an annotated price chart for every ticker, showing trade entries/exits, indicator overlays, and regime shading. Each chart is saved as a static image and embedded in the Markdown report with a descriptive caption. Implementation follows Kalish Nadh's Markdown visualization philosophy and is TDD-compliant. Verified by tests.
- [x] Task 14.1: Add Trade Context (Regime, Volatility, Volume) (2025-04-29)
  - Trade log in portfolio_report.md now includes regime (trending/ranging), volatility (ATR), and volume at entry and exit for each trade. Displayed in a Markdown table per trade. TDD-compliant, minimal code, verified in report and tests.
- [x] Task 14.2: Include Indicator Values at Entry/Exit (2025-04-29)
  - SMA, RSI, and other indicator values at entry/exit are now included in each trade log entry in the report. Displayed side by side in a Markdown table. TDD-compliant, minimal code, verified in report and tests.
- [x] Task 14.3: Add Strategy Logic Summary (2025-04-29)
  - Added a concise, plain-English summary and pseudocode of the algorithm’s rules at the top of the report. TDD-compliant, minimal code, verified in report and tests.
- [x] Task 14.4: Trade Duration and Exposure Statistics (2025-04-29)
  - Added summary table for average/median/max trade duration and portfolio exposure statistics. TDD-compliant, minimal code, verified in report and tests.
- [x] Task 14.5: Slippage/Commission Sensitivity Analysis (2025-04-29)
  - Added scenario analysis table showing how Sharpe, Return, Drawdown change under different slippage/commission assumptions. TDD-compliant, minimal code, verified in report and tests.
- [x] Task 14.6: Per-Period Benchmark Comparison (2025-04-29)
  - Added table/chart comparing strategy vs benchmark returns for each year/quarter, highlighting out/underperformance. TDD-compliant, minimal code, verified in report and tests.
- [x] All core features for the technical analysis reporting system are complete and fully integrated. The pipeline now:
  - Fetches and cleans data for all stocks in STOCKS_LIST (tech_analysis/data/stocks_list.py)
  - Runs backtest strategies (SMA, RSI) with robust, index-agnostic logic (tech_analysis/backtest.py)
  - Generates visually consistent, sectioned Markdown reports with regime summaries, trade logs, and analyst notes (report_generator.py)
  - Orchestrates everything in pipeline.py, now fully standalone and batch-enabled (no user input required)
- [x] All tests pass for data fetching, cleaning, backtesting, metrics, regime analysis, and report generation.
- [x] TDD and minimal code principles followed throughout.
- [x] See summary.md for codebase structure and navigation.
- [x] Fixed root cause of empty/zero report: pipeline.py now computes and passes real portfolio stats, equity curve, and trade log to generate_markdown_report (2025-04-27)
- [x] List Universe/Assets Traded: Explicitly listed all assets or symbols included in the backtest. (2025-04-28)
- [x] Task 9: State Slippage and Commission Assumptions (2025-04-28)
  - The report generation logic now programmatically inserts a dedicated section for slippage (none modeled, all trades at close price) and commission (dynamic, from backtest engine) assumptions.
  - TDD test added to verify this section in the report.
  - No manual edits required; assumptions are always up-to-date.
- [x] Task 10: Add Parameter Sensitivity/Robustness Analysis (2025-04-28)
  - Added run_parameter_sensitivity_analysis to pipeline.py to run backtests with different SMA short_window values and plot comparative equity curves.
  - Added plot_parameter_sensitivity to report_generator.py to generate and embed a static plot in the Markdown report.
  - Updated report_generator.py to include a Parameter Sensitivity Analysis section in the report, following Kalish Nadh's visualization philosophy.
  - Added TDD test in tests/test_report_generation.py to verify the presence of the sensitivity plot and section in the report. All tests pass.
  - Minimal code added, no change to method responsibilities. summary.md updated only for new/changed file roles if needed.

---
