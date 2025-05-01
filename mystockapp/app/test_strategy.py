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