import configparser
from datetime import datetime

def load_config(config_path='config.ini'):
    """
    Load and validate configuration from INI file.
    
    Args:
        config_path (str): Path to configuration file
        
    Returns:
        dict: Dictionary containing validated configuration parameters
        
    Raises:
        ValueError: If configuration is invalid or missing required parameters
    """
    config = configparser.ConfigParser()
    config.read(config_path)
    
    # Validate required parameters in [DEFAULT]
    required_params = {
        'ticker': str,
        'start_date': lambda x: datetime.strptime(x, '%Y-%m-%d').date().isoformat(),
        'end_date': lambda x: datetime.strptime(x, '%Y-%m-%d').date().isoformat(),
        'target_return_pct': float,
        'min_holding_days': int,
        'max_holding_days': int,
        'walk_forward_train_years': int,
        'walk_forward_test_months': int,
        'transaction_cost_pct': float,
        'initial_ma_short': int,
        'initial_ma_long': int
    }
    
    # Build config dictionary with type conversion
    result = {}
    defaults = config['DEFAULT']
    for param, converter in required_params.items():
        try:
            if param not in defaults:
                raise ValueError(f"Missing required parameter: {param}")
            result[param] = converter(defaults[param])
        except ValueError as e:
            raise ValueError(f"Invalid value for {param}: {str(e)}")
    
    return result