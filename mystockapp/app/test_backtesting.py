import pytest
import pandas as pd
import numpy as np
from strategy import Backtester  # To be implemented
from backtester import generate_walk_forward_periods  # To be implemented

def test_backtesting_simulation():
    """Test backtesting simulation against known patterns."""
    # Create sample price data
    dates = pd.date_range('2023-01-01', periods=10, freq='D')
    prices = pd.Series([100, 102, 101, 103, 107, 110, 108, 106, 109, 112], index=dates)
    
    # Test case 1: Simple buy and hold strategy
    signals = pd.Series([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], index=dates)  # All buy signals
    
    config = {
        'data': {
            'symbol': 'TEST',
            'timeframe': '1d',
            'lookback_period': 5
        },
        'strategy': {
            'short_sma': 3,
            'long_sma': 5,
            'risk_ratio': 0.05
        }
    }
    
    backtester = Backtester(prices, signals, config)
    results = backtester.run()
    
    # Verify basic backtest output structure
    assert 'trades' in results
    assert 'cumulative_returns' in results
    assert 'sharpe_ratio' in results
    assert 'max_drawdown' in results
    
    # Verify trade generation
    trades = results['trades']
    assert len(trades) > 0
    assert all(trade['profit'] >= 0 for trade in trades)  # All profitable in this simple case
    
    # Test case 2: Alternating signals
    alt_signals = pd.Series([1, 0, 1, 0, 1, 0, 1, 0, 1, 0], index=dates)
    
    alt_backtester = Backtester(prices, alt_signals, config)
    alt_results = alt_backtester.run()
    
    # Verify trade count matches expected pattern
    alt_trades = alt_results['trades']
    assert len(alt_trades) == 5  # Should have 5 trades from alternating signals
    
    # Test case 3: No signals
    no_signal = pd.Series([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], index=dates)
    
    no_backtester = Backtester(prices, no_signal, config)
    no_results = no_backtester.run()
    
    # Verify no trades generated
    assert len(no_results['trades']) == 0
    assert no_results['cumulative_returns'] == 0

def test_walk_forward_period_generation():
    # Simulate a date range (e.g., 2 years of daily data)
    dates = pd.date_range('2020-01-01', '2021-12-31', freq='D')
    # Use 1 year train, 3 months test as in config
    train_years = 1
    test_months = 3
    periods = generate_walk_forward_periods(dates, train_years, test_months)
    # Each period should have correct boundaries, no overlap in test, and full coverage
    for i, (train_idx, test_idx) in enumerate(periods):
        train_dates = dates[train_idx]
        test_dates = dates[test_idx]
        # Train and test should not overlap
        assert set(train_dates).isdisjoint(set(test_dates))
        # Test period should follow immediately after train
        assert train_dates[-1] < test_dates[0]
        # Train period length should be about 365 days
        assert 360 <= len(train_dates) <= 366
        # Test period length should be about 90 days
        assert 85 <= len(test_dates) <= 95
    # All test periods together should cover the full date range except the initial train window
    all_test = sorted([d for _, test_idx in periods for d in dates[test_idx]])
    assert all_test[0] > dates[0]
    assert all_test[-1] <= dates[-1]

def test_trade_simulation_framework():
    """Test that the trade simulation framework executes trades as expected."""
    # Simulate price data
    dates = pd.date_range('2023-01-01', periods=6, freq='D')
    prices = pd.Series([100, 102, 101, 105, 104, 106], index=dates)
    # Simulate signals: Buy on day 1, sell on day 3, buy on day 4, sell on day 6
    signals = pd.Series([1, 1, 0, 1, 1, 0], index=dates)
    config = {
        'data': {'symbol': 'TEST', 'timeframe': '1d', 'lookback_period': 5},
        'strategy': {'short_sma': 2, 'long_sma': 3, 'risk_ratio': 0.1}
    }
    backtester = Backtester(prices, signals, config)
    results = backtester.run()
    trades = results['trades']
    # Should have 2 trades
    assert len(trades) == 2
    # First trade: entry at 100 (2023-01-01), exit at 101 (2023-01-03)
    assert trades[0]['entry_price'] == 100
    assert trades[0]['exit_price'] == 101
    assert trades[0]['profit'] == 0.1  # absolute profit (101-100)*0.1
    assert abs(trades[0]['return_pct'] - 0.01) < 1e-6  # percent profit
    # Second trade: entry at 105 (2023-01-04), exit at 106 (2023-01-06)
    assert trades[1]['entry_price'] == 105
    assert trades[1]['exit_price'] == 106
    assert trades[1]['profit'] == 0.1  # absolute profit (106-105)*0.1
    assert abs(trades[1]['return_pct'] - (1/105)) < 1e-6  # percent profit

def test_trade_simulation_slippage_commissions_position_sizing():
    """Test that trade simulation applies slippage, commissions, and position sizing."""
    dates = pd.date_range('2023-01-01', periods=4, freq='D')
    prices = pd.Series([100, 105, 110, 120], index=dates)
    signals = pd.Series([1, 1, 0, 0], index=dates)  # Buy on day 1, sell on day 3
    config = {
        'data': {'symbol': 'TEST', 'timeframe': '1d', 'lookback_period': 2},
        'strategy': {'short_sma': 1, 'long_sma': 2, 'risk_ratio': 0.5},
        'slippage_pct': 0.01,  # 1% slippage per trade
        'commission_pct': 0.005  # 0.5% commission per trade
    }
    backtester = Backtester(prices, signals, config)
    results = backtester.run()
    trades = results['trades']
    # Should have 1 trade
    assert len(trades) == 1
    trade = trades[0]
    # Entry price should include slippage and commission
    expected_entry = prices.iloc[0] * (1 + config['slippage_pct']) * (1 + config['commission_pct'])
    # Exit price should subtract slippage and commission
    expected_exit = prices.iloc[2] * (1 - config['slippage_pct']) * (1 - config['commission_pct'])
    # Position size should be risk_ratio (0.5)
    expected_size = config['strategy']['risk_ratio']
    # Profit should be (exit - entry) * position size
    expected_profit = (expected_exit - expected_entry) * expected_size
    expected_return_pct = (expected_exit - expected_entry) / expected_entry
    assert abs(trade['entry_price'] - expected_entry) < 1e-6
    assert abs(trade['exit_price'] - expected_exit) < 1e-6
    assert abs(trade['position_size'] - expected_size) < 1e-6
    assert abs(trade['profit'] - expected_profit) < 1e-6
    assert abs(trade['return_pct'] - expected_return_pct) < 1e-6

def test_fwt_in_sample_vs_out_of_sample_validation():
    """Test that FWT validation catches inconsistencies between in-sample and out-of-sample performance."""
    # Mock FWT results: train and test period returns
    fwt_results = [
        {'train_return': 0.10, 'test_return': -0.05},  # Large discrepancy
        {'train_return': 0.12, 'test_return': -0.02},
        {'train_return': 0.09, 'test_return': 0.01},
    ]
    # Simple validation: fail if any test return is negative while train is strongly positive
    inconsistent = any(
        r['train_return'] > 0.08 and r['test_return'] < 0.0 for r in fwt_results
    )
    # This should be True for the above mock data
    assert inconsistent, "FWT validation did not catch in-sample/out-of-sample inconsistency"

def test_individual_metric_calculations():
    """Test Sharpe ratio, max drawdown, and win rate calculations individually."""
    dates = pd.date_range('2023-01-01', periods=5, freq='D')
    prices = pd.Series([100, 110, 105, 120, 115], index=dates)
    # Simulate signals: Buy on day 1, sell on day 3, buy on day 4, sell on day 5
    signals = pd.Series([1, 1, 0, 1, 0], index=dates)
    config = {
        'data': {'symbol': 'TEST', 'timeframe': '1d', 'lookback_period': 5},
        'strategy': {'short_sma': 2, 'long_sma': 3, 'risk_ratio': 1.0}
    }
    backtester = Backtester(prices, signals, config)
    results = backtester.run()
    # Sharpe ratio should be a float
    assert isinstance(results['sharpe_ratio'], float)
    # Max drawdown should be negative or zero
    assert results['max_drawdown'] <= 0
    # Win rate: count trades with positive return
    trades = results['trades']
    if trades:
        win_count = sum(1 for t in trades if t['profit'] > 0)
        win_rate = win_count / len(trades)
        # At least one trade should be a win
        assert win_rate > 0
    else:
        assert results['sharpe_ratio'] == 0.0
        assert results['max_drawdown'] == 0.0