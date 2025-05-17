"""
Tests for the nan_handler utility module.

This test file ensures that the nan_handler module correctly detects and handles
NaN values in DataFrames in a consistent manner.
"""

import pandas as pd
import numpy as np
import pytest
import logging
import sys
import os

# Add the src directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.nan_handler import (
    detect_nan_columns,
    handle_nans,
    check_dataframe_compatibility,
    ensure_compatible_datetime_index,
)

# Setup logging for tests
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture
def sample_df_with_nans():
    """Create a sample DataFrame with NaNs for testing."""
    dates = pd.date_range(start="2023-01-01", periods=10)
    df = pd.DataFrame(
        {
            "A": [1, 2, np.nan, 4, 5, 6, 7, 8, 9, 10],
            "B": [1, 2, 3, np.nan, 5, 6, 7, 8, 9, 10],
            "C": [1, 2, 3, 4, np.nan, 6, 7, 8, 9, 10],
            "D": [1, 2, 3, 4, 5, np.nan, 7, 8, 9, 10],
            "E": [1, 2, 3, 4, 5, 6, np.nan, 8, 9, 10],
        },
        index=dates,
    )
    return df


def test_detect_nan_columns(sample_df_with_nans):
    """Test the detect_nan_columns function with and without critical columns."""
    # Test with all columns
    nan_cols, has_critical_nans = detect_nan_columns(sample_df_with_nans)

    assert len(nan_cols) == 5, "Should detect NaNs in all 5 columns"
    assert has_critical_nans, "Should indicate critical columns have NaNs"

    # Test with specific critical columns
    critical_cols = ["A", "B"]
    nan_cols, has_critical_nans = detect_nan_columns(
        sample_df_with_nans, critical_cols
    )

    assert len(nan_cols) == 5, "Should still detect all NaN columns"
    assert (
        has_critical_nans
    ), "Should indicate critical columns (A, B) have NaNs"

    # Test with critical columns that don't have NaNs
    non_nan_df = sample_df_with_nans.copy()
    non_nan_df["F"] = 10  # No NaNs in this column
    critical_cols = ["F"]
    nan_cols, has_critical_nans = detect_nan_columns(non_nan_df, critical_cols)

    assert len(nan_cols) == 5, "Should detect NaNs in original 5 columns"
    assert (
        not has_critical_nans
    ), "Should not indicate critical columns have NaNs"

    # Test with empty DataFrame
    empty_df = pd.DataFrame()
    nan_cols, has_critical_nans = detect_nan_columns(empty_df)

    assert (
        len(nan_cols) == 0
    ), "Should detect no NaN columns in empty DataFrame"
    assert (
        not has_critical_nans
    ), "Should not indicate critical columns have NaNs"


def test_handle_nans_default_threshold(sample_df_with_nans):
    """Test handle_nans with default threshold setting."""
    # Each row has at most 1 NaN out of 5 columns (20% NaNs),
    # so default threshold of 0.25 (25%) should keep all rows
    df_result, stats = handle_nans(sample_df_with_nans)

    assert len(df_result) == len(
        sample_df_with_nans
    ), "Should not drop any rows with default threshold"
    assert stats["rows_dropped"] == 0, "Stats should show 0 rows dropped"

    # Add more NaNs to one row to exceed default threshold (3 out of 5 = 60% NaNs)
    df_more_nans = sample_df_with_nans.copy()
    df_more_nans.loc[df_more_nans.index[2], ["A", "B", "C"]] = np.nan

    df_result, stats = handle_nans(df_more_nans)

    assert len(df_result) < len(df_more_nans), "Should drop row with 60% NaNs"
    assert stats["rows_dropped"] == 1, "Stats should show 1 row dropped"


def test_handle_nans_custom_threshold(sample_df_with_nans):
    """Test handle_nans with custom threshold settings."""
    # Set stringent threshold of 0 (no NaNs allowed)
    df_result, stats = handle_nans(sample_df_with_nans, drop_na_threshold=0)

    # Should drop all rows with any NaNs
    assert len(df_result) == 5, "Should drop all 5 rows with NaNs"
    assert stats["rows_dropped"] == 5, "Stats should show 5 rows dropped"

    # Set higher threshold (3 columns can have NaNs)
    df_result, stats = handle_nans(sample_df_with_nans, drop_na_threshold=3)

    # Should keep all rows as no row has more than 3 NaNs
    assert len(df_result) == len(sample_df_with_nans), "Should keep all rows"


def test_check_dataframe_compatibility():
    """Test the check_dataframe_compatibility function."""
    # Create compatible DataFrames
    df1 = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
    df2 = pd.DataFrame({"A": [7, 8, 9], "B": [10, 11, 12]})

    compatible, info = check_dataframe_compatibility(df1, df2)
    assert compatible, "DataFrames should be compatible"
    assert info == "", "Info string should be empty"

    # Create incompatible DataFrames (column mismatch)
    df3 = pd.DataFrame({"A": [1, 2, 3], "C": [4, 5, 6]})

    compatible, info = check_dataframe_compatibility(df1, df3)
    assert (
        not compatible
    ), "DataFrames should be incompatible due to column mismatch"
    assert "Column mismatch" in info, "Info should mention column mismatch"

    # Test with timezone mismatch
    dates1 = pd.date_range(start="2023-01-01", periods=3, tz="UTC")
    dates2 = pd.date_range(start="2023-01-01", periods=3, tz="US/Eastern")

    df_tz1 = pd.DataFrame({"A": [1, 2, 3]}, index=dates1)
    df_tz2 = pd.DataFrame({"A": [1, 2, 3]}, index=dates2)

    compatible, info = check_dataframe_compatibility(df_tz1, df_tz2)
    assert (
        not compatible
    ), "DataFrames should be incompatible due to timezone mismatch"
    assert (
        "timezone mismatch" in info.lower()
    ), "Info should mention timezone mismatch"


def test_ensure_compatible_datetime_index():
    """Test the ensure_compatible_datetime_index function."""
    # Test with timezone-naive DatetimeIndex
    dates_naive = pd.date_range(start="2023-01-01", periods=3)
    df_naive = pd.DataFrame({"A": [1, 2, 3]}, index=dates_naive)

    # Convert to timezone-aware
    df_aware = ensure_compatible_datetime_index(df_naive)

    assert df_aware.index.tz is not None, "Index should now be timezone-aware"
    assert str(df_aware.index.tz) == "UTC", "Timezone should be UTC"

    # Test with already timezone-aware DatetimeIndex
    dates_aware = pd.date_range(start="2023-01-01", periods=3, tz="UTC")
    df_already_aware = pd.DataFrame({"A": [1, 2, 3]}, index=dates_aware)

    # Should remain unchanged
    df_result = ensure_compatible_datetime_index(df_already_aware)

    assert (
        df_result.index.tz is not None
    ), "Index should still be timezone-aware"
    assert str(df_result.index.tz) == "UTC", "Timezone should still be UTC"

    # Test with non-DatetimeIndex
    df_non_datetime = pd.DataFrame({"A": [1, 2, 3]})

    # Should remain unchanged
    df_result = ensure_compatible_datetime_index(df_non_datetime)

    assert not isinstance(
        df_result.index, pd.DatetimeIndex
    ), "Index should not be a DatetimeIndex"


def test_handle_nans_with_empty_dataframe():
    """Test that handle_nans properly handles empty DataFrames."""
    empty_df = pd.DataFrame()

    df_result, stats = handle_nans(empty_df)

    assert df_result.empty, "Result should still be an empty DataFrame"
    assert stats["rows_before"] == 0, "Stats should show 0 rows before"
    assert stats["rows_after"] == 0, "Stats should show 0 rows after"
    assert stats["rows_dropped"] == 0, "Stats should show 0 rows dropped"
    assert stats["pct_dropped"] == 0.0, "Stats should show 0% dropped"

    # Test with None
    df_result, stats = handle_nans(None)

    assert df_result is None, "Result should be None"
    assert stats["rows_before"] == 0, "Stats should show 0 rows before"
