# Task Breakdown for Iterative Trading Strategy Discovery Tool
## Project Statistics

- **Total Estimated Time:** 25h
- **Tasks Completed:** 6/20 (30%)
- **Time Spent:** 80.8h () | **Time Remaining:** 15h (75%)

## Atomic Tasks (1-2h each)

1. **Update Trade Execution Logic**
   - What: Update `Backtester._generate_trades` to use new signals and implement `max_holding_days` exit.
   - Est. Time: 1h
   - Depends: Refactored signals

2. **Remove/Consolidate Redundant Signal Logic**
   - What: Remove duplicate logic from `strategy_optimizer.py`, keep only one source.
   - Est. Time: 1h
   - Depends: Refactored signals

3. **Implement FWT Execution Loop**
   - What: Add main loop to run FWT using `generate_walk_forward_periods`, manage train/test splits.
   - Est. Time: 2h
   - Depends: backtester, data handler

4. **Fix Max Drawdown Calculation**
   - What: Calculate equity curve, then compute Max Drawdown from it.
   - Est. Time: 1h
   - Depends: backtester, trade simulation

5. **Fix Sharpe Ratio Calculation**
   - What: Use daily equity curve returns for Sharpe Ratio, not trade averages.
   - Est. Time: 1h
   - Depends: equity curve logic

6. **Integrate Consistency Score in Iteration**
   - What: Use `calculate_consistency_score` in FWT/iteration manager, include in report.
   - Est. Time: 1h
   - Depends: performance metrics, iteration manager

7. **Remove Redundant Optimization Logic**
   - What: Delete/merge `strategy_optimizer.py` into main optimizer.
   - Est. Time: 1h
   - Depends: refactored optimizer

8. **Fix Trade Entry Timing**
   - What: Ensure trades enter on day after signal (use previous day's signal).
   - Est. Time: 1h
   - Depends: backtester, signal logic

9. **Implement Final Reporting Logic**
   - What: Output success/best attempt as per PRD section 7, include all required metrics.
   - Est. Time: 1h
   - Depends: iteration manager, performance metrics

10. **Add/Improve Code Comments**
    - What: Add concise comments to key logic (signals, trades, metrics).
    - Est. Time: 1h
    - Depends: all modules

11. **Improve Metric Test Coverage**
    - What: Add tests for Sharpe Ratio, Max Drawdown using known equity curves.
    - Est. Time: 1h
    - Depends: fixed metric logic

12. **Make Logging Configurable**
    - What: Add `enable_detailed_logging` flag to config, update logger calls.
    - Est. Time: 1h
    - Depends: config loader, logger

13. **Improve NaN Handling**
    - What: Add check for leading NaNs after ffill, make strategy configurable.
    - Est. Time: 1h
    - Depends: data handler

14. **Clean Up/Document Code**
    - What: Ensure PEP8, add docstrings, update README if needed.
    - Est. Time: 1h
    - Depends: all modules

## Completed Tasks
- Iteration Workflow Manager core logic
- Config file load test
- Minimal config loader
- Config key validation tests
- Config validation logic
- OHLCV structure test
- OHLCV fetch (yfinance)
- Data fetch error test
- Missing data detection test
- Forward-fill missing data
- Resampling validation test
- Time bar resampling
- EMA unit test
- EMA calculation
- SMA test
- SMA calculation
- Crossover signal test
- Crossover logic
- Walk-forward period test
- Walk-forward period calc
- Trade simulation test
- Trade simulation engine
- Test must catch inconsistencies between in-sample and out-of-sample performance
- Test must validate Sharpe ratio, max drawdown, and win rate
- Consistency Score test
- Write tests for Level 0 strategy initialization
- Must handle edge cases (zero trades, negative returns)
- Must produce score between 0-100 with clear interpretation
- Test must catch inconsistencies in multi-period metrics
- Test must verify strategy parameter setup
- Write tests for report structure validation
- Must execute full strategy iteration cycle
- Test must catch invalid parameter ranges
- Must optimize parameters across walk-forward periods
- Test must validate result consistency across iterations
- Write tests for result export functionality
- Implement trade event logger
- Write tests for performance summary logging
- Must produce readable HTML/PDF reports with visualizations
- Test must validate CSV export format
- Test must verify log contains required trade metadata
- Must write structured logs in CSV format
- Test must verify log contains required performance metrics
- Unit tests for Volume MA, RSI, ADX, MACD, BB
- Refactored signal generation logic to unified function (entry=1, exit=-1, hold=0)