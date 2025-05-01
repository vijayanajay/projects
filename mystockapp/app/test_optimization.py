import pytest
import pandas as pd
import numpy as np
from strategy import StrategyOptimizer  # To be implemented

def test_strategy_optimization():
    """Test strategy optimization against known patterns."""
    # Create sample price data
    dates = pd.date_range('2023-01-01', periods=100, freq='D')
    prices = pd.Series(np.sin(np.linspace(0, 4*np.pi, 100)) * 10 + 100, index=dates)
    
    # Test case 1: Basic parameter optimization
    config_template = {
        'data': {
            'symbol': 'TEST',
            'timeframe': '1d',
            'lookback_period': 30
        },
        'strategy': {
            'short_sma': 3,  # Will be optimized
            'long_sma': 5,   # Will be optimized
            'risk_ratio': 0.05
        }
    }
    
    # Define parameter ranges for optimization
    param_ranges = {
        'strategy.short_sma': range(2, 10),
        'strategy.long_sma': range(5, 20)
    }
    
    optimizer = StrategyOptimizer(prices, config_template, param_ranges)
    results = optimizer.optimize()
    
    # Verify optimization output structure
    assert 'best_params' in results
    assert 'best_score' in results
    assert 'all_results' in results
    
    best_params = results['best_params']
    best_score = results['best_score']
    
    # Verify parameter types
    assert isinstance(best_params['strategy']['short_sma'], int)
    assert isinstance(best_params['strategy']['long_sma'], int)
    
    # Test case 2: Empty price data
    empty_prices = pd.Series([], index=pd.DatetimeIndex([]))
    
    empty_optimizer = StrategyOptimizer(empty_prices, config_template, param_ranges)
    
    with pytest.raises(ValueError):
        empty_optimizer.optimize()
    
    # Test case 3: Invalid parameter ranges
    invalid_ranges = {
        'strategy.short_sma': [0, 1],  # Invalid values
        'strategy.long_sma': range(5, 20)
    }
    
    with pytest.raises(ValueError):
        StrategyOptimizer(prices, config_template, invalid_ranges)
    
    # Test case 4: Single parameter range
    single_range = {
        'strategy.short_sma': [5],  # Only one value
        'strategy.long_sma': range(5, 20)
    }
    
    single_optimizer = StrategyOptimizer(prices, config_template, single_range)
    single_results = single_optimizer.optimize()
    
    # Should return the single parameter value
    assert single_results['best_params']['strategy']['short_sma'] == 5
    
    # Test case 5: Negative returns scenario
    # Create price data with consistent downward trend
    negative_prices = pd.Series(100 - np.linspace(0, 20, 100), index=dates)
    
    negative_optimizer = StrategyOptimizer(negative_prices, config_template, param_ranges)
    negative_results = negative_optimizer.optimize()
    
    # Should still find best parameters even with negative returns
    assert 'best_params' in negative_results
    assert negative_results['best_score'] <= 0  # Negative returns

def test_parameter_range_validation_fails_on_invalid_values():
    """Test that StrategyOptimizer raises ValueError for invalid parameter ranges (zero/negative values)."""
    prices = pd.Series([100, 101, 102], index=pd.date_range('2023-01-01', periods=3))
    config_template = {
        'data': {'symbol': 'AAPL', 'timeframe': '1d', 'lookback_period': 10},
        'strategy': {'short_sma': 2, 'long_sma': 3, 'risk_ratio': 0.1}
    }
    # Invalid: zero and negative values in parameter ranges
    invalid_param_ranges = {
        'strategy.short_sma': [0, -1, 2],
        'strategy.long_sma': [3, 4]
    }
    with pytest.raises(ValueError):
        StrategyOptimizer(prices, config_template, invalid_param_ranges)