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
    Test that the backtest engine simulates trade execution and records a trade log with expected fields, including market context.
    """
    data = pd.DataFrame({
        'close': [10, 11, 12, 13, 12, 11, 10, 9, 10, 11, 12, 13],
        'volume': [100, 110, 120, 130, 120, 110, 100, 90, 100, 110, 120, 130]
    })
    short_window = 2
    long_window = 3
    # This should generate at least one buy and one sell
    trades, trade_log = backtest.sma_crossover_backtest_with_log(data[['close', 'volume']], short_window, long_window)
    # trade_log should be a list of dicts with keys: 'entry_index', 'exit_index', 'entry_price', 'exit_price', 'pnl', 'regime', 'volatility', 'volume'
    assert isinstance(trade_log, list)
    assert len(trade_log) > 0
    for log in trade_log:
        assert 'entry_index' in log
        assert 'exit_index' in log
        assert 'entry_price' in log
        assert 'exit_price' in log
        assert 'pnl' in log
        assert 'regime' in log, "Trade log must include market regime context"
        assert 'volatility' in log, "Trade log must include volatility context"
        assert 'volume' in log, "Trade log must include volume context"
        assert isinstance(log['entry_index'], int)
        assert isinstance(log['exit_index'], int)
        assert isinstance(log['entry_price'], (int, float))
        assert isinstance(log['exit_price'], (int, float))
        assert isinstance(log['pnl'], (int, float))
        assert isinstance(log['regime'], str)
        assert isinstance(log['volatility'], (int, float))
        assert isinstance(log['volume'], (int, float))

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

def test_export_backtest_results_for_report(tmp_path):
    """
    Test exporting backtest results (trade log and metrics) to a JSON file for report generation.
    """
    data = pd.DataFrame({
        'close': [10, 11, 12, 13, 12, 11, 10, 9, 10, 11, 12, 13]
    })
    short_window = 2
    long_window = 3
    trades, trade_log = backtest.sma_crossover_backtest_with_log(data[['close']], short_window, long_window)
    equity_curve = [row['exit_price'] if 'exit_price' in row else 0 for row in trade_log]
    metrics = backtest.calculate_performance_metrics(equity_curve, trade_log)
    output_file = tmp_path / "backtest_export.json"
    # This should raise if export_backtest_results is not implemented
    backtest.export_backtest_results(trade_log, metrics, str(output_file))
    # Check that file exists and has expected keys
    import json
    with open(output_file, 'r') as f:
        result = json.load(f)
    assert 'trade_log' in result
    assert 'metrics' in result
    assert isinstance(result['trade_log'], list)
    assert isinstance(result['metrics'], dict)

def test_correlate_performance_with_regimes():
    """
    Test that strategy performance is correctly grouped and summarized by detected market regimes.
    """
    # Simulate trade log with regime labels
    trade_log = [
        {'entry_index': 0, 'exit_index': 1, 'entry_price': 100, 'exit_price': 110, 'pnl': 10, 'regime': 'trending'},
        {'entry_index': 1, 'exit_index': 2, 'entry_price': 110, 'exit_price': 120, 'pnl': 10, 'regime': 'trending'},
        {'entry_index': 2, 'exit_index': 3, 'entry_price': 120, 'exit_price': 119, 'pnl': -1, 'regime': 'ranging'},
        {'entry_index': 3, 'exit_index': 4, 'entry_price': 119, 'exit_price': 121, 'pnl': 2, 'regime': 'ranging'},
        {'entry_index': 4, 'exit_index': 5, 'entry_price': 121, 'exit_price': 118, 'pnl': -3, 'regime': 'volatile'},
    ]
    # This function should return e.g. {'trending': {'mean_pnl': 10, 'count': 2}, ...}
    result = backtest.correlate_performance_with_regimes(trade_log)
    assert 'trending' in result
    assert 'ranging' in result
    assert 'volatile' in result
    assert result['trending']['mean_pnl'] == 10
    assert result['trending']['count'] == 2
    assert result['ranging']['mean_pnl'] == 0.5
    assert result['ranging']['count'] == 2
    assert result['volatile']['mean_pnl'] == -3
    assert result['volatile']['count'] == 1
