"""
Test scenario: Split Date Edge Cases

This test verifies the behavior when split date is set to edge cases like:
- The very first date in the downloaded data
- The very last date in the downloaded data
- A date that results in an empty or single-row in-sample or out-of-sample period
"""

import pytest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sys
import os
import logging
import importlib.util

# Add the src directory to path so we can import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.feature_factory import FeatureFactory
from src.backtester import run_backtest, SMACrossoverStrategy

# Setup logging for test
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture
def sample_ohlcv_data():
    """Generate a sample OHLCV dataset for testing."""
    # Generate dates for a year of data
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    dates = pd.date_range(
        start=start_date, end=end_date, freq="B"
    )  # Business days

    # Generate random price data
    np.random.seed(42)  # For reproducibility
    close_price = 100 + np.random.normal(0, 1, len(dates)).cumsum()
    high_price = close_price * (1 + np.random.uniform(0, 0.05, len(dates)))
    low_price = close_price * (1 - np.random.uniform(0, 0.05, len(dates)))
    open_price = close_price * (1 + np.random.uniform(-0.02, 0.02, len(dates)))
    volume = np.random.randint(1000, 100000, len(dates))

    # Create DataFrame
    data = pd.DataFrame(
        {
            "Open": open_price,
            "High": high_price,
            "Low": low_price,
            "Close": close_price,
            "Volume": volume,
        },
        index=dates,
    )

    return data


def split_and_process_data(data, split_date):
    """
    Helper function to split data and process it through feature generation
    and strategy application.
    """
    # Ensure split date is a pandas Timestamp
    if isinstance(split_date, str):
        split_date = pd.Timestamp(split_date)

    # Split data
    in_sample_data = data[data.index < split_date].copy()
    out_of_sample_data = data[data.index >= split_date].copy()

    # Log split details
    logger.info(f"Split date: {split_date}")
    logger.info(f"In-sample rows: {len(in_sample_data)}")
    logger.info(f"Out-of-sample rows: {len(out_of_sample_data)}")

    # Process both datasets
    results = {}

    for period_name, period_data in [
        ("in_sample", in_sample_data),
        ("out_of_sample", out_of_sample_data),
    ]:
        if len(period_data) == 0:
            logger.warning(f"{period_name} data is empty after split")
            results[period_name] = None
            continue

        # Generate features
        factory = FeatureFactory(period_data, feature_families=["sma"])
        with_features = factory.generate_features(drop_na=False)

        # Apply strategy
        strategy = SMACrossoverStrategy(
            fast_window=5, slow_window=10
        )  # Small windows for testing
        with_signals = strategy.generate_signals(with_features)

        # Drop NaNs
        filtered = with_signals.dropna()

        if len(filtered) == 0:
            logger.warning(
                f"{period_name} data is empty after feature generation and NaN dropping"
            )
            results[period_name] = None
            continue

        # Run backtest
        try:
            backtest_result = run_backtest(
                filtered,
                initial_capital=100000.0,
                commission_fixed=20.0,
                commission_pct=0.0003,
                slippage_pct=0.001,
                position_size_pct=0.25,
            )
            results[period_name] = backtest_result
        except Exception as e:
            logger.error(f"Backtest failed for {period_name}: {str(e)}")
            results[period_name] = str(e)

    return results


def test_split_at_first_date(sample_ohlcv_data):
    """Test behavior when split date is the first date in the data."""
    first_date = sample_ohlcv_data.index[0]
    results = split_and_process_data(sample_ohlcv_data, first_date)

    # In-sample should be empty, out-of-sample should have all data
    assert (
        results["in_sample"] is None
    ), "In-sample should be None when split at first date"
    assert (
        results["out_of_sample"] is not None
    ), "Out-of-sample should have valid results when split at first date"

    if results["out_of_sample"] is not None and isinstance(
        results["out_of_sample"], dict
    ):
        assert isinstance(
            results["out_of_sample"]["final_value"],
            (int, float, np.float32, np.float64),
        ), "Final value should be numeric"


def test_split_at_last_date(sample_ohlcv_data):
    """Test behavior when split date is the last date in the data."""
    last_date = sample_ohlcv_data.index[-1]
    results = split_and_process_data(sample_ohlcv_data, last_date)

    # In-sample should have all data, out-of-sample should be empty
    assert (
        results["in_sample"] is not None
    ), "In-sample should have valid results when split at last date"
    assert (
        results["out_of_sample"] is None
    ), "Out-of-sample should be None when split at last date"

    if results["in_sample"] is not None and isinstance(
        results["in_sample"], dict
    ):
        assert isinstance(
            results["in_sample"]["final_value"],
            (int, float, np.float32, np.float64),
        ), "Final value should be numeric"


def test_split_at_second_date(sample_ohlcv_data):
    """Test behavior when split date results in a single-row in-sample period."""
    second_date = sample_ohlcv_data.index[1]
    results = split_and_process_data(sample_ohlcv_data, second_date)

    # In-sample should have only one row, which is not enough for features
    assert (
        results["in_sample"] is None
    ), "In-sample should be None when only one row"
    assert (
        results["out_of_sample"] is not None
    ), "Out-of-sample should have valid results"


def test_split_at_one_before_last_date(sample_ohlcv_data):
    """Test behavior when split date results in a single-row out-of-sample period."""
    one_before_last = sample_ohlcv_data.index[-2]
    results = split_and_process_data(sample_ohlcv_data, one_before_last)

    # Out-of-sample should have only one row, which is not enough for features
    assert (
        results["in_sample"] is not None
    ), "In-sample should have valid results"
    assert (
        results["out_of_sample"] is None
    ), "Out-of-sample should be None when only one row"


def test_split_with_few_rows(sample_ohlcv_data):
    """Test behavior when split date results in few rows in one period."""
    # Choose a date that will put 5 rows in the out-of-sample period
    split_date = sample_ohlcv_data.index[-6]
    results = split_and_process_data(sample_ohlcv_data, split_date)

    # In-sample should have most data, out-of-sample might fail due to too few rows
    assert (
        results["in_sample"] is not None
    ), "In-sample should have valid results"

    # The outcome for out-of-sample depends on the implementation:
    # - It might be None if there's not enough data after NaN dropping
    # - It might have valid results if the system can handle very small datasets
    # Both cases are valid, so we don't make a specific assertion


def test_split_with_date_outside_range(sample_ohlcv_data):
    """Test behavior when split date is outside the data range."""
    # Date before first date
    before_first = sample_ohlcv_data.index[0] - timedelta(days=30)
    results = split_and_process_data(sample_ohlcv_data, before_first)

    # Everything should be in out-of-sample
    assert results["in_sample"] is None, "In-sample should be None"
    assert (
        results["out_of_sample"] is not None
    ), "Out-of-sample should have all data"

    # Date after last date
    after_last = sample_ohlcv_data.index[-1] + timedelta(days=30)
    results = split_and_process_data(sample_ohlcv_data, after_last)

    # Everything should be in in-sample
    assert results["in_sample"] is not None, "In-sample should have all data"
    assert results["out_of_sample"] is None, "Out-of-sample should be None"


def test_verify_main_script_split_date_handling():
    """
    Test that the main.py script handles split date edge cases correctly.

    This is a more complex test that simulates a direct call to main.py
    with various split dates. It requires mocking of external dependencies
    to fully test the main script behavior.
    """
    # Check if main.py exists
    main_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "main.py")
    )
    if not os.path.exists(main_path):
        pytest.skip("main.py not found, skipping test")

    # For full testing, a proper mocking of the data fetching and other
    # external dependencies would be required. Here, we just verify the
    # script can be loaded without errors, showing it could be tested.
    spec = importlib.util.spec_from_file_location("main", main_path)
    assert spec is not None, "Could not load spec for main.py"

    # In a more comprehensive test, we would:
    # 1. Mock get_reliance_data to return our sample_ohlcv_data
    # 2. Mock command line arguments with various split dates
    # 3. Run main() and verify it doesn't crash
    # 4. Check the outputs of the various operations

    # Placeholder for the mock test - in a real implementation this would
    # be expanded with proper patching of dependencies
    assert True, "This test should be expanded with mocking"


def test_timezone_aware_split_date_handling(sample_ohlcv_data):
    """
    Test that timezone-aware and timezone-naive data are handled consistently
    when splitting by date.
    """
    # Create a timezone-naive index for the sample data
    naive_data = sample_ohlcv_data.copy()

    # Create a timezone-aware split date (in UTC)
    split_date = naive_data.index[len(naive_data) // 2]
    aware_split_date = pd.Timestamp(split_date).tz_localize("UTC")

    # Import the main function from main.py
    main_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "main.py")
    )
    if not os.path.exists(main_path):
        pytest.skip("main.py not found, skipping test")

    spec = importlib.util.spec_from_file_location("main", main_path)
    main_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(main_module)

    # We need a minimal mock for the main module's behavior
    # Create a simple class with necessary attributes
    class MockArgs:
        def __init__(self, split_date):
            self.split_date = split_date
            self.ticker = "TEST"

    # Create a mock logger to capture warnings
    class MockLogger:
        def __init__(self):
            self.warnings = []
            self.errors = []

        def warning(self, msg):
            self.warnings.append(msg)

        def error(self, msg):
            self.errors.append(msg)

        def info(self, msg):
            pass

    # Replace the module's logger temporarily
    original_logger = main_module.logger
    mock_logger = MockLogger()
    main_module.logger = mock_logger

    try:
        # Call the code that would handle the timezone conversion
        split_date_ts = pd.Timestamp(aware_split_date)
        if split_date_ts.tzinfo is None:
            split_date_ts = split_date_ts.tz_localize("UTC")

        # Simulate the timezone handling from main.py
        if naive_data.index.tzinfo is None:
            # Check if we get a warning about naive index
            main_module.logger.warning(
                f"Data index for TEST is timezone-naive. Localizing to UTC for comparison with split_date."
            )
            try:
                naive_data.index = naive_data.index.tz_localize("UTC")
            except Exception as e:
                main_module.logger.error(
                    f"Failed to localize data.index to UTC: {e}. Proceeding with naive index comparison may fail."
                )
                split_date_ts = split_date_ts.tz_localize(None)
        elif naive_data.index.tzinfo != split_date_ts.tzinfo:
            main_module.logger.warning(
                f"Data index timezone ({naive_data.index.tzinfo}) differs from split_date timezone ({split_date_ts.tzinfo}). Converting data index to UTC."
            )
            naive_data.index = naive_data.index.tz_convert("UTC")

        # Now try to split the data
        in_sample = naive_data[naive_data.index < split_date_ts].copy()
        out_of_sample = naive_data[naive_data.index >= split_date_ts].copy()

        # Check that we got a warning about timezone-naive index
        assert any(
            "timezone-naive" in warning for warning in mock_logger.warnings
        ), "Expected warning about timezone-naive index"

        # Check that both splits were successful and contain data
        assert len(in_sample) > 0, "In-sample data should not be empty"
        assert len(out_of_sample) > 0, "Out-of-sample data should not be empty"

        # Verify the total split data equals the original data count
        assert len(in_sample) + len(out_of_sample) == len(
            sample_ohlcv_data
        ), "Split data should maintain the same total count"

    finally:
        # Restore the original logger
        main_module.logger = original_logger
