import pytest
import pandas as pd
from strategy import validate_configuration  # To be implemented

def test_configuration_validation():
    """Test configuration validation against known patterns."""
    # Test case 1: Valid configuration
    valid_config = {
        'data': {
            'symbol': 'AAPL',
            'timeframe': '1d',
            'lookback_period': 30
        },
        'strategy': {
            'short_sma': 10,
            'long_sma': 30,
            'risk_ratio': 0.05
        }
    }
    
    # Should not raise any exceptions
    validate_configuration(valid_config)
    
    # Test case 2: Missing required section
    invalid_config1 = {
        'data': {
            'symbol': 'AAPL',
            'timeframe': '1d'
        },
        'strategy': {
            'short_sma': 10,
            'long_sma': 30
        }
    }
    
    # Should raise ValueError for missing lookback_period
    with pytest.raises(ValueError):
        validate_configuration(invalid_config1)
    
    # Test case 3: Invalid numeric values
    invalid_config2 = {
        'data': {
            'symbol': 'AAPL',
            'timeframe': '1d',
            'lookback_period': -10
        },
        'strategy': {
            'short_sma': 0,
            'long_sma': 50,
            'risk_ratio': 1.5
        }
    }
    
    # Should raise ValueError for invalid numeric values
    with pytest.raises(ValueError):
        validate_configuration(invalid_config2)
    
    # Test case 4: Invalid timeframe format
    invalid_config3 = {
        'data': {
            'symbol': 'AAPL',
            'timeframe': 'invalid',
            'lookback_period': 30
        },
        'strategy': {
            'short_sma': 10,
            'long_sma': 30,
            'risk_ratio': 0.05
        }
    }
    
    # Should raise ValueError for invalid timeframe
    with pytest.raises(ValueError):
        validate_configuration(invalid_config3)