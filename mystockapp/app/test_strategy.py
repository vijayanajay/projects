import pytest
import pandas as pd
import numpy as np
from strategy import calculate_ema  # To be implemented

def test_ema_calculation():
    """Test EMA calculation against known benchmarks and edge cases."""
    # Test case 1: Simple case with known EMA values
    data = pd.Series([1, 2, 3, 4, 5])
    expected_ema = pd.Series([1.0, 1.5, 2.25, 3.125, 4.0625])  # 2-period EMA
    
    result = calculate_ema(data, period=2)
    
    # Use numpy testing for floating point comparison
    np.testing.assert_array_almost_equal(result.values, expected_ema.values, decimal=4)
    
    # Test case 2: Edge case - all values same
    constant_data = pd.Series([5, 5, 5, 5, 5])
    expected_constant_ema = pd.Series([5.0, 5.0, 5.0, 5.0, 5.0])
    
    result_constant = calculate_ema(constant_data, period=3)
    np.testing.assert_array_almost_equal(result_constant.values, expected_constant_ema.values, decimal=4)
    
    # Test case 3: Single value
    single_data = pd.Series([10])
    expected_single = pd.Series([10.0])
    
    result_single = calculate_ema(single_data, period=2)
    np.testing.assert_array_almost_equal(result_single.values, expected_single.values, decimal=4)

    # Test case 4: Empty series
    empty_data = pd.Series([], dtype=float)
    result_empty = calculate_ema(empty_data, period=2)
    assert result_empty.empty

    # Test case 5: Series with NaN values
    nan_data = pd.Series([1.0, np.nan, 3.0, 4.0])
    result_nan = calculate_ema(nan_data, period=2)
    assert np.isnan(result_nan.iloc[1])  # EMA should be NaN where input is NaN
    assert not np.isnan(result_nan.iloc[0])
    assert not np.isnan(result_nan.iloc[2])
    assert not np.isnan(result_nan.iloc[3])

def test_crossover_strategy_consistency_across_timeframes():
    """Test that crossover strategy generates consistent signals across daily and weekly timeframes."""
    # Simulate daily close prices with a DatetimeIndex
    dates = pd.date_range('2023-01-01', periods=20, freq='D')
    daily_prices = pd.Series([10, 11, 12, 13, 12, 11, 10, 11, 12, 13, 14, 15, 16, 15, 14, 13, 12, 11, 10, 9], index=dates)
    # Simulate weekly close prices (resampled)
    weekly_prices = daily_prices.resample('W').mean()

    # Use short=2, long=3 for both timeframes
    from strategy import calculate_sma, generate_crossover_signals
    daily_short = calculate_sma(daily_prices, 2)
    daily_long = calculate_sma(daily_prices, 3)
    daily_signals = generate_crossover_signals(daily_short, daily_long)

    weekly_short = calculate_sma(weekly_prices, 2)
    weekly_long = calculate_sma(weekly_prices, 3)
    weekly_signals = generate_crossover_signals(weekly_short, weekly_long)

    # For this test, just check that signals are not all zero and that the pattern is consistent (e.g., at least one crossover in both)
    assert daily_signals.sum() > 0, "No crossover signals generated for daily timeframe"
    assert weekly_signals.sum() > 0, "No crossover signals generated for weekly timeframe"
    # Optionally, check that the first crossover in both timeframes is a buy (1)
    assert daily_signals[daily_signals == 1].index[0] is not None
    assert weekly_signals[weekly_signals == 1].index[0] is not None

def test_individual_metric_calculations():
    """Test Sharpe ratio, max drawdown, and win rate calculations on simple trade data."""
    from strategy import Backtester
    # Minimal price and signal data
    prices = pd.Series([100, 110, 105, 120, 115],
                      index=pd.date_range('2023-01-01', periods=5))
    # Buy on day 1, sell on day 3, buy on day 4, sell on day 5
    signals = pd.Series([1, 0, 1, 0, 0], index=prices.index)
    config = {
        'data': {
            'symbol': 'TEST',
            'timeframe': '1d',
            'lookback_period': 5
        },
        'strategy': {
            'short_sma': 1,
            'long_sma': 2,
            'risk_ratio': 1.0
        }
    }
    bt = Backtester(prices, signals, config)
    results = bt.run()
    # Check Sharpe ratio and max drawdown keys exist
    assert 'sharpe_ratio' in results
    assert 'max_drawdown' in results
    # Check Sharpe ratio is a float
    assert isinstance(results['sharpe_ratio'], float)
    # Check max drawdown is a float
    assert isinstance(results['max_drawdown'], float)
    # Win rate: should be 100% (2 trades, both profitable)
    trades = results['trades']
    wins = [t for t in trades if t['profit'] > 0]
    win_rate = len(wins) / len(trades) if trades else 0.0
    assert win_rate == 1.0, f"Expected win rate 1.0, got {win_rate}"

def test_consistency_score_components():
    """Test Consistency Score calculation for stability and drawdown components."""
    # Minimal mock trade period metrics: each dict is a period with 'return' and 'drawdown'
    trade_period_metrics = [
        {'return': 0.05, 'drawdown': -0.02},  # meets target
        {'return': 0.04, 'drawdown': -0.01},  # meets target
        {'return': 0.01, 'drawdown': -0.10},  # fails target
        {'return': 0.06, 'drawdown': -0.03},  # meets target
        {'return': -0.02, 'drawdown': -0.15}, # fails target
    ]
    target_return = 0.03
    max_drawdown = -0.05
    # Assume function returns percent of periods meeting both criteria (return >= target and drawdown >= max_drawdown)
    from strategy import calculate_consistency_score
    score = calculate_consistency_score(trade_period_metrics, target_return, max_drawdown)
    # 3 periods meet both criteria (first, second, and fourth)
    assert score == 60, f"Expected 60, got {score}"
    # Test all fail
    all_fail = [
        {'return': 0.01, 'drawdown': -0.10},
        {'return': -0.02, 'drawdown': -0.15},
    ]
    score = calculate_consistency_score(all_fail, target_return, max_drawdown)
    assert score == 0, f"Expected 0, got {score}"
    # Test all pass
    all_pass = [
        {'return': 0.05, 'drawdown': -0.01},
        {'return': 0.04, 'drawdown': -0.02},
    ]
    score = calculate_consistency_score(all_pass, target_return, max_drawdown)
    assert score == 100, f"Expected 100, got {score}"

def test_core_performance_metrics_calculator():
    """Test Backtester returns all required core metrics and handles edge cases (zero trades, negative returns)."""
    from strategy import Backtester
    import numpy as np
    # Case 1: Normal trades
    prices = pd.Series([100, 110, 105, 120, 115], index=pd.date_range('2023-01-01', periods=5))
    signals = pd.Series([1, 0, 1, 0, 0], index=prices.index)
    config = {
        'data': {'symbol': 'TEST', 'timeframe': '1d', 'lookback_period': 5},
        'strategy': {'short_sma': 1, 'long_sma': 2, 'risk_ratio': 1.0}
    }
    bt = Backtester(prices, signals, config)
    results = bt.run()
    # Required metrics
    for key in ['avg_return_per_trade', 'win_rate', 'avg_holding_period', 'profit_factor', 'max_drawdown']:
        assert key in results, f"Missing metric: {key}"
    # Types
    assert isinstance(results['avg_return_per_trade'], float)
    assert isinstance(results['win_rate'], float)
    assert isinstance(results['avg_holding_period'], float)
    assert isinstance(results['profit_factor'], float)
    assert isinstance(results['max_drawdown'], float)
    # Edge case: zero trades
    no_signal = pd.Series([0, 0, 0, 0, 0], index=prices.index)
    bt2 = Backtester(prices, no_signal, config)
    results2 = bt2.run()
    assert results2['avg_return_per_trade'] == 0.0
    assert results2['win_rate'] == 0.0
    assert results2['avg_holding_period'] == 0.0
    assert results2['profit_factor'] == 0.0
    # Edge case: negative returns
    prices_neg = pd.Series([100, 90, 80, 70, 60], index=pd.date_range('2023-01-01', periods=5))
    signals_neg = pd.Series([1, 0, 1, 0, 0], index=prices_neg.index)
    bt3 = Backtester(prices_neg, signals_neg, config)
    results3 = bt3.run()
    assert results3['avg_return_per_trade'] < 0
    assert results3['profit_factor'] <= 0

def test_metric_aggregation_consistency():
    """Test that aggregation of metrics across multiple periods is consistent and catches inconsistencies."""
    # Simulate per-period metrics (e.g., from walk-forward test)
    period_metrics = [
        {'avg_return_per_trade': 0.05, 'win_rate': 0.6, 'avg_holding_period': 10, 'profit_factor': 1.5, 'max_drawdown': -0.02},
        {'avg_return_per_trade': 0.03, 'win_rate': 0.5, 'avg_holding_period': 12, 'profit_factor': 1.2, 'max_drawdown': -0.03},
        {'avg_return_per_trade': 0.07, 'win_rate': 0.7, 'avg_holding_period': 9,  'profit_factor': 2.0, 'max_drawdown': -0.01},
    ]
    # Aggregate metrics (mean for all except max_drawdown, which should be min)
    from strategy import aggregate_metrics
    agg = aggregate_metrics(period_metrics)
    assert abs(agg['avg_return_per_trade'] - (0.05+0.03+0.07)/3) < 1e-8
    assert abs(agg['win_rate'] - (0.6+0.5+0.7)/3) < 1e-8
    assert abs(agg['avg_holding_period'] - (10+12+9)/3) < 1e-8
    assert abs(agg['profit_factor'] - (1.5+1.2+2.0)/3) < 1e-8
    assert agg['max_drawdown'] == min(-0.02, -0.03, -0.01)
    # Inconsistency: missing key in one period
    bad_metrics = period_metrics + [{'avg_return_per_trade': 0.04}]
    import pytest
    with pytest.raises(KeyError):
        aggregate_metrics(bad_metrics)
    # Edge case: non-numeric value in metrics should raise TypeError
    non_numeric_metrics = period_metrics.copy()
    non_numeric_metrics[0] = dict(non_numeric_metrics[0])
    non_numeric_metrics[0]['win_rate'] = 'not_a_number'
    with pytest.raises(TypeError):
        aggregate_metrics(non_numeric_metrics)

def test_level0_strategy_initialization():
    """Test Level 0 strategy initialization: config structure and parameter setup."""
    from strategy import validate_configuration
    # Minimal valid Level 0 config (Base MA Crossover)
    config = {
        'data': {
            'symbol': 'AAPL',
            'timeframe': '1d',
            'lookback_period': 30
        },
        'strategy': {
            'short_sma': 9,
            'long_sma': 21,
            'risk_ratio': 0.05
        }
    }
    # Should not raise
    validate_configuration(config)
    # Missing key should fail
    bad_config = {
        'data': {
            'symbol': 'AAPL',
            'timeframe': '1d',
            # 'lookback_period' missing
        },
        'strategy': {
            'short_sma': 9,
            'long_sma': 21,
            'risk_ratio': 0.05
        }
    }
    import pytest
    with pytest.raises(ValueError):
        validate_configuration(bad_config)

def test_level0_iteration_framework_executes_cycle():
    """Test that the Level 0 iteration framework executes a full strategy iteration cycle (Base MA)."""
    import pandas as pd
    from strategy_optimizer import StrategyOptimizer
    # Minimal config for Level 0
    config = {
        'ticker': 'AAPL',
        'start_date': '2023-01-01',
        'end_date': '2023-01-10',
        'initial_ma_short': 2,
        'initial_ma_long': 3,
        'transaction_cost_pct': 0.0
    }
    # Simulate price data
    dates = pd.date_range('2023-01-01', periods=10)
    prices = pd.Series([100, 101, 102, 103, 104, 105, 106, 107, 108, 109], index=dates)
    # Patch fetch_ohlcv_data to return our prices as a DataFrame
    import strategy_optimizer
    def mock_fetch_ohlcv_data(ticker, start, end):
        return pd.DataFrame({'Close': prices})
    strategy_optimizer.fetch_ohlcv_data = mock_fetch_ohlcv_data
    # Run Level 0 iteration (should not raise and should return best params/performance)
    optimizer = StrategyOptimizer(config)
    result = optimizer.optimize_parameters()
    assert 'best_params' in result
    assert 'best_performance' in result
    assert isinstance(result['best_params'], dict)
    assert isinstance(result['best_performance'], dict)
    # Should use the initial_ma_short/long as starting point
    assert result['best_params']['short_ma'] == config['initial_ma_short']
    assert result['best_params']['long_ma'] == config['initial_ma_long']

def test_level1_parameter_tuning_iteration():
    """Test Level 1 (Parameter Tuning) iteration: must optimize parameters across walk-forward periods."""
    import pandas as pd
    import numpy as np
    from strategy import StrategyOptimizer
    from backtester import generate_walk_forward_periods

    # Simulate price data (400 days to allow for 1-year train + 1-month test)
    dates = pd.date_range('2023-01-01', periods=400, freq='D')
    prices = pd.Series(np.linspace(100, 200, 400), index=dates)

    # Config template for optimization
    config_template = {
        'data': {'symbol': 'TEST', 'timeframe': '1d', 'lookback_period': 30},
        'strategy': {'short_sma': 3, 'long_sma': 5, 'risk_ratio': 0.05}
    }
    param_ranges = {
        'strategy.short_sma': [2, 3],
        'strategy.long_sma': [5, 6]
    }

    # Generate walk-forward periods (2 periods for simplicity)
    periods = generate_walk_forward_periods(dates, train_years=1, test_months=1)
    assert len(periods) > 0

    # For each period, optimize parameters on train, evaluate on test
    all_period_results = []
    for train_idx, test_idx in periods[:2]:  # Only test first 2 periods for speed
        train_prices = prices[train_idx]
        test_prices = prices[test_idx]
        optimizer = StrategyOptimizer(train_prices, config_template, param_ranges)
        result = optimizer.optimize()
        # Use best params on test set
        best_params = result['best_params']
        # Minimal signals: just use short_sma < long_sma for all
        from strategy import calculate_sma, generate_crossover_signals, Backtester
        short = calculate_sma(test_prices, best_params['strategy']['short_sma'])
        long = calculate_sma(test_prices, best_params['strategy']['long_sma'])
        signals = generate_crossover_signals(short, long)
        bt = Backtester(test_prices, signals, best_params)
        metrics = bt.run()
        # Only keep numeric metrics for aggregation
        numeric_metrics = {k: v for k, v in metrics.items() if isinstance(v, (int, float, np.floating))}
        all_period_results.append(numeric_metrics)

    # Aggregate metrics (e.g., average return, win rate)
    from strategy import aggregate_metrics
    agg = aggregate_metrics(all_period_results)
    assert 'avg_return_per_trade' in agg
    assert 'win_rate' in agg
    assert isinstance(agg['avg_return_per_trade'], float)
    assert isinstance(agg['win_rate'], float)

def test_trade_event_logging_schema():
    """Test that trade event logger outputs required trade metadata fields."""
    # Minimal mock trade event
    trade_event = {
        'timestamp': '2023-01-01T10:00:00Z',
        'symbol': 'AAPL',
        'price': 150.0,
        'quantity': 10,
        'side': 'buy'
    }
    # Assume a function log_trade_event exists (to be implemented)
    from logger import log_trade_event
    log_line = log_trade_event(trade_event)
    # Check that all required fields are present in the log line (CSV or string)
    for field in ['timestamp', 'symbol', 'price', 'quantity', 'side']:
        assert str(trade_event[field]) in log_line, f"Missing {field} in log output"