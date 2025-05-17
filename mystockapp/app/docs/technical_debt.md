**Debt Title:** Consistent Timezone Handling for Stock Data Index
**Unique Identifier:** TD-20231028-001
**Origin/Context:** Arises from the partially unresolved "Potential Data Inconsistency (Split Date Handling)" flaw (Part 1A, Flaw 3). `main.py` does not yet ensure `data.index` is timezone-aware and consistent with `split_date_ts` before splitting.
**Status (if updating existing):** ADDRESSED (2025-05-17)
**Detailed Description:**
    *   Current: `main.py` now converts `split_date` to a timezone-aware UTC `Timestamp` (`split_date_ts`) AND ensures `data.index` (from `get_stock_data`) is either timezone-aware and in the same timezone as `split_date_ts`, or converts it. The issue has been completely resolved.
    *   Previous: `main.py` converts `split_date` to a timezone-aware UTC `Timestamp` (`split_date_ts`). However, `data.index` (from `get_stock_data`) might be timezone-naive. Comparing naive and aware `DatetimeIndex` objects in pandas raises a `TypeError`.
    *   Ideal: `main.py` should check if `data.index` is naive. If it is, and `split_date_ts` is aware, `data.index` should be localized to a standard timezone (e.g., UTC) before any date-based splitting or filtering operations occur.
    *   Why Debt: Failure to implement this leads to potential runtime errors and incorrect data splitting depending on the source of stock data.
**Impact/Consequences:** `TypeError` during data splitting in `main.py` if fetched data has a naive index. Incorrect in-sample/out-of-sample periods. Unreliable backtests.
**Proposed Rectification (Task/Feature):**
    *   Goal: Ensure `data.index` and `split_date_ts` in `main.py` have compatible timezones before comparison for splitting.
    *   Specific Actionable Steps:
        1.  In `main.py`, after `data = get_stock_data(...)` and after `split_date_ts` is defined:
        2.  Check `if data.index.tzinfo is None and split_date_ts.tzinfo is not None:`.
        3.  If true, `data.index = data.index.tz_localize('UTC')` (or another appropriate standard timezone, with error handling for ambiguous times if necessary).
        4.  If `data.index.tzinfo` is not None but differs from `split_date_ts.tzinfo`, convert `data.index` using `data.index.tz_convert('UTC')`.
    *   Acceptance Criteria / Definition of Done: `main.py` successfully splits data regardless of whether `get_stock_data` returns naive or aware `DatetimeIndex`, provided `split_date` is given. No `TypeError` during index comparison. Data split is verifiably correct.
**Estimated Effort/Priority:** Small / High
