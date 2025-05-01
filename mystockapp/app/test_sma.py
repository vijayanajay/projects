import pytest
import pandas as pd
import numpy as np
from strategy import calculate_sma  # To be implemented

def test_sma_calculation():
    """Test SMA calculation against known benchmarks."""
    # Test case 1: Simple case with known SMA values
    data = pd.Series([1, 2, 3, 4, 5])
    expected_sma = pd.Series([1.0, 1.5, 2.5, 3.5, 4.5])  # 2-period SMA
    
    result = calculate_sma(data, period=2)
    
    # Use numpy testing for floating point comparison
    np.testing.assert_array_almost_equal(result.values, expected_sma.values, decimal=4)
    
    # Test case 2: Edge case - all values same
    constant_data = pd.Series([5, 5, 5, 5, 5])
    expected_constant_sma = pd.Series([5.0, 5.0, 5.0, 5.0, 5.0])
    
    result_constant = calculate_sma(constant_data, period=3)
    np.testing.assert_array_almost_equal(result_constant.values, expected_constant_sma.values, decimal=4)
    
    # Test case 3: Single value
    single_data = pd.Series([10])
    expected_single = pd.Series([10.0])
    
    result_single = calculate_sma(single_data, period=2)
    np.testing.assert_array_almost_equal(result_single.values, expected_single.values, decimal=4)