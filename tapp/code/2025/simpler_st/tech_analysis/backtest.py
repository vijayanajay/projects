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
