import pytest
import pandas as pd
import numpy as np
from indicator_calculator import calculate_volume_ma, calculate_rsi, calculate_adx, calculate_macd, calculate_bollinger_bands

def test_calculate_volume_ma():
    data = pd.Series([1, 2, 3, 4, 5])
    result = calculate_volume_ma(data, period=3)
    # The rolling mean for period=3: [1, 1.5, 2, 3, 4]
    expected = pd.Series([1, 1.5, 2, 3, 4])
    pd.testing.assert_series_equal(result.round(4), expected.round(4))

def test_calculate_rsi():
    data = pd.Series([45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60])
    result = calculate_rsi(data, period=14)
    # For a strictly increasing series, RSI should be 100 after warmup
    assert result.iloc[-1] > 99

def test_calculate_adx():
    high = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    low = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    close = pd.Series([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5])
    adx = calculate_adx(high, low, close, period=14)
    # ADX should be a float series, last value should be finite
    assert np.isfinite(adx.iloc[-1])

def test_calculate_macd():
    data = pd.Series(np.arange(1, 51))
    macd, signal, hist = calculate_macd(data)
    # MACD of a ramp should be positive, signal should be positive
    assert macd.iloc[-1] > 0
    assert signal.iloc[-1] > 0
    assert isinstance(hist, pd.Series)

def test_calculate_bollinger_bands():
    data = pd.Series([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    upper, middle, lower = calculate_bollinger_bands(data, period=20)
    # Bands should be same length as input
    assert len(upper) == len(data)
    assert len(middle) == len(data)
    assert len(lower) == len(data)
    # Middle band should equal SMA
    np.testing.assert_almost_equal(middle.iloc[-1], np.mean(data), decimal=4) 