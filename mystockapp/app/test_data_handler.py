import pytest
import pandas as pd
from data_handler import fetch_ohlcv_data, detect_missing_data

def test_ohlcv_structure():
    # Test with verified parameters that return consistent data
    df = fetch_ohlcv_data("MSFT", "2023-06-01", "2023-06-30")

    # Verify required columns exist and are properly titled
    assert all(col in df.columns for col in ['Open', 'High', 'Low', 'Close', 'Volume'])
    # Verify no extra columns are present
    assert len(df.columns) == 5
    
    # Verify DateTimeIndex
    assert isinstance(df.index, pd.DatetimeIndex)
    
    # Verify no missing columns
    assert len(df.columns) == 5

if __name__ == "__main__":
    test_ohlcv_structure()
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
from data_handler import handle_missing_data # Import the function to be tested

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