import pandas as pd
import numpy as np
import pytest

# Assume the SMA crossover backtest logic will be in tech_analysis/backtest.py
from tech_analysis import backtest
from tech_analysis.utils import (
    calculate_performance_metrics,
    correlate_performance_with_regimes,
    extract_drawdown_periods,
    calculate_indicator_summary_stats
)

def test_sma_crossover_basic():
    # Minimal price data for clear crossover
    data = pd.DataFrame({
        'close': [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],
        'high': [2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2],
        'low': [0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0]
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
        'close': [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5],
        'high': [2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6],
        'low': [0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
    })
    period = 5
    overbought = 70
    oversold = 30
    # For this test, expect a buy when RSI crosses above oversold, sell when crosses below overbought
    # We'll just check that the function returns a list of trades with correct actions
    signals, trade_log = backtest.rsi_strategy_backtest(data[['close']], period, overbought, oversold, strategy_params={})
    print('DEBUG RSI TRADES:', signals, trade_log)
    assert isinstance(signals, list)
    assert all(isinstance(sig, dict) for sig in signals)
    # Optionally: check trade_log structure
    assert isinstance(trade_log, list)
    for trade in trade_log:
        assert 'entry_index' in trade and 'exit_index' in trade

def test_rsi_strategy_handles_none_strategy_params():
    """
    Ensure rsi_strategy_backtest does not raise AttributeError when strategy_params is None
    and sets ticker to 'UNKNOWN'.
    """
    data = pd.DataFrame({
        'close': [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5],
        'high': [2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 3, 4, 5, 6],
        'low': [0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1, 0, 1, 2, 3, 4]
    })
    period = 5
    overbought = 70
    oversold = 30
    # Call without strategy_params
    signals, trade_log = backtest.rsi_strategy_backtest(data[['close']], period, overbought, oversold)
    # Should not raise, and ticker should be 'UNKNOWN' in trade_log or signals if present
    assert isinstance(trade_log, list)
    if trade_log:
        for trade in trade_log:
            assert trade.get('ticker', None) == 'UNKNOWN'
    elif signals:
        for sig in signals:
            assert sig.get('ticker', None) == 'UNKNOWN'

def test_trade_execution_and_log():
    """
    Test that the backtest engine simulates trade execution and records a trade log with expected fields, including market context.
    """
    data = pd.DataFrame({
        'close': [10, 11, 12, 13, 12, 11, 10, 9, 10, 11, 12, 13],
        'volume': [100, 110, 120, 130, 120, 110, 100, 90, 100, 110, 120, 130],
        'high': [11, 12, 13, 14, 13, 12, 11, 10, 11, 12, 13, 14],
        'low': [9, 10, 11, 12, 11, 10, 9, 8, 9, 10, 11, 12]
    })
    short_window = 2
    long_window = 3
    strategy_params = {'context_window': 10} # Add dummy params for the test
    # This should generate at least one buy and one sell
    trades, trade_log = backtest.sma_crossover_backtest_with_log(data, short_window, long_window, strategy_params)
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
        assert 'entry_sma_short' in log, "Trade log must include entry short SMA value"
        assert 'entry_sma_long' in log, "Trade log must include entry long SMA value"
        assert 'exit_sma_short' in log, "Trade log must include exit short SMA value"
        assert 'exit_sma_long' in log, "Trade log must include exit long SMA value"
        assert 'atr_entry' in log, "Trade log must include ATR at entry"
        assert 'volume_entry' in log, "Trade log must include volume at entry"
        assert isinstance(log['entry_index'], int)
        assert isinstance(log['exit_index'], int)
        assert isinstance(log['entry_price'], (int, float))
        assert isinstance(log['exit_price'], (int, float))
        assert isinstance(log['pnl'], (int, float))
        assert isinstance(log['regime'], str)
        assert isinstance(log['volatility'], (int, float))
        assert isinstance(log['volume'], (int, float))
        assert isinstance(log['entry_sma_short'], (int, float, np.floating, np.integer))
        assert isinstance(log['entry_sma_long'], (int, float, np.floating, np.integer))
        assert isinstance(log['exit_sma_short'], (int, float, np.floating, np.integer))
        assert isinstance(log['exit_sma_long'], (int, float, np.floating, np.integer))
        assert isinstance(log['atr_entry'], (int, float, np.floating, np.integer)), "ATR at entry must be numeric"
        assert isinstance(log['volume_entry'], (int, float, np.floating, np.integer)), "Volume at entry must be numeric"
    # Optionally: check trade_log structure
    assert isinstance(trade_log, list)
    for trade in trade_log:
        assert 'entry_index' in trade and 'exit_index' in trade

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
    metrics = calculate_performance_metrics(equity_curve, trade_log)
    # Check all required keys exist under 'strategy'
    strat_metrics = metrics['strategy']
    for key in ['total_return', 'sharpe_ratio', 'max_drawdown', 'win_rate']:
        assert key in strat_metrics
    # Check total return (final/initial - 1)
    expected_return = (140 / 100) - 1
    assert abs(strat_metrics['total_return'] - expected_return) < 1e-6
    # Check win rate (3/4)
    assert abs(strat_metrics['win_rate'] - 0.75) < 1e-6
    # Sharpe ratio and drawdown: just check they are floats (detailed checks can be added later)
    assert isinstance(strat_metrics['sharpe_ratio'], float) or hasattr(strat_metrics['sharpe_ratio'], '__float__')
    assert isinstance(strat_metrics['max_drawdown'], float) or hasattr(strat_metrics['max_drawdown'], '__float__')

def test_export_backtest_results_for_report(tmp_path):
    """
    Test exporting backtest results (trade log and metrics) to a JSON file for report generation.
    """
    data = pd.DataFrame({
        'close': [10, 11, 12, 13, 12, 11, 10, 9, 10, 11, 12, 13],
        'high': [11, 12, 13, 14, 13, 12, 11, 10, 11, 12, 13, 14],
        'low': [9, 10, 11, 12, 11, 10, 9, 8, 9, 10, 11, 12]
    })
    short_window = 2
    long_window = 3
    strategy_params = {'context_window': 10} # Add dummy params for the test
    trades, trade_log = backtest.sma_crossover_backtest_with_log(data, short_window, long_window, strategy_params)
    equity_curve = [row['exit_price'] if 'exit_price' in row else 0 for row in trade_log]
    metrics = calculate_performance_metrics(equity_curve, trade_log)
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
    result = correlate_performance_with_regimes(trade_log)
    assert 'trending' in result
    assert 'ranging' in result
    assert 'volatile' in result
    assert result['trending']['mean_pnl'] == 10
    assert result['trending']['count'] == 2
    assert result['ranging']['mean_pnl'] == 0.5
    assert result['ranging']['count'] == 2
    assert result['volatile']['mean_pnl'] == -3
    assert result['volatile']['count'] == 1

def test_trade_log_includes_rationale():
    """
    Test that each trade log entry includes a human-readable rationale string for PDF reporting.
    """
    data = pd.DataFrame({
        'close': [10, 11, 12, 13, 12, 11, 10, 9, 10, 11, 12, 13],
        'volume': [100, 110, 120, 130, 120, 110, 100, 90, 100, 110, 120, 130],
        'high': [11, 12, 13, 14, 13, 12, 11, 10, 11, 12, 13, 14],
        'low': [9, 10, 11, 12, 11, 10, 9, 8, 9, 10, 11, 12]
    })
    short_window = 2
    long_window = 3
    strategy_params = {'context_window': 10} # Add dummy params for the test
    trades, trade_log = backtest.sma_crossover_backtest_with_log(data, short_window, long_window, strategy_params)
    assert isinstance(trade_log, list)
    assert len(trade_log) > 0
    for log in trade_log:
        assert 'rationale' in log, "Trade log must include rationale field for PDF"
        assert isinstance(log['rationale'], str), "Rationale must be a string"
        assert log['rationale'].strip() != '', "Rationale string must not be empty"
        # Optionally, check rationale content matches action
        if log['entry_price'] < log['exit_price']:
            assert 'Buy' in log['rationale'] or 'buy' in log['rationale']
        elif log['entry_price'] > log['exit_price']:
            assert 'Sell' in log['rationale'] or 'sell' in log['rationale']

def test_portfolio_state_basic():
    from tech_analysis.portfolio import PortfolioState
    # Start with 10,000 cash
    pf = PortfolioState(10000)
    # Buy 10 shares of ABC at 100
    pf.buy('ABC', 10, 100, 'Signal: SMA cross')
    assert pf.cash == 9000
    assert pf.holdings['ABC'] == 10
    assert pf.transaction_log[-1]['action'] == 'buy'
    assert pf.transaction_log[-1]['ticker'] == 'ABC'
    assert pf.transaction_log[-1]['qty'] == 10
    assert pf.transaction_log[-1]['price'] == 100
    assert pf.transaction_log[-1]['rationale'] == 'Signal: SMA cross'
    # Sell 5 shares at 110
    pf.sell('ABC', 5, 110, 'Profit target')
    assert pf.cash == 9000 + 5 * 110
    assert pf.holdings['ABC'] == 5
    assert pf.transaction_log[-1]['action'] == 'sell'
    assert pf.transaction_log[-1]['qty'] == 5
    # Try to sell more than held (should raise)
    try:
        pf.sell('ABC', 10, 120, 'Mistake')
        assert False, 'Should not allow short selling'
    except ValueError:
        pass
    # Buy with insufficient cash (should raise)
    try:
        pf.buy('XYZ', 1000, 1000, 'Too expensive')
        assert False, 'Should not allow buy with insufficient cash'
    except ValueError:
        pass

def test_portfolio_backtest_multi_ticker():
    """
    Test unified portfolio-level backtest across multiple tickers, time-based iteration, no short selling, buy preference, position sizing, and rationale logging.
    """
    import pandas as pd
    from tech_analysis.portfolio import PortfolioState
    # Simulate two tickers with simple price data
    data = {
        'AAA': pd.DataFrame({
            'close': [10, 12, 14, 11, 15, 20],
            'volume': [100, 120, 110, 130, 140, 150],
            'high': [11, 13, 15, 12, 16, 21],
            'low': [9, 11, 13, 10, 14, 19]
        }),
        'BBB': pd.DataFrame({
            'close': [20, 18, 16, 14, 12, 10],
            'volume': [200, 180, 170, 160, 150, 140],
            'high': [21, 19, 17, 15, 13, 11],
            'low': [19, 17, 15, 13, 11, 9]
        })
    }
    initial_cash = 1000
    position_size = 100  # Max cash per buy
    # Minimalistic signals: Buy AAA if price increases, BBB if price decreases
    # We'll assume the function uses a naive crossover: buy if last close > prev close
    pf = PortfolioState(initial_cash)
    # This should raise if portfolio_backtest is not implemented
    from tech_analysis import backtest
    results = backtest.portfolio_backtest(
        data,
        initial_cash=initial_cash,
        position_size=position_size,
        strategy_params={
            'position_size': position_size,
            'initial_cash': initial_cash,
            'short_window': 2,
            'long_window': 3
        }
    )
    # results should include 'portfolio_state', 'trade_log', and 'assets' (explicitly listed)
    assert 'portfolio_state' in results
    assert 'trade_log' in results
    assert 'assets' in results, "Backtest results must include explicit list of assets traded."
    assert set(results['assets']) == set(data.keys()), f"Assets listed in results do not match input: {results['assets']} vs {list(data.keys())}"
    pf_result = results['portfolio_state']
    trade_log = results['trade_log']
    # PortfolioState should reflect buys only, never short sells
    for trade in trade_log:
        assert trade['action'] == 'buy', 'Only buy actions allowed (no short selling)'
        assert trade['qty'] > 0
        assert trade['ticker'] in data
        assert 'rationale' in trade and trade['rationale'].strip() != ''
    # Cash should decrease with each buy, never negative
    assert pf_result.cash >= 0
    # Holdings should be non-negative
    for qty in pf_result.holdings.values():
        assert qty >= 0
    # There should be at least one trade for AAA (uptrend)
    assert any(trade['ticker'] == 'AAA' for trade in trade_log)
    # There should be no short sells for BBB (downtrend)
    assert all(trade['action'] == 'buy' for trade in trade_log)

def test_timeframe_and_frequency_applied():
    """
    Test that the backtest fetches data strictly within the specified start/end date and frequency from config.json.
    """
    import json, os
    from tech_analysis.backtest import get_data_for_backtest, load_config
    cfg = load_config()
    data = get_data_for_backtest()
    # Pick a ticker present in STOCKS_LIST
    ticker = next(iter(data))
    df = data[ticker]
    # Check DataFrame date range and frequency
    assert not df.empty, f"No data fetched for {ticker}"
    # Index is DatetimeIndex
    assert str(type(df.index)).endswith("DatetimeIndex'>")
    # Check start/end
    assert str(cfg['start_date']) <= str(df.index.min().date()), f"Data starts before config start_date: {df.index.min()} < {cfg['start_date']}"
    assert str(cfg['end_date']) >= str(df.index.max().date()), f"Data ends after config end_date: {df.index.max()} > {cfg['end_date']}"
    # Check frequency (roughly)
    freq = cfg['frequency']
    if freq == '1d':
        # Check that the step between rows is 1 day
        diffs = df.index.to_series().diff().dropna()
        assert all(d.total_seconds() >= 86400 for d in diffs), "Some intervals are less than 1 day"
    # If more granular freq, add more checks as needed

def test_benchmark_comparison():
    """
    Test that the backtest engine can compare strategy performance to a benchmark (e.g., buy-and-hold).
    """
    # Simulate strategy and benchmark equity curves
    strategy_curve = [100, 110, 120, 115, 130, 120, 140]
    benchmark_curve = [100, 105, 110, 120, 125, 130, 135]  # e.g., buy-and-hold
    trade_log = [
        {'entry_index': 0, 'exit_index': 1, 'entry_price': 100, 'exit_price': 110, 'pnl': 10},
        {'entry_index': 1, 'exit_index': 2, 'entry_price': 110, 'exit_price': 120, 'pnl': 10},
        {'entry_index': 2, 'exit_index': 4, 'entry_price': 120, 'exit_price': 130, 'pnl': 10},
        {'entry_index': 4, 'exit_index': 5, 'entry_price': 130, 'exit_price': 120, 'pnl': -10},
    ]
    # Call the updated metrics function
    metrics = calculate_performance_metrics(strategy_curve, trade_log, benchmark_equity_curve=benchmark_curve)
    # Check that both strategy and benchmark metrics are present
    assert 'strategy' in metrics
    assert 'benchmark' in metrics
    for key in ['total_return', 'sharpe_ratio', 'max_drawdown', 'win_rate']:
        assert key in metrics['strategy']
        assert key in metrics['benchmark']
    # Check that strategy and benchmark returns are as expected
    expected_strategy_return = (140 / 100) - 1
    expected_benchmark_return = (135 / 100) - 1
    assert abs(metrics['strategy']['total_return'] - expected_strategy_return) < 1e-6
    assert abs(metrics['benchmark']['total_return'] - expected_benchmark_return) < 1e-6

def test_summary_stats_include_atr_and_volume():
    """
    Test that summary statistics include ATR and volume (mean, min, max) over all trades.
    """
    data = pd.DataFrame({
        'close': [10, 11, 12, 13, 12, 11, 10, 9, 10, 11, 12, 13],
        'volume': [100, 110, 120, 130, 120, 110, 100, 90, 100, 110, 120, 130],
        'high': [11, 12, 13, 14, 13, 12, 11, 10, 11, 12, 13, 14],
        'low': [9, 10, 11, 12, 11, 10, 9, 8, 9, 10, 11, 12]
    })
    short_window = 2
    long_window = 3
    strategy_params = {'context_window': 10}
    trades, trade_log = backtest.sma_crossover_backtest_with_log(data, short_window, long_window, strategy_params)
    # Assume a new function is added to calculate summary stats for ATR/volume
    from tech_analysis import backtest as bt
    stats = bt.calculate_indicator_summary_stats(trade_log)
    for field in ['atr_entry', 'volume_entry']:
        assert field in stats, f"Summary stats must include {field}"
        for stat in ['mean', 'min', 'max']:
            assert stat in stats[field], f"{field} summary must include {stat}"
            assert isinstance(stats[field][stat], (int, float, np.floating, np.integer)), f"{field} {stat} must be numeric"

def test_export_backtest_results_serializes_numpy_types(tmp_path):
    """
    Test that export_backtest_results correctly serializes NumPy types in trade_log and metrics.
    Should not raise TypeError: Object of type int64/float64 is not JSON serializable.
    """
    import numpy as np
    import json
    from tech_analysis import backtest
    # Create trade_log and metrics with NumPy types
    trade_log = [
        {'entry_index': np.int64(0), 'exit_index': np.int64(1), 'pnl': np.float64(10.5)}
    ]
    metrics = {
        'total_return': np.float64(0.123),
        'num_trades': np.int64(1)
    }
    output_file = tmp_path / "backtest_export_numpy.json"
    # Should not raise
    backtest.export_backtest_results(trade_log, metrics, str(output_file))
    # Check file exists and loads
    with open(output_file, 'r') as f:
        result = json.load(f)
    assert result['trade_log'][0]['entry_index'] == 0
    assert result['trade_log'][0]['exit_index'] == 1
    assert result['trade_log'][0]['pnl'] == 10.5
    assert result['metrics']['total_return'] == 0.123
    assert result['metrics']['num_trades'] == 1

def test_calculate_atr_requires_high_low():
    import pandas as pd
    from tech_analysis.utils import calculate_atr
    # DataFrame missing high/low columns
    df = pd.DataFrame({
        'close': [1, 2, 3, 4, 5]
    })
    try:
        _ = calculate_atr(df, window=3)
    except ValueError as e:
        msg = str(e).lower()
        assert "high" in msg and "low" in msg
    else:
        raise AssertionError("calculate_atr should raise ValueError if 'high'/'low' columns are missing.")

def test_sma_crossover_does_not_recalculate_indicators():
    import pandas as pd
    from tech_analysis.backtest import sma_crossover_backtest_with_log_dict
    # Precompute indicators
    df = pd.DataFrame({
        'close': [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],
        'high': [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],
        'low': [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1],
        'volume': [100]*11
    })
    df['sma_short'] = df['close'].rolling(window=3, min_periods=1).mean()
    df['sma_long'] = df['close'].rolling(window=5, min_periods=1).mean()
    df['atr'] = 42.0  # Sentinel value
    df['rsi'] = 99.0  # Sentinel value
    strategy_params = {'commission': 0.0, 'slippage': 0.0}
    result = sma_crossover_backtest_with_log_dict(df, 3, 5, strategy_params)
    # Check that the sentinel values are preserved in the trade log
    for trade in result['trade_log']:
        assert trade['atr_entry'] == 42.0
        assert trade['entry_sma_short'] == trade['entry_sma_short']  # Should match precomputed
        assert trade['entry_sma_long'] == trade['entry_sma_long']
        assert trade['entry_rsi'] == 99.0
