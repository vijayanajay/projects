**Architectural Audit Report**

**Date:** 2025-05-17
**Auditor:** AI Language Model
**Codebase Path:** D:/Code/projects/mystockapp/app/
**Documentation Path:** D:/Code/projects/mystockapp/app/ (README.md, docs/)
**`arch_review.md` Path:** D:/Code/projects/mystockapp/app/docs/arch_review.md
**`technical_debt.md` Path:** D:/Code/projects/mystockapp/app/docs/technical_debt.md

**Part 1: Audit of Prior Architectural Mandates & Identification of New Critical Flaws**

**A. Compliance Audit of `arch_review.md` Directives:**

**-- AUDIT OF PRIOR DIRECTIVE --**
**Directive Reference (from arch_review.md):** Potential Data Inconsistency (Split Date Handling)
**Current Status:** PARTIALLY RESOLVED
**Evidence & Justification for Status:**
    The mandated solution required using a validated, timezone-aware `pd.Timestamp` for data splitting in `main.py` and ensuring consistent timezone handling between `data.index` and the `split_date_ts`.
    *   **`main.py`, lines 630-634:** `split_date_ts` is correctly created as a `pd.Timestamp` from `args.split_date` and localized to 'UTC' if naive. This `split_date_ts` is then used for splitting data (lines 639, 646). This part of the mandate is RESOLVED.
    *   **Outstanding Issue:** The mandate also specified: "Ensure `data.index` is also timezone-aware or comparison is handled correctly. If `data.index.tzinfo` is None and `split_date_ts` is not None: Option 1: Localize `data.index` (e.g., to UTC, if appropriate). Option 2: Compare naive (if `split_date_ts` was also made naive, but aware is better)." This explicit handling of potential timezone mismatch between `data.index` (from `get_stock_data`) and the UTC-aware `split_date_ts` is **NOT implemented** in `main.py` before the split occurs at lines 639 and 646. If `data.index` is naive, comparing it with a timezone-aware `split_date_ts` will raise a `TypeError` in pandas.
**Required Action (If Not Fully Resolved/Regressed):**
    The original proposed solution for timezone consistency remains valid. Implement timezone handling for `data.index` before splitting in `main.py`:
    ```python
    # In main.py, before line 639 (data splitting)
    # After data = get_stock_data(...) and after split_date_ts is defined

    if data is not None and not data.empty and split_date_ts is not None:
        if data.index.tzinfo is None:
            logger.warning(f"Data index for {args.ticker} is timezone-naive. Localizing to UTC for comparison with split_date.")
            try:
                data.index = data.index.tz_localize('UTC')
            except Exception as e: # Handle cases like AmbiguousTimeError during DST transitions if not 'B' freq
                logger.error(f"Failed to localize data.index to UTC: {e}. Proceeding with naive index if yfinance returned it as such, but comparison with aware split_date might fail.")
                # Potentially make split_date_ts naive for comparison if data.index cannot be localized,
                # though this is less ideal:
                # split_date_ts = split_date_ts.tz_localize(None)
        elif data.index.tzinfo != split_date_ts.tzinfo:
            logger.warning(f"Data index timezone ({data.index.tzinfo}) differs from split_date timezone ({split_date_ts.tzinfo}). Converting data index to UTC.")
            data.index = data.index.tz_convert('UTC')

    # ... then proceed with splitting ...
    in_sample_data_raw = (
        data[data.index < split_date_ts].copy()
        if split_date_ts and data is not None and not data.empty # Add checks for data
        else data.copy() if data is not None else pd.DataFrame() # Handle data being None
    )
    out_of_sample_data_raw = (
        data[data.index >= split_date_ts].copy()
        if split_date_ts and data is not None and not data.empty
        else pd.DataFrame().reindex_like(data).iloc[0:0] if data is not None and not data.empty else pd.DataFrame()
    )
    ```
    This ensures that `data.index` is timezone-aware (preferably UTC) before comparison with the UTC-aware `split_date_ts`, preventing `TypeError`.

**B. New Critical Architectural Flaws:**

**-- NEW CRITICAL ARCHITECTURAL FLAW --**
**Category:** Critical Logic Failure (Uninitialized Variable in Backtester)
**Location:** `src/backtester.py`, `run_backtest` function, around line 408.
**Description:** The `trades` list is appended to within the buy signal logic (`trades.append(...)` at line 408) but is never initialized (e.g., `trades = []`) at the beginning of the `run_backtest` function. Other lists like `open_positions`, `portfolio_values`, and `completed_trades` are initialized (lines 366-368).
**Consequences:** If a buy signal is encountered and the code attempts to append to `trades`, a `NameError` will be raised because `trades` is not defined. This will cause the entire backtest to crash, preventing any results from being generated if buy signals exist.
**Justification for Criticality:** This is a fundamental bug that breaks the core backtesting functionality under common conditions (i.e., when a buy signal occurs).
**Root Cause Analysis:** Oversight in variable initialization within the `run_backtest` function.
**Mandated Solution:**
    *   **Immediate Corrective Action:** Initialize `trades` as an empty list at the beginning of the `run_backtest` function in `src/backtester.py`.
        ```python
        # In src/backtester.py, run_backtest function, around line 368
        completed_trades = []
        trades = [] # Add this line
        total_commission = 0
        ```
    *   **Verification Protocol:**
        1.  Write a unit test for `run_backtest` with a simple DataFrame that includes at least one buy signal.
        2.  Ensure the backtest completes without a `NameError`.
        3.  Verify that `results['trades']` is populated correctly.
**Systemic Prevention Mandate:** Enhance static analysis (linters like Pylint, Flake8) to more aggressively detect uninitialized variables. Code reviews must explicitly check for initialization of all variables that are appended to or modified in loops/conditional blocks.

**-- NEW CRITICAL ARCHITECTURAL FLAW --**
**Category:** Critical Data Integrity / UI Bug (Mismatched DataFrame Indexing in Dashboard)
**Location:** `app.py` (main dashboard file, not the snippet), lines 363 and 379-380.
**Description:**
    1.  `portfolio_series` (line 363): `portfolio_series = pd.Series(results["portfolio_values"], index=features_df.index)`. The `results["portfolio_values"]` are generated by `run_backtest` based on `features_with_signals` (passed at line 302). If `features_with_signals` has a different length or index than `features_df` (e.g., due to NaN dropping in `strategy.generate_signals` or if `features_df` was not re-assigned after potential modifications), this will lead to a `ValueError` due to mismatched lengths or misaligned plotting of the equity curve.
    2.  `buy_points` / `sell_points` (lines 379-380): `buy_points = features_df[features_df["buy_signal"] == True]`. Signals (`buy_signal`, `sell_signal`) are generated on `features_with_signals`, not necessarily on the original `features_df`. This will lead to incorrect or missing buy/sell markers on the equity plot.
**Consequences:** The portfolio equity curve may fail to render, render incorrectly, or be misaligned with trade signals. Buy/sell markers on the plot will be incorrect or missing. This severely impacts the usability and correctness of the dashboard's primary backtest visualization.
**Justification for Criticality:** This breaks core visualization features of the dashboard, rendering performance analysis misleading or impossible.
**Root Cause Analysis:** Using an older/unmodified DataFrame (`features_df`) for indexing and signal plotting instead of the DataFrame that was actually used for the backtest (`features_with_signals`).
**Mandated Solution:**
    *   **Immediate Corrective Action:** Modify `app.py` to consistently use the DataFrame that was fed into `run_backtest` (i.e., `features_with_signals`) for creating `portfolio_series` and for identifying `buy_points` and `sell_points`.
        ```python
        # In app.py, after features_with_signals is defined and before run_backtest
        # Ensure features_with_signals is the final version of data used for backtesting.
        # If any NaN dropping happens after strategy.generate_signals, it should be on features_with_signals.
        # For example, if a general dropna is needed:
        # features_with_signals = features_with_signals.dropna() # if not already handled robustly

        # ... (results = run_backtest(features_with_signals, ...)) ...

        # Line 363:
        portfolio_series = pd.Series(
            results["portfolio_values"], index=features_with_signals.index # USE features_with_signals.index
        )

        # Lines 379-380:
        buy_points = features_with_signals[features_with_signals["buy_signal"] == True] # USE features_with_signals
        sell_points = features_with_signals[features_with_signals["sell_signal"] == True] # USE features_with_signals

        # Ensure buy_points.index and sell_points.index are valid for portfolio_series.loc[]
        # This should be fine if portfolio_series is indexed by features_with_signals.index
        equity_fig.add_trace(
            go.Scatter(
                x=buy_points.index,
                y=portfolio_series.loc[buy_points.index], # Ensure buy_points.index exists in portfolio_series
                # ...
            )
        )
        equity_fig.add_trace(
            go.Scatter(
                x=sell_points.index,
                y=portfolio_series.loc[sell_points.index], # Ensure sell_points.index exists in portfolio_series
                # ...
            )
        )
        ```
        *Note: The `app/app.py` snippet provided in the prompt appears to contain these fixes. The main `app.py` file needs to be updated to match this corrected logic.*
    *   **Verification Protocol:**
        1.  Run a scenario in `app.py` where `features_df` (after `FeatureFactory`) would have NaNs at the beginning (due to indicator lookback) but `features_with_signals` (after `strategy.generate_signals` and potential internal NaN handling or if `dropna()` is applied before `run_backtest`) has fewer rows.
        2.  Verify the equity curve plots correctly without errors.
        3.  Verify buy/sell signals appear at the correct dates on the equity curve, corresponding to the signals in `features_with_signals`.
**Systemic Prevention Mandate:** Maintain a clear "source of truth" DataFrame throughout the processing pipeline for backtesting and plotting. Ensure that any DataFrame modifications (like NaN dropping or signal addition) result in the updated DataFrame being used consistently in subsequent steps. Consider passing DataFrames explicitly or using a state management object that clearly tracks the current version of the data.

**-- NEW CRITICAL ARCHITECTURAL FLAW --**
**Category:** Critical Initialization Error (Misconfiguration of Streamlit Cache TTL)
**Location:** `src/data_fetcher.py`, line 20, the `@st.cache_data` decorator.
**Description:** The Streamlit cache decorator is used as `@st.cache_data(ttl=timedelta(days=cache_expiry_days))`. The `cache_expiry_days` variable is a parameter of the `fetch_stock_data` function itself. Decorator arguments are evaluated at function definition time, not at call time. At the time `fetch_stock_data` is defined, `cache_expiry_days` (as a parameter) is not in the accessible scope for the decorator. This will lead to a `NameError` when `data_fetcher.py` is imported, or when Streamlit tries to register the cached function.
**Consequences:** The application may fail to start or the data fetching caching mechanism provided by Streamlit will not work as intended, potentially crashing. This impacts a core data retrieval and caching feature.
**Justification for Criticality:** This flaw can prevent the application from running or cause data fetching to be unreliably cached by Streamlit, affecting performance and stability.
**Root Cause Analysis:** Misunderstanding of decorator argument scope and evaluation time. Function parameters are not available to the decorator at definition time.
**Mandated Solution:**
    *   **Immediate Corrective Action:** Set a fixed TTL for `st.cache_data` or remove the `ttl` argument if dynamic TTL based on function parameters is not directly supported by `st.cache_data` in this manner. The file-based caching already uses the `cache_expiry_days` parameter correctly.
        Option 1 (Fixed TTL for Streamlit cache):
        ```python
        # In src/data_fetcher.py
        # Define a global constant or use a literal for TTL
        STREAMLIT_CACHE_TTL_DAYS = 1
        @st.cache_data(ttl=timedelta(days=STREAMLIT_CACHE_TTL_DAYS))
        def fetch_stock_data(
            ticker_symbol,
            period="max",
            interval="1d",
            save_to_csv=True,
            cache_dir="data",
            cache_expiry_days=1, # This param is for file cache
        ):
            # ... rest of the function
        ```
        Option 2 (Remove TTL from Streamlit cache, rely on its default or manual clearing):
        ```python
        # In src/data_fetcher.py
        @st.cache_data # No ttl argument, or a fixed one like ttl=3600 for 1 hour
        def fetch_stock_data(
            # ...
        ):
            # ... rest of the function
        ```
        The `cache_expiry_days` parameter should remain for the file-based caching logic within the function.
    *   **Verification Protocol:**
        1.  Ensure the application imports `src.data_fetcher.py` and runs without a `NameError` related to `cache_expiry_days` in the decorator.
        2.  If using Streamlit, verify that data fetching calls are cached by Streamlit as expected (e.g., subsequent calls with same args are faster and don't re-trigger the underlying `yf.Ticker().history()` if the file cache is also bypassed or old).
**Systemic Prevention Mandate:** Ensure developers understand Python's scoping rules, especially concerning decorators and when their arguments are evaluated. Use linters that can catch `NameError` issues. For dynamic configurations within decorators, explore alternative patterns if the decorator library supports them, or manage such dynamic behavior outside the decorator itself.

**-- NEW CRITICAL ARCHITECTURAL FLAW --**
**Category:** Critical Logic Failure (Incorrect Return Value in Main Script)
**Location:** `main.py`, `main()` function, line 788.
**Description:** The `main()` function in `main.py` concludes with `return features_df if "features_df" in locals() else None`. However, within the primary execution path of `main()`, after the introduction of in-sample and out-of-sample data processing, the variable `features_df` is no longer assigned the final combined dataset. The script processes `in_sample_df` and `out_of_sample_df`, and a `combined_df` is created and saved to `signal_output` (line 775). The `features_df` variable, if it exists in `locals()` at all, would be from an earlier, incomplete stage or potentially from a different scope if `main()` were structured differently.
**Consequences:** If `main.main()` is ever imported and called as a function by another part of the system expecting the fully processed DataFrame (with features and signals for the entire period), it will receive an incorrect or `None` value. This breaks the contract of the function if it's intended to return the processed data.
**Justification for Criticality:** This represents a significant logical flaw in the data flow of the main script. While `main.py` is primarily a CLI tool, incorrect return values can lead to subtle bugs if it's later used as a library component or if its return is used for conditional logic not apparent now. It indicates a lack of coherence in variable management post-refactoring.
**Root Cause Analysis:** Refactoring of `main()` to handle in-sample/out-of-sample data processing was not accompanied by an update to the final return statement to reflect the new data flow and variable names for the complete processed dataset.
**Mandated Solution:**
    *   **Immediate Corrective Action:** Modify the return statement in `main.main()` to return the `combined_df` (which contains both in-sample and out-of-sample data with signals) or `None` if `combined_df` was not successfully created.
        ```python
        # In main.py, replace line 788:
        # return features_df if "features_df" in locals() else None
        # With:
        return combined_df if "combined_df" in locals() and combined_df is not None and not combined_df.empty else None
        ```
    *   **Verification Protocol:**
        1.  Run `main.py` successfully with parameters that generate both in-sample and out-of-sample data.
        2.  If `main.main()` is called programmatically, assert that the returned DataFrame is indeed the `combined_df` (concatenation of processed in-sample and out-of-sample dataframes) and contains expected columns (OHLC, features, signals).
        3.  If `main.py` encounters an error that prevents `combined_df` creation, verify it returns `None`.
**Systemic Prevention Mandate:** Implement stricter variable scope management and ensure return values of functions accurately reflect their outputs, especially after significant refactoring. Unit tests for `main.py` (if treated as a callable module) should assert the correctness of its return value under various conditions.

**Part 2: Strategic Architectural Imperatives**

**-- STRATEGIC ARCHITECTURAL IMPERATIVE --**
**Imperative:** Standardize Timezone Handling for All Timestamp Data.
**Architectural Justification:** The PARTIALLY RESOLVED Flaw 3 (Split Date Handling) highlights a remaining risk due to potential timezone mismatches between fetched data and user-defined dates (like `split_date`). Data from `yfinance` can be timezone-aware or naive depending on the exchange/ticker. Comparisons between naive and aware timestamps lead to `TypeError`. To ensure robustness for date-based operations (splitting, filtering, merging):
    1. All `DatetimeIndex` objects for stock data should be consistently converted to a standard timezone (e.g., UTC) immediately after fetching or loading from cache.
    2. All user-provided dates (e.g., `split_date`) should also be normalized to this standard timezone.
**Expected Impact:**
    *   Eliminates `TypeError` exceptions from mixed naive/aware timestamp comparisons.
    *   Ensures correct and consistent data splitting and filtering across all scenarios.
    *   Improves the reliability of time-sensitive calculations and backtest period definitions.

**-- STRATEGIC ARCHITECTURAL IMPERATIVE --**
**Imperative:** Implement a Robust NaN Handling Strategy Across All Data Processing Pipelines.
**Architectural Justification:** While `FeatureFactory` and `main.py` have `drop_na_threshold` options, the point at which NaNs are handled and the consistency of this handling across different execution paths (e.g., `main.py`, `app.py`, `scanner.py`) is crucial. The UI bug (Flaw 6) related to `app.py` using a DataFrame for plotting that was different from the one used in `run_backtest` (potentially due to different NaN states) underscores this.
    1. Define clear stages for NaN handling: e.g., after data fetching (for raw data issues), after feature generation (for indicator lookbacks), and before strategy signal application/backtesting.
    2. Ensure that the DataFrame passed to `run_backtest` is the definitive, NaN-handled version, and this same DataFrame is used for subsequent result interpretation and plotting.
    3. `scanner.py` currently does `features_df.dropna()` (line 74) which drops rows with *any* NaN. This might be too aggressive if some features are not used by the scanning strategy. It should ideally drop NaNs only based on columns required by the *specific* strategy being used for scanning or use a less aggressive threshold.
**Expected Impact:**
    *   Prevents errors due to unexpected NaNs in critical calculations (signals, backtesting).
    *   Ensures consistency in data quality across different parts of the application.
    *   Reduces bugs related to misaligned DataFrames due to varying NaN states.
    *   Improves the reliability of scanner results by ensuring signals are generated on valid data points.

**Part 3: Essential Test Scenarios**

**-- ESSENTIAL TEST SCENARIO --**
**Scenario Title:** Backtester Execution with Buy Signal
**Direct Link to Flaw/Risk:** New Critical Flaw - "Critical Logic Failure (Uninitialized Variable in Backtester)"
**Description:** This test ensures that `run_backtest` executes without crashing when a buy signal is present, specifically verifying that the `trades` list is correctly initialized and used.
**Setup/Steps:**
    1.  Create a minimal `pd.DataFrame` with 'Close', 'buy_signal', 'sell_signal' columns.
    2.  Ensure 'buy_signal' is `True` for at least one row and 'sell_signal' is `False` for all rows.
    3.  Call `src.backtester.run_backtest` with this DataFrame and default financial parameters.
**Expected Outcome:**
    *   `run_backtest` completes without raising a `NameError` or any other exception.
    *   The returned results dictionary should contain a non-empty `trades` list (or at least an initialized empty list if the trade couldn't be afforded).
    *   `results['num_trades']` should be 1 (assuming the trade is affordable).
**Justification for Inclusion:** Directly verifies the fix for a critical crash bug in the backtester.

**-- ESSENTIAL TEST SCENARIO --**
**Scenario Title:** Dashboard Equity Curve and Signal Marker Alignment
**Direct Link to Flaw/Risk:** New Critical Flaw - "Critical Data Integrity / UI Bug (Mismatched DataFrame Indexing in Dashboard)"
**Description:** This test verifies that `app.py` correctly aligns the portfolio equity curve with buy/sell signals, using the same underlying DataFrame for both.
**Setup/Steps:**
    1.  Prepare a mock `features_df` that, after `FeatureFactory`, would have leading NaNs.
    2.  Simulate `strategy.generate_signals` which might internally handle some NaNs or operate on a subset, resulting in `features_with_signals` having a potentially shorter or different index than the initial `features_df`.
    3.  Mock `run_backtest` to return predefined `results` where `results['portfolio_values']` corresponds in length to `features_with_signals`.
    4.  In a test environment for `app.py` (or by inspecting its logic), verify that `portfolio_series` is created using `features_with_signals.index`.
    5.  Verify that `buy_points` and `sell_points` are derived from `features_with_signals`.
    6.  Verify that plotting calls for markers (`equity_fig.add_trace` for buy/sell) use `portfolio_series.loc[buy_points.index]` and `portfolio_series.loc[sell_points.index]` without index errors.
**Expected Outcome:**
    *   No `ValueError` (length mismatch) or `KeyError` (index not found) during the creation of `portfolio_series` or when plotting buy/sell markers.
    *   The buy/sell markers should align with dates present in `features_with_signals`.
**Justification for Inclusion:** Verifies the fix for a critical UI bug that misrepresents backtest results.

**-- ESSENTIAL TEST SCENARIO --**
**Scenario Title:** Data Fetcher Import and Basic Cache Functionality
**Direct Link to Flaw/Risk:** New Critical Flaw - "Critical Initialization Error (Misconfiguration of Streamlit Cache TTL)"
**Description:** This test ensures that `src.data_fetcher.py` can be imported without error and that the Streamlit caching mechanism is properly configured (or gracefully handled if fixed).
**Setup/Steps:**
    1.  Attempt to import `fetch_stock_data` from `src.data_fetcher`.
    2.  (If fix involves a fixed TTL) Call `fetch_stock_data` twice with the same parameters (mocking `yf.Ticker().history` to track calls).
**Expected Outcome:**
    *   `src.data_fetcher` imports without a `NameError` related to `cache_expiry_days` in the decorator.
    *   If Streamlit caching is active, the underlying `yf.Ticker().history` should be called only once for the two identical calls to `fetch_stock_data`.
**Justification for Inclusion:** Verifies the fix for a critical initialization error that could prevent the application from starting or lead to caching failures.

**-- ESSENTIAL TEST SCENARIO --**
**Scenario Title:** `main.py` Data Splitting with Timezone-Naive Fetched Data and Timezone-Aware Split Date
**Direct Link to Flaw/Risk:** Part 1A - Flaw 3 (Potential Data Inconsistency - Split Date Handling) - Unresolved part.
**Description:** This test verifies that `main.py` correctly handles data splitting when `get_stock_data` returns a DataFrame with a timezone-naive index (e.g., for some international exchanges) and `args.split_date` results in a timezone-aware `split_date_ts`.
**Setup/Steps:**
    1.  Mock `src.data_fetcher.get_stock_data` to return a sample DataFrame with a timezone-naive `DatetimeIndex`.
    2.  Run `main.main()` (or the relevant logic path) with a `split_date` argument.
    3.  Inside `main.py`, before the data splitting logic (lines 639, 646), observe or assert that `data.index` is converted to be timezone-aware (e.g., UTC) if `split_date_ts` is timezone-aware.
**Expected Outcome:**
    *   No `TypeError` is raised during the comparison `data.index < split_date_ts` or `data.index >= split_date_ts`.
    *   `in_sample_data_raw` and `out_of_sample_data_raw` are correctly populated based on the (now consistently timezoned) comparison.
**Justification for Inclusion:** Verifies the fix for the outstanding part of a previously identified data inconsistency risk, crucial for reliable backtesting.

**Part 4: Actionable Technical Debt Rectification (Update `technical_debt.md`)**

`docs/technical_debt.md` is currently empty. All identified critical flaws in Part 1B are expected to be rectified immediately. If any mandated solution for a critical flaw from Part 1B cannot be implemented immediately due to *extreme and unavoidable* constraints (which must be heavily justified by the development team), it must be logged as new technical debt.

Assuming immediate rectification of flaws identified in Part 1B:

**Part 5: Audit Conclusion & Next Steps Mandate**

1.  **Critical Path to Compliance:**
    *   **Highest Priority (Crash/Core Functionality):**
        1.  Resolve "Critical Logic Failure (Uninitialized Variable in Backtester)" (`src/backtester.py` - `trades` list).
        2.  Resolve "Critical Initialization Error (Misconfiguration of Streamlit Cache TTL)" (`src/data_fetcher.py` - `@st.cache_data` decorator).
    *   **Second Priority (Data Integrity/UI Correctness):**
        1.  Resolve "Critical Data Integrity / UI Bug (Mismatched DataFrame Indexing in Dashboard)" (`app.py` - DataFrame usage for plotting).
        2.  Fully resolve "Potential Data Inconsistency (Split Date Handling)" (Part 1A, Flaw 3) by implementing timezone consistency for `data.index` in `main.py`.
        3.  Resolve "Critical Logic Failure (Incorrect Return Value in Main Script)" (`main.py` - `main()` return).

2.  **System Integrity Verdict:**
    The system's architectural integrity has **IMPROVED** concerning the specific prior mandates for feature parameterization (Flaw 1), UI strategy parameter validation (Flaw 2), and UI display of trade return percentages (Flaw 4), which are now RESOLVED. However, the split date handling (Flaw 3) remains PARTIALLY RESOLVED.
    Critically, **new significant flaws have been identified** that impact core functionality (backtester crash, Streamlit cache error, incorrect main script return) and UI correctness (`app.py` plotting). Until these new critical flaws and the remainder of Flaw 3 are addressed, the system's reliability for backtesting and dashboard operation is compromised. The presence of these new flaws indicates regressions or gaps in the development and testing process.
