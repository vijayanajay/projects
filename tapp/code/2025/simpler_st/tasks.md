# Project Task Breakdown: Technical Analysis PDF Reporting System

## Project Stats
- **Total Tasks:** 34
- **Total Estimated Hours:** 52
- **Hours Complete:** 7.5
- **Hours Pending:** 44.5
- **% Complete:** 22%

---

## Task List (PDF Reports, Backtest, and Pipeline, Atomic ≤2h Each)

### 1. Data Pipeline
- **1.1** Implement data fetcher for stock price data (e.g., yfinance)  
  - Estimated Time: 1h  
  - Status: Done
- **1.2** Clean and validate raw data (handle missing/outlier values)  
  - Estimated Time: 1.5h  
  - Status: Done
- **1.3** Cache processed data in Parquet files  
  - Estimated Time: 1h  
  - Status: Done
- **1.4** Load cached data for analysis  
  - Estimated Time: 1h  
  - Status: Done

### 2. Backtesting Engine
- **2.1** Implement SMA crossover backtest logic  
  - Estimated Time: 1.5h  
  - Status: Done
- **2.2** Implement RSI strategy backtest logic  
  - Estimated Time: 1.5h  
  - Status: Done
- **2.3** Simulate trade execution and record trade logs  
  - Estimated Time: 1.5h  
  - Status: Pending
- **2.4** Calculate core performance metrics (returns, Sharpe, drawdown, win rate)  
  - Estimated Time: 1.5h  
  - Status: Pending
- **2.5** Export backtest results for report generation  
  - Estimated Time: 1h  
  - Status: Pending

### 3. Market Condition Analysis
- **3.1** Define criteria for market regimes (trending, ranging, volatile, calm)  
  - Estimated Time: 1h  
  - Status: Pending
- **3.2** Implement market regime detection logic  
  - Estimated Time: 1.5h  
  - Status: Pending
- **3.3** Correlate strategy performance with detected market regimes  
  - Estimated Time: 1.5h  
  - Status: Pending
- **3.4** Summarize regime analysis in PDF report  
  - Estimated Time: 1h  
  - Status: Pending

### 4. Design PDF Report Template
- **4.1** Define PDF report sections and layout (outline in Markdown or diagram)  
  - Estimated Time: 1h  
  - Status: Pending
- **4.2** Design PDF template structure (cover, TOC, sections)  
  - Estimated Time: 2h  
  - Status: Pending
- **4.3** Create reusable PDF components for charts, tables, and logs  
  - Estimated Time: 2h  
  - Status: Pending
- **4.4** Add placeholders for analyst notes and suggestions in PDF  
  - Estimated Time: 1h  
  - Status: Pending

### 5. Generate and Integrate Visualizations (PDF)
- **5.1** Implement equity curve plotting for PDF  
  - Estimated Time: 1.5h  
  - Status: Pending
- **5.2** Overlay SMA indicator with annotations for PDF  
  - Estimated Time: 1.5h  
  - Status: Pending
- **5.3** Overlay RSI indicator with annotations for PDF  
  - Estimated Time: 1.5h  
  - Status: Pending
- **5.4** Standardize PDF visual style and legends  
  - Estimated Time: 1h  
  - Status: Pending

### 6. Trade-by-Trade Log and Market Context (PDF)
- **6.1** Capture and store trade entry/exit data for PDF  
  - Estimated Time: 1.5h  
  - Status: Pending
- **6.2** Calculate and log PnL per trade for PDF  
  - Estimated Time: 1h  
  - Status: Pending
- **6.3** Capture market context (trend, volatility, volume) at each trade for PDF  
  - Estimated Time: 1.5h  
  - Status: Pending
- **6.4** Format trade log for PDF inclusion  
  - Estimated Time: 1h  
  - Status: Pending

### 7. Transaction Decision Rationale Logging (PDF)
- **7.1** Log indicator values at decision points for PDF  
  - Estimated Time: 1.5h  
  - Status: Pending
- **7.2** Log algorithmic rationale at each transaction for PDF  
  - Estimated Time: 1h  
  - Status: Pending
- **7.3** Summarize rationale for PDF report section  
  - Estimated Time: 1h  
  - Status: Pending

### 8. Performance Metrics Visualization (PDF)
- **8.1** Visualize metric distributions and highlight outliers in PDF  
  - Estimated Time: 1.5h  
  - Status: Pending

### 9. Analyst Notes & Improvement Suggestions Section (PDF)
- **9.1** Design notes section in PDF report template  
  - Estimated Time: 1h  
  - Status: Pending
- **9.2** Ensure section is visible and editable in PDF (if possible)  
  - Estimated Time: 1h  
  - Status: Pending

### 10. Pipeline Orchestration & Integration
- **10.1** Design and implement a main pipeline script to coordinate fetcher, backtesting, and reporting modules  
  - Estimated Time: 1.5h  
  - Status: Pending
- **10.2** Integrate command-line arguments or config file for pipeline (e.g., date range, stock symbols, strategies)  
  - Estimated Time: 1h  
  - Status: Pending
- **10.3** Ensure proper error handling and logging in orchestration script  
  - Estimated Time: 1h  
  - Status: Pending
- **10.4** Write integration tests for the full pipeline (fetch → backtest → report)  
  - Estimated Time: 1.5h  
  - Status: Pending

## Recent Changes (2025-04-27)

- Updated test in `tests/test_data_fetcher.py`:
  - Now fetches data for `HCLTECH.NS` instead of `RELIANCE.NS`.
  - Uses a 20-year period for robust data fetching.
  - Added print statement for DataFrame output in the test.
- Created/updated `tech_analysis/data/fetcher.py` for stock data fetching logic.
- Investigated yfinance API changes and error handling for robustness.
- Added and passed tests for data cleaning/validation and Parquet caching.
- Implemented `clean_and_validate_data` and `cache_to_parquet` functions.
- Added and passed test for loading cached Parquet data.
- Implemented `load_from_parquet` function.
- Implemented and tested SMA crossover backtest logic in `tech_analysis/backtest.py` with TDD in `tests/test_backtest_engine.py`. Test now passes and logic matches pandas idioms.
- Implemented and tested RSI strategy backtest logic in `tech_analysis/backtest.py` with TDD in `tests/test_backtest_engine.py`. Test now passes and logic matches pandas idioms.

---

_Update task status and hours as you progress. Project stats will update automatically when you recalculate._
