import pandas as pd

def sma_crossover_backtest(data: pd.DataFrame, short_window: int, long_window: int):
    data = data.copy()
    data['sma_short'] = data['close'].rolling(window=short_window, min_periods=1).mean()
    data['sma_long'] = data['close'].rolling(window=long_window, min_periods=1).mean()

    # Buy when short SMA crosses above long SMA at the current bar
    trades = []
    position = None
    for idx, row in data.iterrows():
        # Only check crossover if not at the first row
        if idx > 0:
            prev_short = data.loc[idx-1, 'sma_short']
            prev_long = data.loc[idx-1, 'sma_long']
            # Buy: previous short <= long and now short > long
            if prev_short <= prev_long and row['sma_short'] > row['sma_long'] and position != 'long':
                trades.append({'action': 'buy', 'index': idx})
                position = 'long'
            # Sell: previous short >= long and now short < long
            elif prev_short >= prev_long and row['sma_short'] < row['sma_long'] and position == 'long':
                trades.append({'action': 'sell', 'index': idx})
                position = None
    return trades

def sma_crossover_backtest_with_log(data: pd.DataFrame, short_window: int, long_window: int):
    data = data.copy()
    data['sma_short'] = data['close'].rolling(window=short_window, min_periods=1).mean()
    data['sma_long'] = data['close'].rolling(window=long_window, min_periods=1).mean()

    trades = []
    trade_log = []
    position = None
    entry_index = None
    entry_price = None
    for idx, row in data.iterrows():
        if idx > 0:
            prev_short = data.loc[idx-1, 'sma_short']
            prev_long = data.loc[idx-1, 'sma_long']
            # Buy
            if prev_short <= prev_long and row['sma_short'] > row['sma_long'] and position != 'long':
                trades.append({'action': 'buy', 'index': idx})
                position = 'long'
                entry_index = idx
                entry_price = row['close']
            # Sell
            elif prev_short >= prev_long and row['sma_short'] < row['sma_long'] and position == 'long':
                trades.append({'action': 'sell', 'index': idx})
                exit_index = idx
                exit_price = row['close']
                pnl = exit_price - entry_price if entry_price is not None else 0
                trade_log.append({
                    'entry_index': entry_index,
                    'exit_index': exit_index,
                    'entry_price': entry_price,
                    'exit_price': exit_price,
                    'pnl': pnl
                })
                position = None
                entry_index = None
                entry_price = None
    return trades, trade_log

def rsi_strategy_backtest(data: pd.DataFrame, period: int, overbought: float, oversold: float):
    data = data.copy()
    # Calculate RSI
    delta = data['close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=period, min_periods=period).mean()
    avg_loss = loss.rolling(window=period, min_periods=period).mean()
    rs = avg_gain / (avg_loss + 1e-10)  # avoid div by zero
    data['rsi'] = 100 - (100 / (1 + rs))

    trades = []
    position = None
    for idx in range(1, len(data)):
        prev_rsi = data['rsi'].iloc[idx-1]
        curr_rsi = data['rsi'].iloc[idx]
        # Buy: prev RSI <= oversold, now RSI > oversold
        if prev_rsi <= oversold and curr_rsi > oversold and position != 'long':
            trades.append({'action': 'buy', 'index': idx})
            position = 'long'
        # Sell: prev RSI >= overbought, now RSI < overbought
        elif prev_rsi >= overbought and curr_rsi < overbought and position == 'long':
            trades.append({'action': 'sell', 'index': idx})
            position = None
    return trades

def calculate_performance_metrics(equity_curve, trade_log):
    import numpy as np
    equity_curve = np.array(equity_curve)
    # Total return
    total_return = (equity_curve[-1] / equity_curve[0]) - 1 if len(equity_curve) > 1 else 0.0
    # Win rate
    wins = sum(1 for trade in trade_log if trade['pnl'] > 0)
    win_rate = wins / len(trade_log) if trade_log else 0.0
    # Daily returns (assume 1 step per day for simplicity)
    returns = np.diff(equity_curve) / equity_curve[:-1]
    mean_ret = returns.mean() if len(returns) > 0 else 0.0
    std_ret = returns.std(ddof=1) if len(returns) > 1 else 1e-10
    sharpe_ratio = (mean_ret / std_ret) * np.sqrt(252) if std_ret > 0 else 0.0
    # Max drawdown
    running_max = np.maximum.accumulate(equity_curve)
    drawdowns = (equity_curve - running_max) / running_max
    max_drawdown = drawdowns.min() if len(drawdowns) > 0 else 0.0
    return {
        'total_return': total_return,
        'win_rate': win_rate,
        'sharpe_ratio': sharpe_ratio,
        'max_drawdown': abs(max_drawdown),
    }
