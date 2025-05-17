"""
Test scenario: Feature Generation with Empty or Invalid Input Data

This test verifies that the FeatureFactory handles edge cases like empty DataFrames
or non-numeric data gracefully, as mentioned in the requirements.
"""

import pytest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import sys
import os
import logging

# Add the src directory to path so we can import modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.feature_factory import FeatureFactory
from src.backtester import run_backtest

# Setup logging for test
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def test_feature_factory_with_empty_dataframe():
    """Test that FeatureFactory handles an empty DataFrame gracefully."""
    # Create an empty DataFrame with required columns
    columns = ["Open", "High", "Low", "Close", "Volume"]
    empty_df = pd.DataFrame(columns=columns)

    # Instantiate FeatureFactory with the empty DataFrame
    with pytest.raises(Exception) as excinfo:
        factory = FeatureFactory(empty_df)
        features_df = factory.generate_features()

    # We expect some kind of error (ValueError or similar)
    logger.info(f"Empty DataFrame raised: {str(excinfo.value)}")
    assert (
        "empty" in str(excinfo.value).lower()
        or "no data" in str(excinfo.value).lower()
    ), "Should raise error for empty DataFrame"


def test_feature_factory_with_non_numeric_data():
    """Test that FeatureFactory handles non-numeric data appropriately."""
    # Create a DataFrame with non-numeric values in OHLCV columns
    dates = pd.date_range(start=datetime.now(), periods=10, freq="D")

    # Mix of numeric and non-numeric data
    df = pd.DataFrame(
        {
            "Open": [100, 101, "bad", 103, 104, 105, 106, 107, 108, 109],
            "High": [105, 106, 107, "error", 109, 110, 111, 112, 113, 114],
            "Low": [95, 96, 97, 98, "invalid", 100, 101, 102, 103, 104],
            "Close": [102, 103, 104, 105, 106, "wrong", 108, 109, 110, 111],
            "Volume": [
                10000,
                "N/A",
                10200,
                10300,
                10400,
                10500,
                10600,
                10700,
                10800,
                10900,
            ],
        },
        index=dates,
    )

    # Attempt to instantiate FeatureFactory with non-numeric data
    with pytest.raises(Exception) as excinfo:
        factory = FeatureFactory(df)
        features_df = factory.generate_features()

    # We expect a data type error
    logger.info(f"Non-numeric data raised: {str(excinfo.value)}")
    assert (
        "convert" in str(excinfo.value).lower()
        or "numeric" in str(excinfo.value).lower()
        or "type" in str(excinfo.value).lower()
    ), "Should raise error for non-numeric data"


def test_feature_factory_with_single_row():
    """Test that FeatureFactory handles a DataFrame with only one row appropriately."""
    # Create a DataFrame with just one row
    dates = pd.date_range(start=datetime.now(), periods=1, freq="D")
    df = pd.DataFrame(
        {
            "Open": [100],
            "High": [105],
            "Low": [95],
            "Close": [102],
            "Volume": [10000],
        },
        index=dates,
    )

    # We expect this to fail since most technical indicators need multiple data points
    with pytest.raises(Exception) as excinfo:
        factory = FeatureFactory(df)
        features_df = factory.generate_features()

    logger.info(f"Single row DataFrame raised: {str(excinfo.value)}")
    assert (
        "window" in str(excinfo.value).lower()
        or "data" in str(excinfo.value).lower()
    ), "Should raise error for single row DataFrame"


def test_backtest_with_invalid_dataframe():
    """Test that run_backtest handles an invalid DataFrame appropriately."""
    # Create an empty DataFrame with required columns
    empty_df = pd.DataFrame(columns=["Close", "buy_signal", "sell_signal"])

    # Run backtest with empty DataFrame
    results = run_backtest(
        empty_df,
        initial_capital=100000.0,
        commission_fixed=20.0,
        commission_pct=0.0003,
        slippage_pct=0.001,
        position_size_pct=0.25,
    )

    # We expect it to return None or raise an error
    assert results is None, "Backtest should return None for empty DataFrame"


def test_backtest_with_missing_columns():
    """Test that run_backtest handles a DataFrame with missing required columns."""
    # Create a DataFrame without required signal columns
    dates = pd.date_range(start=datetime.now(), periods=10, freq="D")
    df = pd.DataFrame(
        {
            "Open": np.random.randn(10) + 100,
            "High": np.random.randn(10) + 105,
            "Low": np.random.randn(10) + 95,
            "Close": np.random.randn(10) + 102,
            "Volume": np.random.randint(10000, 20000, 10),
            # Missing 'buy_signal' and 'sell_signal' columns
        },
        index=dates,
    )

    # Run backtest with DataFrame missing required columns
    results = run_backtest(
        df,
        initial_capital=100000.0,
        commission_fixed=20.0,
        commission_pct=0.0003,
        slippage_pct=0.001,
        position_size_pct=0.25,
    )

    # We expect it to return None or raise an error
    assert (
        results is None
    ), "Backtest should return None for DataFrame with missing columns"


def test_feature_factory_with_empty_dataframe():
    """
    Test FeatureFactory behavior with an empty DataFrame as input.

    The factory should raise a ValueError when attempting to generate features
    from an empty DataFrame.
    """
    # Create an empty DataFrame with the required columns
    empty_df = pd.DataFrame(columns=["Open", "High", "Low", "Close", "Volume"])

    # Create a FeatureFactory instance with the empty DataFrame
    with pytest.raises(ValueError) as excinfo:
        factory = FeatureFactory(empty_df)
        factory.generate_features()

    # Verify error message mentions empty data
    assert "empty data" in str(excinfo.value).lower()


def test_feature_factory_with_non_numeric_data():
    """
    Test FeatureFactory behavior with non-numeric data in OHLCV columns.

    The factory should raise a ValueError when attempting to generate features
    from data with non-numeric values.
    """
    # Create a DataFrame with non-numeric values in some OHLCV cells
    dates = pd.date_range(start="2023-01-01", periods=30, freq="B")

    # Create a DataFrame with proper data
    data = pd.DataFrame(
        {
            "Open": np.random.randn(30) * 10 + 100,
            "High": np.random.randn(30) * 10 + 105,
            "Low": np.random.randn(30) * 10 + 95,
            "Close": np.random.randn(30) * 10 + 100,
            "Volume": np.random.randint(1000, 100000, 30),
        },
        index=dates,
    )

    # Insert non-numeric values in some cells
    data.loc[data.index[5], "Close"] = "NaN"
    data.loc[data.index[10], "Open"] = "error"
    data.loc[data.index[15], "High"] = None

    # Create a FeatureFactory instance with the problematic DataFrame
    with pytest.raises((ValueError, TypeError)) as excinfo:
        factory = FeatureFactory(data)
        factory.generate_features()

    # Verify error message mentions data type issue
    assert any(
        keyword in str(excinfo.value).lower()
        for keyword in [
            "type",
            "numeric",
            "convert",
            "cast",
            "invalid",
            "data",
        ]
    )


def test_feature_factory_insufficient_data():
    """
    Test FeatureFactory behavior when input data has fewer rows than needed for calculation.

    The factory should raise a ValueError when the data is too short for the indicators.
    """
    # Create a small DataFrame with only 5 rows
    dates = pd.date_range(start="2023-01-01", periods=5, freq="B")

    data = pd.DataFrame(
        {
            "Open": np.random.randn(5) * 10 + 100,
            "High": np.random.randn(5) * 10 + 105,
            "Low": np.random.randn(5) * 10 + 95,
            "Close": np.random.randn(5) * 10 + 100,
            "Volume": np.random.randint(1000, 100000, 5),
        },
        index=dates,
    )

    # Try to create 200-day SMA which requires at least 200 data points
    custom_params = {"sma": {"windows": [5, 10, 20, 50, 200]}}

    # Create a FeatureFactory instance with the insufficient data
    with pytest.raises(ValueError) as excinfo:
        factory = FeatureFactory(data, indicator_params=custom_params)
        factory.generate_features()

    # Verify error message mentions insufficient data
    assert any(
        keyword in str(excinfo.value).lower()
        for keyword in [
            "insufficient",
            "not enough",
            "too few",
            "minimum",
            "required",
        ]
    )


def test_feature_factory_missing_columns():
    """
    Test FeatureFactory behavior when input data is missing required columns.

    The factory should raise a ValueError when required columns are missing.
    """
    # Create a DataFrame missing some required columns
    dates = pd.date_range(start="2023-01-01", periods=30, freq="B")

    # Missing 'High' and 'Volume' columns
    data = pd.DataFrame(
        {
            "Open": np.random.randn(30) * 10 + 100,
            "Low": np.random.randn(30) * 10 + 95,
            "Close": np.random.randn(30) * 10 + 100,
        },
        index=dates,
    )

    # Create a FeatureFactory instance with the missing columns
    with pytest.raises(ValueError) as excinfo:
        factory = FeatureFactory(data)
        factory.generate_features()

    # Verify error message mentions missing columns
    assert "missing" in str(excinfo.value).lower()
    assert any(col in str(excinfo.value) for col in ["High", "Volume"])


def test_feature_factory_with_nans():
    """
    Test FeatureFactory handling of NaN values in the input data.
    """
    # Create a DataFrame with some NaN values
    dates = pd.date_range(start="2023-01-01", periods=30, freq="B")

    # Create data with NaNs
    data = pd.DataFrame(
        {
            "Open": np.random.randn(30) * 10 + 100,
            "High": np.random.randn(30) * 10 + 105,
            "Low": np.random.randn(30) * 10 + 95,
            "Close": np.random.randn(30) * 10 + 100,
            "Volume": np.random.randint(1000, 100000, 30),
        },
        index=dates,
    )

    # Insert NaN values
    data.loc[data.index[5], "Close"] = np.nan
    data.loc[data.index[10], "Open"] = np.nan
    data.loc[data.index[15], "High"] = np.nan

    # Test with drop_na=False
    factory = FeatureFactory(data)
    result_with_nans = factory.generate_features(drop_na=False)

    # Should have NaNs in the result
    assert result_with_nans.isna().any().any()

    # Test with drop_na=True
    factory = FeatureFactory(data)
    result_without_nans = factory.generate_features(drop_na=True)

    # Should have no NaNs in the result
    assert not result_without_nans.isna().any().any()

    # Should have fewer rows due to NaN dropping
    assert len(result_without_nans) < len(result_with_nans)


if __name__ == "__main__":
    pytest.main(["-xvs", __file__])
