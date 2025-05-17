# Stock Trading App Test Suite

This directory contains automated tests for the stock trading application. The tests verify various components and scenarios to ensure the application behaves correctly.

## Test Scenarios

1. **Data Insufficient for Indicator Calculation** (`test_insufficient_data.py`)
   - Tests the behavior when input data is too short for calculating indicators.

2. **Split Date Edge Cases** (`test_split_date_edge_cases.py`)
   - Tests behavior when split dates are at extreme points (first date, last date, etc.).

3. **Backtest with Zero Capital or Zero Costs** (`test_backtest_edge_cases.py`)
   - Tests the backtester with extreme financial parameters.

4. **Data Fetching Failure Simulation** (`test_data_fetching_failure.py`)
   - Tests how the application handles failures in fetching data from yfinance.

## Running the Tests

### Prerequisites

- Make sure you have installed pytest:
  ```
  pip install pytest
  ```

### Running All Tests

From the project root directory, run:

```bash
python -m pytest tests/
```

### Running Specific Test Files

To run tests from a specific file:

```bash
python -m pytest tests/test_insufficient_data.py
```

### Running with Detailed Output

For more detailed output, including print statements and logs:

```bash
python -m pytest tests/ -v
```

### Running with Coverage Report

To generate a test coverage report (requires pytest-cov):

```bash
pip install pytest-cov
python -m pytest tests/ --cov=src
```

## Writing New Tests

When adding new tests:

1. Create a new test file in the `tests/` directory.
2. Import the necessary modules from the application.
3. Use pytest fixtures for common test data.
4. Follow the naming convention: `test_*.py` for files and `test_*` for test functions.
5. Add the new test file to this README.
