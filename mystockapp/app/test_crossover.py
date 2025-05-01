import pytest
import pandas as pd
import numpy as np
from strategy import generate_crossover_signals  # To be implemented

def test_crossover_signal_generation():
    """Test crossover signal generation against known patterns."""
    # Test case 1: Simple crossover pattern
    short_sma = pd.Series([1, 1.5, 2, 2.5, 3, 3.5, 4])
    long_sma = pd.Series([1, 1.2, 1.4, 1.6, 1.8, 2, 2.2])
    
    expected_signals = pd.Series([0, 1, 1, 1, 1, 1, 1])  # 1 for buy, 0 for hold
    
    result = generate_crossover_signals(short_sma, long_sma)
    
    # Verify signals match expected pattern
    pd.testing.assert_series_equal(result, expected_signals, check_dtype=False)
    
    # Test case 2: No crossover pattern
    flat_short = pd.Series([2, 2, 2, 2, 2])
    flat_long = pd.Series([2, 2, 2, 2, 2])
    
    expected_flat = pd.Series([0, 0, 0, 0, 0])
    
    result_flat = generate_crossover_signals(flat_short, flat_long)
    pd.testing.assert_series_equal(result_flat, expected_flat, check_dtype=False)
    
    # Test case 3: Multiple crossovers
    oscillating_short = pd.Series([1, 1.5, 1, 1.5, 1])
    oscillating_long = pd.Series([1, 1, 1, 1, 1])
    
    expected_oscillating = pd.Series([0, 1, 0, 1, 0])
    
    result_oscillating = generate_crossover_signals(oscillating_short, oscillating_long)
    pd.testing.assert_series_equal(result_oscillating, expected_oscillating, check_dtype=False)