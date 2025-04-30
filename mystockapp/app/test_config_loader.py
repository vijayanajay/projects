import tempfile
import configparser
from config_loader import load_config

def test_valid_config():
    # Create temporary config file
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        config = configparser.ConfigParser()
        config['DEFAULT'] = {
            'ticker': 'AAPL',
            'start_date': '2020-01-01',
            'end_date': '2020-01-31',
            'target_return_pct': '3.0',
            'min_holding_days': '10',
            'max_holding_days': '30',
            'walk_forward_train_years': '1',
            'walk_forward_test_months': '3',
            'transaction_cost_pct': '0.1',
            'initial_ma_short': '9',
            'initial_ma_long': '21'
        }
        config.write(f)
        f_path = f.name

    try:
        # Debug: Print the contents of the config file created
        with open(f_path, 'r') as debug_f:
            print("\n[DEBUG] Contents of test config file:")
            print(debug_f.read())
        # Test valid config
        config = load_config(f_path)
        
        # Verify all parameters exist and have correct types
        assert config['ticker'] == 'AAPL'
        assert config['start_date'] == '2020-01-01'
        assert config['end_date'] == '2020-01-31'
        assert isinstance(config['target_return_pct'], float)
        assert isinstance(config['min_holding_days'], int)
        assert isinstance(config['max_holding_days'], int)
        assert isinstance(config['walk_forward_train_years'], int)
        assert isinstance(config['walk_forward_test_months'], int)
        assert isinstance(config['transaction_cost_pct'], float)
        assert isinstance(config['initial_ma_short'], int)
        assert isinstance(config['initial_ma_long'], int)
    finally:
        import os
        os.unlink(f_path)

def test_missing_required_section():
    # Test missing [DEFAULT] section
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        f.write('[OTHER]\nticker=AAPL')
        f_path = f.name
    
    try:
        try:
            load_config(f_path)
            assert False, "Expected ValueError for missing DEFAULT section"
        except ValueError as e:
            # Now we expect a missing required parameter error, since [DEFAULT] is not present
            assert "Missing required parameter" in str(e)
    finally:
        import os
        os.unlink(f_path)

def test_missing_required_parameter():
    # Test missing required parameter
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        # Provide all but one required parameter, to ensure the error is for missing parameter, not missing section
        f.write('[DEFAULT]\n')
        f.write('ticker=AAPL\n')
        f.write('start_date=2020-01-01\n')
        f.write('end_date=2020-01-31\n')
        f.write('target_return_pct=3.0\n')
        f.write('min_holding_days=10\n')
        f.write('max_holding_days=30\n')
        f.write('walk_forward_train_years=1\n')
        f.write('walk_forward_test_months=3\n')
        f.write('transaction_cost_pct=0.1\n')
        f.write('initial_ma_short=9\n')
        # Omit 'initial_ma_long' to trigger missing parameter error
        f.flush()
        f_path = f.name
    
    try:
        try:
            load_config(f_path)
            assert False, "Expected ValueError for missing parameter"
        except ValueError as e:
            assert "Missing required parameter" in str(e)
    finally:
        import os
        os.unlink(f_path)

if __name__ == "__main__":
    test_valid_config()
    test_missing_required_section()
    test_missing_required_parameter()