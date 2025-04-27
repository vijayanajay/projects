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
