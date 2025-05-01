# Task Breakdown for Iterative Trading Strategy Discovery Tool
## Project Statistics

- **Total Estimated Time:** 25h
- **Tasks Completed:** 6/20 (30%)
- **Time Spent:** 78.8h () | **Time Remaining:** 17h (85%)

## Atomic Tasks (1-2h each)

1. **Implement Iteration Workflow Manager**
   - What: Create core logic to manage Level 0-4 iteration as per PRD (FR-F06-F09).
   - Est. Time: 2h
   - Depends: config loader, base strategy, backtester
   - Status: done

2. **Integrate Performance Criteria Checks**
   - What: Add logic to evaluate `target_return_pct` and Consistency Score after each level, controlling iteration flow.
   - Est. Time: 1h
   - Depends: Iteration manager, performance metrics
   - Status: done

3. **Implement Volume MA Calculation**
   - What: Add function for Volume MA in `indicator_calculator.py`.
   - Est. Time: 1h
   - Depends: pandas/numpy, data handler
   - Status: done

4. **Implement RSI, ADX, MACD, Bollinger Bands**
   - What: Add functions for RSI, ADX, MACD, Bollinger Bands in `indicator_calculator.py`.
   - Est. Time: 2h
   - Depends: pandas/numpy, data handler
   - Status: done

6. **Refactor Signal Generation Logic**
   - What: Create a single, consistent signal function (entry=1, exit=-1, hold=0) per PRD.
   - Est. Time: 1h
   - Depends: strategy.py, PRD rules
   - Status: done

7. **Update Trade Execution Logic**
   - What: Update `Backtester._generate_trades` to use new signals and implement `max_holding_days` exit.
   - Est. Time: 1h
   - Depends: Refactored signals

8. **Remove/Consolidate Redundant Signal Logic**
   - What: Remove duplicate logic from `strategy_optimizer.py`, keep only one source.
   - Est. Time: 1h
   - Depends: Refactored signals

9. **Implement FWT Execution Loop**
   - What: Add main loop to run FWT using `generate_walk_forward_periods`, manage train/test splits.
   - Est. Time: 2h
   - Depends: backtester, data handler

10. **Fix Max Drawdown Calculation**
    - What: Calculate equity curve, then compute Max Drawdown from it.
    - Est. Time: 1h
    - Depends: backtester, trade simulation

11. **Fix Sharpe Ratio Calculation**
    - What: Use daily equity curve returns for Sharpe Ratio, not trade averages.
    - Est. Time: 1h
    - Depends: equity curve logic

12. **Integrate Consistency Score in Iteration**
    - What: Use `calculate_consistency_score` in FWT/iteration manager, include in report.
    - Est. Time: 1h
    - Depends: performance metrics, iteration manager

13. **Remove Redundant Optimization Logic**
    - What: Delete/merge `strategy_optimizer.py` into main optimizer.
    - Est. Time: 1h
    - Depends: refactored optimizer

14. **Fix Trade Entry Timing**
    - What: Ensure trades enter on day after signal (use previous day's signal).
    - Est. Time: 1h
    - Depends: backtester, signal logic

15. **Implement Final Reporting Logic**
    - What: Output success/best attempt as per PRD section 7, include all required metrics.
    - Est. Time: 1h
    - Depends: iteration manager, performance metrics

16. **Add/Improve Code Comments**
    - What: Add concise comments to key logic (signals, trades, metrics).
    - Est. Time: 1h
    - Depends: all modules

17. **Improve Metric Test Coverage**
    - What: Add tests for Sharpe Ratio, Max Drawdown using known equity curves.
    - Est. Time: 1h
    - Depends: fixed metric logic

18. **Make Logging Configurable**
    - What: Add `enable_detailed_logging` flag to config, update logger calls.
    - Est. Time: 1h
    - Depends: config loader, logger

19. **Improve NaN Handling**
    - What: Add check for leading NaNs after ffill, make strategy configurable.
    - Est. Time: 1h
    - Depends: data handler

20. **Clean Up/Document Code**
    - What: Ensure PEP8, add docstrings, update README if needed.
    - Est. Time: 1h
    - Depends: all modules

## Completed Tasks
- IMPLEMENT-001A: Iteration Workflow Manager core logic
- CONFIG-001A: Config file load test
- CONFIG-001B: Minimal config loader
- CONFIG-002A: Config key validation tests
- CONFIG-002B: Config validation logic
- DATA-001A: OHLCV structure test
- DATA-001B: OHLCV fetch (yfinance)
- DATA-001C: Data fetch error test
- DATA-002A: Missing data detection test
- DATA-002B: Forward-fill missing data
- DATA-003A: Resampling validation test
- DATA-003B: Time bar resampling
- STRATEGY-001A: EMA unit test
- STRATEGY-001B: EMA calculation
- STRATEGY-002A: SMA test
- STRATEGY-002B: SMA calculation
- STRATEGY-003A: Crossover signal test
- STRATEGY-003B: Crossover logic
- FWT-001A: Walk-forward period test
- FWT-001B: Walk-forward period calc
- FWT-002A: Trade simulation test
- FWT-002B: Trade simulation engine
- FWT-003A: Test must catch inconsistencies between in-sample and out-of-sample performance
- METRICS-001A: Test must validate Sharpe ratio, max drawdown, and win rate
- METRICS-002A: Consistency Score test
- ITERATION-001A: Write tests for Level 0 strategy initialization
- METRICS-001B: Must handle edge cases (zero trades, negative returns)
- METRICS-002B: Must produce score between 0-100 with clear interpretation
- METRICS-003A: Test must catch inconsistencies in multi-period metrics
- ITERATION-001A: Test must verify strategy parameter setup
- REPORT-001A: Write tests for report structure validation
- ITERATION-001B: Must execute full strategy iteration cycle
- ITERATION-002A: Test must catch invalid parameter ranges
- ITERATION-002B: Must optimize parameters across walk-forward periods
- ITERATION-003A: Test must validate result consistency across iterations
- REPORT-002A: Write tests for result export functionality
- LOGGING-001B: Implement trade event logger
- LOGGING-002A: Write tests for performance summary logging
- REPORT-001B: Must produce readable HTML/PDF reports with visualizations
- REPORT-002A: Test must validate CSV export format
- LOGGING-001A: Test must verify log contains required trade metadata
- LOGGING-001B: Must write structured logs in CSV format
- LOGGING-002A: Test must verify log contains required performance metrics
- INDICATOR-001A: Unit tests for Volume MA, RSI, ADX, MACD, BB
- TASK-006: Refactored signal generation logic to unified function (entry=1, exit=-1, hold=0)