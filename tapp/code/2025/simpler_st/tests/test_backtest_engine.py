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
