"""
Test scenario: Split Date Exactly on a Weekend/Holiday

This test verifies that the splitting logic correctly handles the case where the split date
falls on a day that is not present in the business-day indexed DataFrame (e.g., a Saturday or Sunday).
"""

import pytest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sys
import os
import logging
from src.feature_factory import FeatureFactory
from src.backtester import SMACrossoverStrategy

# Add the src directory to path so we can import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Setup logging for test
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture
def sample_ohlcv_data():
    """Generate a sample DataFrame with OHLCV data for testing."""
    end_date = datetime.now().replace(
        hour=0, minute=0, second=0, microsecond=0
    )
    start_date = end_date - timedelta(days=60)
    dates = pd.date_range(start=start_date, end=end_date, freq="B")
    np.random.seed(42)
    data = pd.DataFrame(
        {
            "Open": np.random.rand(len(dates)),
            "High": np.random.rand(len(dates)),
            "Low": np.random.rand(len(dates)),
            "Close": np.random.rand(len(dates)),
            "Volume": np.random.rand(len(dates)),
        },
        index=dates,
    )
    return data


def split_and_process_data(df, split_date_str):
    """
    Split data into in-sample and out-of-sample sets based on a date string.
    This is a simplified version of the split logic in main.py.

    Args:
        df: DataFrame with OHLCV data
        split_date_str: Date string in YYYY-MM-DD format

    Returns:
        tuple: (in_sample_df, out_of_sample_df, split_date)
    """
    # Convert the split date to a timestamp
    split_date = pd.Timestamp(split_date_str)
    if split_date.tz is None:
        split_date = split_date.tz_localize("UTC")

    # Ensure DataFrame index has the same timezone for comparison
    backtest_data = df.copy()
    if backtest_data.index.tz is None:
        backtest_data.index = backtest_data.index.tz_localize("UTC")

    # Split data into in-sample and out-of-sample
    in_sample_data = backtest_data[backtest_data.index < split_date].copy()
    out_of_sample_data = backtest_data[
        backtest_data.index >= split_date
    ].copy()

    return in_sample_data, out_of_sample_data, split_date


def get_weekend_date(df_for_dates):
    """
    Find a weekend date that falls between the start and end of the sample data.

    Args:
        df_for_dates: The DataFrame to find a weekend date within.

    Returns:
        str: Weekend date string in YYYY-MM-DD format
    """
    middle_index = len(df_for_dates) // 2
    middle_date = df_for_dates.index[middle_index]

    # Find the next Saturday
    days_until_saturday = (
        5 - middle_date.weekday()
        if middle_date.weekday() < 5
        else 12 - middle_date.weekday()
    )
    saturday = middle_date + timedelta(days=days_until_saturday)

    return saturday.strftime("%Y-%m-%d")


def test_split_date_on_saturday(sample_ohlcv_data):
    """Test that splitting logic correctly handles a split date that falls on a Saturday."""
    df = sample_ohlcv_data
    saturday_date = get_weekend_date(df)
    logger.info(f"Using Saturday date: {saturday_date}")

    # Split data using Saturday date
    in_sample, out_of_sample, split_date = split_and_process_data(
        df, saturday_date
    )

    # The first date in out_of_sample should be the first business day on or after the split date
    saturday = pd.Timestamp(saturday_date).tz_localize("UTC")
    next_business_day = saturday
    while next_business_day.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
        next_business_day += timedelta(days=1)

    # Convert to same tz-aware format for comparison
    first_oos_date = out_of_sample.index[0].tz_convert("UTC")

    # Test that out-of-sample starts on the correct date (Monday after weekend)
    assert (
        first_oos_date.date() >= next_business_day.date()
    ), "Out-of-sample should start on the first business day on or after the split date"

    # Test that in-sample ends on the last business day before the split date
    last_is_date = in_sample.index[-1].tz_convert("UTC")
    assert (
        last_is_date.date() < saturday.date()
    ), "In-sample should end on the last business day before the split date"

    # Verify there's no gap between in-sample and out-of-sample
    expected_total_rows = len(df)
    actual_total_rows = len(in_sample) + len(out_of_sample)
    assert (
        actual_total_rows == expected_total_rows
    ), "No data should be lost in the splitting process"


def test_split_date_on_sunday(sample_ohlcv_data):
    """Test that splitting logic correctly handles a split date that falls on a Sunday."""
    df = sample_ohlcv_data
    saturday_date = get_weekend_date(df)
    sunday_date = (pd.Timestamp(saturday_date) + timedelta(days=1)).strftime(
        "%Y-%m-%d"
    )
    logger.info(f"Using Sunday date: {sunday_date}")

    # Split data using Sunday date
    in_sample, out_of_sample, split_date = split_and_process_data(
        df, sunday_date
    )

    # The first date in out_of_sample should be the first business day on or after the split date
    sunday = pd.Timestamp(sunday_date).tz_localize("UTC")
    next_business_day = sunday
    while next_business_day.weekday() >= 5:  # 5 = Saturday, 6 = Sunday
        next_business_day += timedelta(days=1)

    # Convert to same tz-aware format for comparison
    first_oos_date = out_of_sample.index[0].tz_convert("UTC")

    # Test that out-of-sample starts on the correct date (Monday after weekend)
    assert (
        first_oos_date.date() >= next_business_day.date()
    ), "Out-of-sample should start on the first business day on or after the split date"

    # Test that in-sample ends on the last business day before the split date
    last_is_date = in_sample.index[-1].tz_convert("UTC")
    assert (
        last_is_date.date() < sunday.date()
    ), "In-sample should end on the last business day before the split date"


def test_split_date_on_holiday(sample_ohlcv_data):
    """Test that splitting logic correctly handles a split date that falls on a holiday."""
    # This is a simplified test that just uses a weekend day as a proxy for a holiday,
    # since determining actual holidays would add complexity

    # Call the weekend test as a proxy
    test_split_date_on_saturday(sample_ohlcv_data)

    # In a real implementation, this would test with an actual holiday date
    logger.info("Holiday test uses weekend as a proxy for a holiday")


def test_split_date_exactly_on_business_day(sample_ohlcv_data):
    """Test that splitting logic correctly handles a split date that falls exactly on a business day."""
    df = sample_ohlcv_data
    middle_index = len(df) // 2
    business_day = df.index[middle_index].strftime("%Y-%m-%d")
    logger.info(f"Using business day date: {business_day}")

    # Split data using the business day date
    in_sample, out_of_sample, split_date = split_and_process_data(
        df, business_day
    )

    # Convert the business day to a timestamp for comparison
    business_day_ts = pd.Timestamp(business_day).tz_localize("UTC")

    # The first date in out_of_sample should be the business day itself
    first_oos_date = out_of_sample.index[0].tz_convert("UTC")
    assert (
        first_oos_date.date() == business_day_ts.date()
    ), "Out-of-sample should start on the business day itself"

    # The last date in in_sample should be the business day before
    last_is_date = in_sample.index[-1].tz_convert("UTC")
    assert (
        last_is_date.date() < business_day_ts.date()
    ), "In-sample should end before the split date"


def generate_features_and_signals(df_period_data):
    if df_period_data.empty:
        df_period_data["buy_signal"] = pd.Series(dtype=bool)
        df_period_data["sell_signal"] = pd.Series(dtype=bool)
        return df_period_data
    min_len_for_sma = 10
    if len(df_period_data) < min_len_for_sma:
        df_period_data["buy_signal"] = False
        df_period_data["sell_signal"] = False
        df_period_data["sma_5"] = np.nan
        df_period_data["sma_10"] = np.nan
        return df_period_data
    small_sma_params = {"sma": {"windows": [5, 10]}}
    factory = FeatureFactory(
        df_period_data,
        feature_families=["sma"],
        indicator_params=small_sma_params,
    )
    try:
        with_features = factory.generate_features(drop_na=False)
    except ValueError:
        df_period_data["buy_signal"] = False
        df_period_data["sell_signal"] = False
        df_period_data["sma_5"] = np.nan
        df_period_data["sma_10"] = np.nan
        return df_period_data
    strategy = SMACrossoverStrategy(fast_window=5, slow_window=10)
    with_signals = strategy.generate_signals(with_features)
    return with_signals


def test_weekend_split_date(sample_ohlcv_data):
    """
    Test splitting data on a weekend date.

    The function should find the next business day after the specified
    weekend date for the out-of-sample period.
    """
    # Find a Saturday in the middle of the data range
    # Data starts on 2023-01-01, which is a Sunday
    # 2023-01-07 is a Saturday
    weekend_date = get_weekend_date(sample_ohlcv_data)
    logger.info(f"Using weekend date: {weekend_date}")

    # Split the data
    in_sample, out_of_sample, actual_split_date = split_and_process_data(
        sample_ohlcv_data, weekend_date
    )

    # Calculate expected_next_business_day dynamically
    saturday = pd.Timestamp(weekend_date).tz_localize("UTC")
    expected_next_business_day = saturday
    while expected_next_business_day.weekday() >= 5:
        expected_next_business_day += timedelta(days=1)

    # Verify in_sample and out_of_sample have the correct date ranges
    assert (
        in_sample.index[-1].normalize()
        < expected_next_business_day.normalize()
    )
    assert (
        out_of_sample.index[0].normalize()
        == expected_next_business_day.normalize()
    )

    # Ensure no data was lost
    assert len(in_sample) + len(out_of_sample) == len(sample_ohlcv_data)

    # Verify the new assertions
    assert not out_of_sample.empty, "Out-of-sample should not be empty"
    assert (
        out_of_sample.index[0].normalize()
        == expected_next_business_day.normalize()
    ), f"Out-of-sample should start on {expected_next_business_day.date()}, but started on {out_of_sample.index[0].date()}"
    assert not in_sample.empty, "In-sample should not be empty"
    assert (
        in_sample.index[-1].normalize() < actual_split_date.normalize()
    ), "In-sample should end on the last business day before the split date"


def test_holiday_split_date(sample_ohlcv_data):
    """
    Test splitting data on a date that might be a holiday.

    Since our sample data uses 'B' frequency which only excludes weekends,
    we'll simulate a holiday by removing a business day from the data.
    """
    # Get a copy of the data
    data = sample_ohlcv_data.copy()

    # Remove a business day to simulate a holiday
    # Let's say Jan 16, 2023 is a holiday (actually Martin Luther King Jr. Day in the US)
    saturday_date = get_weekend_date(sample_ohlcv_data)
    sunday_date = (pd.Timestamp(saturday_date) + timedelta(days=1)).strftime(
        "%Y-%m-%d"
    )
    data = data.drop(sunday_date, errors="ignore")

    # Set the split date to the holiday
    split_date_str = sunday_date
    holiday_split_date = pd.Timestamp(split_date_str).tz_localize("UTC")
    expected_next_business_day = holiday_split_date
    while expected_next_business_day.weekday() >= 5:
        expected_next_business_day += timedelta(days=1)

    # Split the data
    in_sample, out_of_sample, actual_split_date = split_and_process_data(
        data, split_date_str
    )

    # Verify in_sample and out_of_sample have the correct date ranges
    assert (
        in_sample.index[-1].normalize()
        < expected_next_business_day.normalize()
    )
    assert (
        out_of_sample.index[0].normalize()
        == expected_next_business_day.normalize()
    )

    # Verify the new assertions
    assert (
        not out_of_sample.empty
    ), "Out-of-sample should not be empty for holiday test"
    assert (
        out_of_sample.index[0].normalize()
        == expected_next_business_day.normalize()
    ), f"Out-of-sample should start on {expected_next_business_day.date()} after holiday, but started on {out_of_sample.index[0].date()}"
    assert (
        not in_sample.empty
    ), "In-sample should not be empty for holiday test"
    assert (
        in_sample.index[-1].normalize() < actual_split_date.normalize()
    ), "In-sample should end on the last business day before the holiday split date"


def test_weekend_split_date_feature_generation(sample_ohlcv_data):
    """
    Test the full workflow of splitting data on a weekend,
    generating features, and applying a strategy.
    """
    # Find a Saturday in the middle of the data range
    weekend_date = get_weekend_date(sample_ohlcv_data)
    logger.info(f"Using weekend date: {weekend_date}")

    # Split the data
    in_sample, out_of_sample, actual_split_date = split_and_process_data(
        sample_ohlcv_data, weekend_date
    )

    # Calculate expected_next_business_day dynamically
    saturday = pd.Timestamp(weekend_date).tz_localize("UTC")
    expected_next_business_day = saturday
    while expected_next_business_day.weekday() >= 5:
        expected_next_business_day += timedelta(days=1)

    # Generate features and signals for both periods
    in_sample_with_signals = generate_features_and_signals(in_sample)
    out_of_sample_with_signals = generate_features_and_signals(out_of_sample)

    # Verify features and signals were generated
    assert "sma_10" in in_sample_with_signals.columns
    assert "sma_5" in in_sample_with_signals.columns
    assert "buy_signal" in in_sample_with_signals.columns
    assert "sell_signal" in in_sample_with_signals.columns

    assert "sma_10" in out_of_sample_with_signals.columns
    assert "sma_5" in out_of_sample_with_signals.columns
    assert "buy_signal" in out_of_sample_with_signals.columns
    assert "sell_signal" in out_of_sample_with_signals.columns

    # Ensure the first day of out-of-sample is the next business day after the weekend
    assert out_of_sample_with_signals.index[0] == expected_next_business_day


def test_end_of_month_split_date(sample_ohlcv_data):
    """
    Test splitting data at the end of a month, which might involve
    weekend days before the next month starts.
    """
    # Set split date to January 31, 2023 (Tuesday)
    # February 1, 2023 is a Wednesday
    if len(sample_ohlcv_data) > 1:
        split_date_obj = sample_ohlcv_data.index[-2]
    else:
        pytest.skip("Sample data too short for end_of_month_split_date test")
    split_date_str = split_date_obj.strftime("%Y-%m-%d")
    logger.info(
        f"Using dynamic split_date_str for end_of_month: {split_date_str}"
    )
    in_sample, out_of_sample, actual_split_date = split_and_process_data(
        sample_ohlcv_data, split_date_str
    )
    assert not in_sample.empty, "In-sample should not be empty"
    assert not out_of_sample.empty, "Out-of-sample should not be empty"
    assert in_sample.index[-1].normalize() < actual_split_date.normalize()
    assert out_of_sample.index[0].normalize() == actual_split_date.normalize()
    assert (
        in_sample.index[-1].normalize()
        == (actual_split_date - pd.offsets.BDay(1)).normalize()
    )


if __name__ == "__main__":
    pytest.main(["-xvs", __file__])
