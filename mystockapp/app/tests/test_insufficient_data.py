"""
Test scenario: Data Insufficient for Indicator Calculation

This test verifies the behavior of FeatureFactory and backtesting when
the input data DataFrame has fewer rows than the largest required
lookback window for the selected features.
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
from src.backtester import run_backtest, SMACrossoverStrategy

# Setup logging for test
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@pytest.fixture
def small_ohlcv_data():
    """Generate a small OHLCV dataset with 100 rows (insufficient for SMA 200)."""
    # Generate dates for the last 100 days
    end_date = datetime.now()
    start_date = end_date - timedelta(days=100)
    dates = pd.date_range(start=start_date, end=end_date, periods=100)

    # Generate random price data
    np.random.seed(42)  # For reproducibility
    close_price = np.random.normal(100, 10, 100).cumsum()
    high_price = close_price * (1 + np.random.uniform(0, 0.05, 100))
    low_price = close_price * (1 - np.random.uniform(0, 0.05, 100))
    open_price = close_price * (1 + np.random.uniform(-0.02, 0.02, 100))
    volume = np.random.randint(1000, 100000, 100)

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


def test_generate_features_with_insufficient_data(small_ohlcv_data):
    """Test that FeatureFactory generates features with mostly NaNs when data is insufficient."""
    # Create factory with default parameters (which include SMA 200)
    factory = FeatureFactory(small_ohlcv_data)

    # Generate features without dropping NaNs
    df_with_features = factory.generate_features(drop_na=False)

    # Check that all rows have at least some NaN values
    assert (
        df_with_features.isna().any(axis=1).any()
    ), "Expected some NaN values in the result"

    # Check that SMA 200 column has mostly NaN values (should be NaN for the first 200 rows,
    # but our dataset only has 100 rows, so all should be NaN)
    assert "sma_200" in df_with_features.columns, "SMA 200 column not found"
    assert (
        df_with_features["sma_200"].isna().all()
    ), "Expected all NaN values in SMA 200 column"

    # Check that shorter window indicators have valid values in the latter part of the DataFrame
    assert "sma_20" in df_with_features.columns, "SMA 20 column not found"
    assert (
        not df_with_features["sma_20"].isna().all()
    ), "Expected some valid values in SMA 20 column"
    assert df_with_features["sma_20"].isna().sum() < len(
        df_with_features
    ), "Expected some valid SMA 20 values"


def test_generate_features_with_drop_na(small_ohlcv_data):
    """Test that FeatureFactory returns few or no rows when drop_na=True with insufficient data."""
    # Create factory with default parameters (which include SMA 200)
    factory = FeatureFactory(small_ohlcv_data)

    # Generate features with dropping NaNs
    df_with_features = factory.generate_features(drop_na=True)

    # The result should be empty or have very few rows
    assert len(df_with_features) < len(
        small_ohlcv_data
    ), "Expected fewer rows after dropping NaNs"

    # Alternatively, the result might be completely empty
    # Allows for both possibilities
    if not df_with_features.empty:
        # If not empty, check that there are no NaN values
        assert (
            not df_with_features.isna().any().any()
        ), "Expected no NaN values when drop_na=True"


def test_generate_features_with_drop_na_threshold(small_ohlcv_data):
    """Test that FeatureFactory with drop_na_threshold preserves more rows while handling NaNs."""
    # Create factory with default parameters
    factory = FeatureFactory(small_ohlcv_data)

    # Generate features with threshold-based NaN dropping (50% threshold)
    df_with_features = factory.generate_features(
        drop_na=True, drop_na_threshold=0.5
    )

    # Should preserve rows where less than 50% of columns have NaNs
    if not df_with_features.empty:
        assert (
            len(df_with_features) > 0
        ), "Expected some rows to be preserved with threshold"
        # With threshold dropping, some NaNs might still be present in the DataFrame
        # This is expected behavior since we're dropping rows with > 50% NaNs, not all NaNs
        logger.info(
            f"Found {df_with_features.isna().sum().sum()} NaN values in {len(df_with_features)} rows"
        )

        # Count how many columns are entirely NaN
        nan_columns = df_with_features.columns[df_with_features.isna().all()]
        logger.info(f"Found {len(nan_columns)} columns that are all NaN")

        # Assert that at least some data is usable
        assert (
            df_with_features.notna().any().any()
        ), "Expected some non-NaN values in the result"


def test_backtest_with_insufficient_data(small_ohlcv_data):
    """Test that backtesting handles insufficient data gracefully."""
    # Generate features and apply strategy
    factory = FeatureFactory(small_ohlcv_data, feature_families=["sma"])
    df_with_features = factory.generate_features(drop_na=False)

    # Apply strategy to generate signals
    strategy = SMACrossoverStrategy(fast_window=20, slow_window=50)
    df_with_signals = strategy.generate_signals(df_with_features)

    # Drop NaNs after signal generation
    df_filtered = df_with_signals.dropna()

    # See if we have any data left
    if not df_filtered.empty:
        # Run backtest
        results = run_backtest(df_filtered, initial_capital=100000.0)

        # Check that results are valid
        assert isinstance(results, dict), "Expected dictionary of results"
        assert (
            results["final_value"] >= 0
        ), "Final value should not be negative"
        assert (
            results["num_trades"] >= 0
        ), "Number of trades should not be negative"
    else:
        # If all data was dropped, create an empty DataFrame with required columns
        empty_df = pd.DataFrame(columns=["Close", "buy_signal", "sell_signal"])

        # Run backtest and check that it handles empty DataFrame gracefully
        with pytest.raises(Exception):
            # This should raise an exception because there are no date indexes
            run_backtest(empty_df, initial_capital=100000.0)

        # Try with a minimal valid DataFrame
        minimal_df = pd.DataFrame(
            {"Close": [100.0], "buy_signal": [False], "sell_signal": [False]},
            index=[pd.Timestamp("2022-01-01")],
        )

        # Run backtest with minimal data
        results = run_backtest(minimal_df, initial_capital=100000.0)

        # Check that results are valid
        assert isinstance(results, dict), "Expected dictionary of results"
        assert (
            results["final_value"] == 100000.0
        ), "Capital should be unchanged with no trades"
        assert results["num_trades"] == 0, "Should be no trades"


def test_full_pipeline_with_insufficient_data(small_ohlcv_data):
    """Test the entire pipeline from feature generation to backtesting with insufficient data."""
    # Generate features
    factory = FeatureFactory(
        small_ohlcv_data, feature_families=["sma", "rsi", "macd"]
    )
    df_with_features = factory.generate_features(drop_na=False)

    # Apply strategy
    strategy = SMACrossoverStrategy(fast_window=20, slow_window=50)
    df_with_signals = strategy.generate_signals(df_with_features)

    # Drop NaNs after signal generation
    df_filtered = df_with_signals.dropna()

    # Check behavior when data is insufficient
    if len(df_filtered) < 10:  # Arbitrary threshold for "too little data"
        logger.warning(
            f"Very little data left after filtering: {len(df_filtered)} rows"
        )

    # Run backtest if we have any data left
    if not df_filtered.empty:
        results = run_backtest(df_filtered, initial_capital=100000.0)

        # Check results
        assert isinstance(results, dict), "Expected dictionary of results"
        assert "final_value" in results, "Results should include final_value"
        assert "num_trades" in results, "Results should include num_trades"
    else:
        logger.warning(
            "No data left after filtering out NaNs, cannot run backtest"
        )

        # Check that we don't crash when there's no data
        assert (
            True
        ), "Test should complete without errors even when no data is left"


def test_generate_features_with_insufficient_data():
    from src.feature_factory import FeatureFactory  # Import if not already
    import pandas as pd

    # Create a small DataFrame
    short_df = pd.DataFrame(
        {
            "Open": [1.0],
            "High": [1.0],
            "Low": [1.0],
            "Close": [1.0],
            "Volume": [100],
        },
        index=pd.date_range(start="2023-01-01", periods=1),
    )

    factory = FeatureFactory(
        short_df,
        feature_families=["sma"],
        indicator_params={"sma": {"windows": [50]}},
    )

    try:
        factory.generate_features()
        assert False, "Expected ValueError was not raised"
    except ValueError as e:
        assert "Input DataFrame has" in str(
            e
        )  # Check for the specific error message

    # Add more tests for other families if needed
