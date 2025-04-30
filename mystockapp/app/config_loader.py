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
    
    # Validate required sections exist
    if not config.has_section('DEFAULT'):
        raise ValueError("Missing required [DEFAULT] section in config file")
    
    # Required parameters with type conversion
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
    for param, converter in required_params.items():
        try:
            if not config.has_option('DEFAULT', param):
                raise ValueError(f"Missing required parameter: {param}")
                
            result[param] = converter(config.get('DEFAULT', param))
        except ValueError as e:
            raise ValueError(f"Invalid value for {param}: {str(e)}")
    
    return result