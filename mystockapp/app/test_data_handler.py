print("MODULE LEVEL: test_data_handler.py loaded by pytest")

import pytest
import pandas as pd
from data_handler import fetch_ohlcv_data, detect_missing_data, handle_missing_data, resample_ohlcv

def test_ohlcv_structure():
    # Test with verified parameters that return consistent data
    df = fetch_ohlcv_data("MSFT", "2023-06-01", "2023-06-30")

    # Verify required columns exist and are properly titled
    assert all(col in df.columns for col in ['Open', 'High', 'Low', 'Close', 'Volume'])
    # Verify no extra columns are present
    assert len(df.columns) == 5
    
    # Verify DateTimeIndex
    assert isinstance(df.index, pd.DatetimeIndex)
    
def test_resampling_validation():
    """Test that resampled data maintains correct structure and values."""
    # Create sample data with proper OHLCV structure
    sample_data = pd.DataFrame({
        'Open': [100, 101, 102],
        'High': [105, 106, 107],
        'Low': [95, 96, 97],
        'Close': [102, 103, 104],
        'Volume': [1000, 1500, 2000]
    }, index=pd.date_range('2023-01-01', periods=3, freq='D'))
    
    # Apply resampling
    resampled = resample_ohlcv(sample_data, 'W')
    print ("resampled:", resampled)
    
    # Verify structure
    assert isinstance(resampled.index, pd.DatetimeIndex)
    assert all(col in resampled.columns for col in ['Open', 'High', 'Low', 'Close', 'Volume'])
    
    # Verify values match OHLCV aggregation rules
    assert resampled.iloc[0]['Open'] == 100    # First value
    assert resampled.iloc[0]['High'] == 105    # Only first day (2023-01-01) in first weekly bin; pandas resample('W') aligns bins to week ending Sunday
    assert resampled.iloc[0]['Low'] == 95      # Min value
    assert resampled.iloc[0]['Close'] == 102   # Last value of the first day in the bin
    assert resampled.iloc[0]['Volume'] == 1000 # Only 2023-01-01 in first bin
    # Second bin: 2023-01-02 and 2023-01-03
    assert resampled.iloc[1]['Volume'] == 3500 # 1500 + 2000
    
    # Verify time series compression
    assert len(resampled) < len(sample_data)
    # Verify no missing columns
    assert len(resampled.columns) == 5

def test_data_fetching_error_handling():
    # Test with invalid ticker symbol
    with pytest.raises(ValueError) as exc_info:
        fetch_ohlcv_data("INVALIDTICKER123", "2020-01-01", "2020-01-31")
    
    # Verify error message contains relevant information
    assert "ticker" in str(exc_info.value).lower()
    assert "invalid" in str(exc_info.value).lower()

def test_fetch_ohlcv_data_invalid_ticker():
    """Test that fetch_ohlcv_data fails gracefully with invalid ticker symbols."""
    with pytest.raises(ValueError, match="No data found for the specified ticker"):
        fetch_ohlcv_data("INVALID_TICKER", start_date="2020-01-01", end_date="2020-01-31")

def test_detect_missing_data_identifies_gaps():
    """Test that detect_missing_data correctly identifies gaps in time series data."""
    # Create a DataFrame with a gap in dates
    dates = pd.date_range(start="2023-01-01", end="2023-01-05").drop(pd.Timestamp("2023-01-03"))
    data = pd.DataFrame({"Close": [100, 101, 102, 103]}, index=dates)

    with pytest.raises(ValueError, match="Missing data detected"):
        detect_missing_data(data)

def test_detect_missing_data_passes_with_no_gaps():
    """Test that detect_missing_data passes when no gaps exist."""
    dates = pd.date_range(start="2023-01-01", end="2023-01-05")
    data = pd.DataFrame({"Close": [100, 101, 102, 103, 104]}, index=dates)

    try:
        result = detect_missing_data(data)
        assert result is True
    except ValueError:
        pytest.fail("detect_missing_data raised unexpected ValueError")

import numpy as np # Add numpy import for NaN

def test_detect_missing_data_nan_values():
    """Test that detect_missing_data correctly identifies NaN values in data."""
    # Create a DataFrame with NaN values
    dates = pd.date_range(start="2023-01-01", periods=5)
    data = pd.DataFrame({"Close": [100, 101, np.nan, 103, 104]}, index=dates)

    with pytest.raises(ValueError, match="Missing data detected"):
        detect_missing_data(data)

def test_handle_missing_data_forward_fill():
    """Test that handle_missing_data correctly forward-fills NaN values."""
    # Create a DataFrame with NaN values
    dates = pd.date_range(start="2023-01-01", periods=5)
    data = pd.DataFrame({
        "Open": [100, 101, np.nan, 103, np.nan],
        "Close": [99, np.nan, 102, 102.5, 104]
    }, index=dates)

    # Define the expected DataFrame after forward fill
    expected_data = pd.DataFrame({
        "Open": [100.0, 101.0, 101.0, 103.0, 103.0], # NaN filled with 101, last NaN filled with 103
        "Close": [99.0, 99.0, 102.0, 102.5, 104.0] # NaN filled with 99
    }, index=dates)

    # Call the function (expected to fail as it doesn't exist yet)
    filled_data = handle_missing_data(data.copy()) # Use copy to avoid modifying original

    # Assert the filled data matches the expected data
    pd.testing.assert_frame_equal(filled_data, expected_data)

def test_resample_data_validation():
    """Test that resample_data maintains OHLC structure and index type."""
    # Create a sample daily DataFrame
    dates = pd.date_range(start="2023-01-01", periods=10, freq='D')
    data = pd.DataFrame({
        'Open': [100 + i for i in range(10)],
        'High': [105 + i for i in range(10)],
        'Low': [95 + i for i in range(10)],
        'Close': [102 + i for i in range(10)],
        'Volume': [1000 + i*100 for i in range(10)]
    }, index=dates)
    
    # Resample to weekly
    resampled = resample_ohlcv(data, rule='W')
    
    # Check if the resampled data has the correct frequency
    assert isinstance(resampled.index, pd.DatetimeIndex)
    # Check that the resampled data has the correct columns
    assert all(col in resampled.columns for col in ['Open', 'High', 'Low', 'Close', 'Volume'])
    # Check that the resampled data has fewer rows (weekly vs daily)
    assert len(resampled) < len(data)

def test_resample_ohlcv_3day():
    """Test that resample_ohlcv correctly resamples to 3-day bars and maintains OHLC consistency."""
    dates = pd.date_range(start="2023-01-01", periods=9, freq='D')
    data = pd.DataFrame({
        'Open': [10, 20, 30, 40, 50, 60, 70, 80, 90],
        'High': [15, 25, 35, 45, 55, 65, 75, 85, 95],
        'Low':  [5, 15, 25, 35, 45, 55, 65, 75, 85],
        'Close':[12, 22, 32, 42, 52, 62, 72, 82, 92],
        'Volume':[100, 200, 300, 400, 500, 600, 700, 800, 900]
    }, index=dates)

    resampled = resample_ohlcv(data, rule='3D')

    # There should be 3 rows (each 3 days)
    assert len(resampled) == 3
    # Check OHLC consistency for first bar (2023-01-01 to 2023-01-03)
    assert resampled.iloc[0]['Open'] == 10
    assert resampled.iloc[0]['High'] == 35
    assert resampled.iloc[0]['Low'] == 5
    assert resampled.iloc[0]['Close'] == 32
    assert resampled.iloc[0]['Volume'] == 100 + 200 + 300
    # Check OHLC consistency for second bar (2023-01-04 to 2023-01-06)
    assert resampled.iloc[1]['Open'] == 40
    assert resampled.iloc[1]['High'] == 65
    assert resampled.iloc[1]['Low'] == 35
    assert resampled.iloc[1]['Close'] == 62
    assert resampled.iloc[1]['Volume'] == 400 + 500 + 600
    # Check OHLC consistency for third bar (2023-01-07 to 2023-01-09)
    assert resampled.iloc[2]['Open'] == 70
    assert resampled.iloc[2]['High'] == 95
    assert resampled.iloc[2]['Low'] == 65
    assert resampled.iloc[2]['Close'] == 92
    assert resampled.iloc[2]['Volume'] == 700 + 800 + 900
