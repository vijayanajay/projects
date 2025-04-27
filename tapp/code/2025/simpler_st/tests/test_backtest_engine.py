import pandas as pd
import numpy as np
import pytest

# Assume the SMA crossover backtest logic will be in tech_analysis/backtest.py
from tech_analysis import backtest

def test_sma_crossover_basic():
    # Minimal price data for clear crossover
    data = pd.DataFrame({
        'close': [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
    })
    short_window = 3
    long_window = 5
    
    # Expected: Buy when short SMA crosses above long SMA, sell when crosses below
    # For this data, expect a buy at index 3 (short SMA > long SMA), sell at index 8 (short SMA < long SMA)
    # Add SMA columns for debugging
    data['sma_short'] = data['close'].rolling(window=short_window, min_periods=1).mean()
    data['sma_long'] = data['close'].rolling(window=long_window, min_periods=1).mean()
    print('DEBUG SMA VALUES:')
    print(data[['close', 'sma_short', 'sma_long']])
    trades = backtest.sma_crossover_backtest(data[['close']], short_window, long_window)
    print('DEBUG TRADES:', trades)
    if len(trades) != 2 or trades[0]['action'] != 'buy' or trades[1]['action'] != 'sell' or trades[0]['index'] != 3 or trades[1]['index'] != 8:
        raise AssertionError(f"Actual trades: {trades}")
    assert isinstance(trades, list)
    assert len(trades) == 2
    assert trades[0]['action'] == 'buy'
    assert trades[0]['index'] == 3
    assert trades[1]['action'] == 'sell'
    assert trades[1]['index'] == 8

def test_rsi_strategy_basic():
    # Minimal price data to simulate RSI overbought/oversold
    data = pd.DataFrame({
        'close': [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5]
    })
    period = 5
    overbought = 70
    oversold = 30
    # For this test, expect a buy when RSI crosses above oversold, sell when crosses below overbought
    # We'll just check that the function returns a list of trades with correct actions
    trades = backtest.rsi_strategy_backtest(data[['close']], period, overbought, oversold)
    print('DEBUG RSI TRADES:', trades)
    assert isinstance(trades, list)
    for trade in trades:
        assert trade['action'] in ('buy', 'sell')
        assert isinstance(trade['index'], int)

def test_trade_execution_and_log():
    """
    Test that the backtest engine simulates trade execution and records a trade log with expected fields.
    """
    data = pd.DataFrame({
        'close': [10, 11, 12, 13, 12, 11, 10, 9, 10, 11, 12, 13]
    })
    short_window = 2
    long_window = 3
    # This should generate at least one buy and one sell
    trades, trade_log = backtest.sma_crossover_backtest_with_log(data[['close']], short_window, long_window)
    # trade_log should be a list of dicts with keys: 'entry_index', 'exit_index', 'entry_price', 'exit_price', 'pnl'
    assert isinstance(trade_log, list)
    assert len(trade_log) > 0
    for log in trade_log:
        assert 'entry_index' in log
        assert 'exit_index' in log
        assert 'entry_price' in log
        assert 'exit_price' in log
        assert 'pnl' in log
        assert isinstance(log['entry_index'], int)
        assert isinstance(log['exit_index'], int)
        assert isinstance(log['entry_price'], (int, float))
        assert isinstance(log['exit_price'], (int, float))
        assert isinstance(log['pnl'], (int, float))

def test_performance_metrics_calculation():
    """
    Test that the backtest engine calculates returns, Sharpe ratio, drawdown, and win rate correctly from a trade log or equity curve.
    """
    # Simulate a simple equity curve
    equity_curve = [100, 110, 120, 115, 130, 120, 140]
    # Simulate trade log: 4 trades, 3 wins, 1 loss
    trade_log = [
        {'entry_index': 0, 'exit_index': 1, 'entry_price': 100, 'exit_price': 110, 'pnl': 10},  # win
        {'entry_index': 1, 'exit_index': 2, 'entry_price': 110, 'exit_price': 120, 'pnl': 10},  # win
        {'entry_index': 2, 'exit_index': 4, 'entry_price': 120, 'exit_price': 130, 'pnl': 10},  # win
        {'entry_index': 4, 'exit_index': 5, 'entry_price': 130, 'exit_price': 120, 'pnl': -10}, # loss
    ]
    metrics = backtest.calculate_performance_metrics(equity_curve, trade_log)
    # Check all required keys exist
    for key in ['total_return', 'sharpe_ratio', 'max_drawdown', 'win_rate']:
        assert key in metrics
    # Check total return (final/initial - 1)
    expected_return = (140 / 100) - 1
    assert abs(metrics['total_return'] - expected_return) < 1e-6
    # Check win rate (3/4)
    assert abs(metrics['win_rate'] - 0.75) < 1e-6
    # Sharpe ratio and drawdown: just check they are floats (detailed checks can be added later)
    assert isinstance(metrics['sharpe_ratio'], float)
    assert isinstance(metrics['max_drawdown'], float)
