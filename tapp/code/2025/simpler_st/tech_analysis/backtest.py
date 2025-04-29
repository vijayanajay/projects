import pandas as pd
from tech_analysis.market_regimes import classify_market_regime
import numpy as np
from tech_analysis.utils import calculate_atr

# Helper to convert NumPy types to Python types recursively
def convert_numpy_types(obj):
    if isinstance(obj, dict):
        return {k: convert_numpy_types(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_numpy_types(i) for i in obj]
    elif isinstance(obj, np.generic):
        return obj.item()
    elif isinstance(obj, np.ndarray):
        return obj.tolist()
    else:
        return obj

def sma_crossover_backtest(data: pd.DataFrame, short_window: int, long_window: int):
    data = data.copy()
    data['sma_short'] = data['close'].rolling(window=short_window, min_periods=1).mean()
    data['sma_long'] = data['close'].rolling(window=long_window, min_periods=1).mean()

    trades = []
    position = None
    prev_short = data['sma_short'].shift(1)
    prev_long = data['sma_long'].shift(1)
    for idx, row in data.iterrows():
        # Only check crossover if not at the first row
        if pd.isna(prev_short.loc[idx]) or pd.isna(prev_long.loc[idx]):
            continue
        # Buy: previous short <= long and now short > long
        if prev_short.loc[idx] <= prev_long.loc[idx] and row['sma_short'] > row['sma_long'] and position != 'long':
            trades.append({'action': 'buy', 'index': idx})
            position = 'long'
        # Sell: previous short >= long and now short < long
        elif prev_short.loc[idx] >= prev_long.loc[idx] and row['sma_short'] < row['sma_long'] and position == 'long':
            trades.append({'action': 'sell', 'index': idx})
            position = None
    return trades

def sma_crossover_backtest_with_log(data: pd.DataFrame, short_window: int, long_window: int, strategy_params: dict):
    data = data.copy()
    data['sma_short'] = data['close'].rolling(window=short_window, min_periods=1).mean()
    data['sma_long'] = data['close'].rolling(window=long_window, min_periods=1).mean()
    # ATR window: use long_window or 14 as default
    atr_window = strategy_params.get('atr_window', max(long_window, 14))
    data['atr'] = calculate_atr(data, window=atr_window)
    # Compute RSI if not already present
    rsi_period = strategy_params.get('rsi_period', 14)
    if 'rsi' not in data.columns:
        delta = data['close'].diff()
        gain = delta.clip(lower=0)
        loss = -delta.clip(upper=0)
        avg_gain = gain.rolling(window=rsi_period, min_periods=rsi_period).mean()
        avg_loss = loss.rolling(window=rsi_period, min_periods=rsi_period).mean()
        rs = avg_gain / avg_loss
        data['rsi'] = 100 - (100 / (1 + rs))

    commission = strategy_params.get('commission', 0.0)
    slippage = strategy_params.get('slippage', 0.0)

    trades = []
    trade_log = []
    position = None
    entry_index = None
    entry_price = None
    entry_volatility = None
    entry_volume = None
    entry_regime = None
    entry_atr = None
    entry_sma_short = None
    entry_sma_long = None
    entry_rsi = None
    prev_short = data['sma_short'].shift(1)
    prev_long = data['sma_long'].shift(1)
    for idx, row in data.iterrows():
        if pd.isna(prev_short.loc[idx]) or pd.isna(prev_long.loc[idx]):
            continue
        # Buy
        if prev_short.loc[idx] <= prev_long.loc[idx] and row['sma_short'] > row['sma_long'] and position != 'long':
            trades.append({'action': 'buy', 'index': idx})
            position = 'long'
            entry_index = idx
            entry_price = row['close']
            # Market context at entry
            context_window = strategy_params.get('context_window', 10)
            price_window = data['close'].iloc[max(0, data.index.get_loc(idx)-context_window):data.index.get_loc(idx)+1]
            entry_regime = classify_market_regime(price_window)
            entry_volatility = price_window.std()
            entry_volume = row['volume'] if 'volume' in data.columns else 0
            entry_atr = row['atr'] if 'atr' in data.columns else 0
            entry_sma_short = row['sma_short']
            entry_sma_long = row['sma_long']
            entry_rsi = row['rsi'] if 'rsi' in data.columns else None
        # Sell
        elif prev_short.loc[idx] >= prev_long.loc[idx] and row['sma_short'] < row['sma_long'] and position == 'long':
            trades.append({'action': 'sell', 'index': idx})
            exit_index = idx
            exit_price = row['close']
            adj_entry, adj_exit, net_pnl, commission_cost = apply_transaction_costs(entry_price, exit_price, commission, slippage)
            # Market context at exit
            context_window = strategy_params.get('context_window', 10)
            price_window = data['close'].iloc[max(0, data.index.get_loc(idx)-context_window):data.index.get_loc(idx)+1]
            exit_regime = classify_market_regime(price_window)
            exit_volatility = price_window.std()
            exit_volume = row['volume'] if 'volume' in data.columns else 0
            exit_atr = row['atr'] if 'atr' in data.columns else 0
            exit_sma_short = row['sma_short']
            exit_sma_long = row['sma_long']
            exit_rsi = row['rsi'] if 'rsi' in data.columns else None
            trade_log.append({
                'entry_index': entry_index,
                'exit_index': exit_index,
                'entry_price': adj_entry,
                'exit_price': adj_exit,
                'pnl': net_pnl,
                'commission_cost': commission_cost,
                'regime': entry_regime,
                'entry_regime': entry_regime,
                'exit_regime': exit_regime,
                'EntryRegime': entry_regime,
                'ExitRegime': exit_regime,
                'volatility': entry_volatility,
                'exit_volatility': exit_volatility,
                'entry_volatility': entry_volatility,
                'exit_volatility': exit_volatility,
                'EntryVolatility': entry_volatility,
                'ExitVolatility': exit_volatility,
                'volume': entry_volume,
                'exit_volume': exit_volume,
                'entry_volume': entry_volume,
                'exit_volume': exit_volume,
                'volume_entry': entry_volume,
                'volume_exit': exit_volume,
                'EntryVolume': entry_volume,
                'ExitVolume': exit_volume,
                'atr_entry': entry_atr,
                'atr_exit': exit_atr,
                'EntryATR': entry_atr,
                'ExitATR': exit_atr,
                'entry_sma_short': entry_sma_short,
                'exit_sma_short': exit_sma_short,
                'entry_sma_long': entry_sma_long,
                'exit_sma_long': exit_sma_long,
                'EntrySMA_Short': entry_sma_short,
                'ExitSMA_Short': exit_sma_short,
                'EntrySMA_Long': entry_sma_long,
                'ExitSMA_Long': exit_sma_long,
                'entry_rsi': entry_rsi,
                'exit_rsi': exit_rsi,
                'EntryRSI': entry_rsi,
                'ExitRSI': exit_rsi,
                'rationale': f"{'Buy' if net_pnl > 0 else 'Sell'}: short SMA {'crossed above' if net_pnl > 0 else 'crossed below'} long SMA at index {entry_index if net_pnl > 0 else exit_index}",
                'Rationale': f"{'Buy' if net_pnl > 0 else 'Sell'}: short SMA {'crossed above' if net_pnl > 0 else 'crossed below'} long SMA at index {entry_index if net_pnl > 0 else exit_index}",
                # Always include ticker, context, indicators
                'ticker': strategy_params.get('ticker', 'UNKNOWN'),
                'context': list(price_window.values),
                'indicators': {
                    'sma_short': entry_sma_short,
                    'sma_long': entry_sma_long,
                    'rsi': entry_rsi,
                    'atr': entry_atr,
                    'volatility': entry_volatility
                }
            })
            position = None
            entry_index = None
            entry_price = None
            entry_volatility = None
            entry_volume = None
            entry_regime = None
            entry_atr = None
            entry_sma_short = None
            entry_sma_long = None
            entry_rsi = None
    return trades, trade_log

def rsi_strategy_backtest(data: pd.DataFrame, period: int, overbought: float, oversold: float, strategy_params: dict = None):
    data = data.copy()
    delta = data['close'].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=period, min_periods=period).mean()
    avg_loss = loss.rolling(window=period, min_periods=period).mean()
    rs = avg_gain / avg_loss
    data['rsi'] = 100 - (100 / (1 + rs))
    signals = []
    trade_log = []
    position = None
    entry_index = None
    entry_price = None
    commission = 0.0
    slippage = 0.0
    if strategy_params:
        commission = strategy_params.get('commission', 0.0)
        slippage = strategy_params.get('slippage', 0.0)
    for idx, row in data.iterrows():
        if row['rsi'] < oversold and position != 'long':
            signals.append({'action': 'buy', 'index': idx})
            position = 'long'
            entry_index = idx
            entry_price = row['close']
        elif row['rsi'] > overbought and position == 'long':
            signals.append({'action': 'sell', 'index': idx})
            exit_index = idx
            exit_price = row['close']
            adj_entry, adj_exit, net_pnl, commission_cost = apply_transaction_costs(entry_price, exit_price, commission, slippage)
            trade_log.append({
                'entry_index': entry_index,
                'exit_index': exit_index,
                'entry_price': adj_entry,
                'exit_price': adj_exit,
                'pnl': net_pnl,
                'commission_cost': commission_cost,
                'rationale': f"{'Buy' if net_pnl > 0 else 'Sell'}: RSI strategy trade",
                # Always include ticker, context, indicators
                'ticker': strategy_params.get('ticker', 'UNKNOWN') if strategy_params else 'UNKNOWN',
                'context': [],
                'indicators': {
                    'rsi': row['rsi']
                }
            })
            position = None
            entry_index = None
            entry_price = None
    return signals, trade_log

def export_backtest_results(trade_log, metrics, output_path):
    """
    Export trade log and metrics to a JSON file for report generation.
    """
    import json
    data = {'trade_log': trade_log, 'metrics': metrics}
    data = convert_numpy_types(data)
    with open(output_path, 'w') as f:
        json.dump(data, f)

def portfolio_backtest(data_dict, initial_cash, position_size, strategy_params):
    """
    Unified portfolio-level backtest for multiple tickers, simulating shared cash, position sizing, and time-step-based trade selection.
    data_dict: dict of ticker -> pd.DataFrame with 'close' column
    Returns: {'portfolio_state': PortfolioState, 'trade_log': list, 'strategy_params': dict, 'assets': tickers}
    """
    if strategy_params is None:
        raise ValueError("strategy_params must be provided (from config.json)")
    from tech_analysis.portfolio import PortfolioState
    pf = PortfolioState(initial_cash, strategy_params=strategy_params)
    trade_log = []
    tickers = list(data_dict.keys())
    max_len = max(len(df) for df in data_dict.values())
    last_prices = {ticker: data_dict[ticker]['close'].iloc[0] for ticker in tickers}
    # For each time step, evaluate all tickers and buy if signal, respecting cash and position size
    for i in range(1, max_len):
        for ticker in tickers:
            df = data_dict[ticker]
            if i >= len(df):
                continue
            price = df['close'].iloc[i]
            prev_price = df['close'].iloc[i-1]
            last_prices[ticker] = price
            # Simple signal: buy if price increased from previous step
            signal = price > prev_price
            if signal and pf.cash >= position_size:
                qty = int(position_size // price)
                if qty > 0:
                    pf.buy(ticker, price, qty, f"Buy: {ticker} at index {i} due to price increase")
                    trade_log.append({
                        'ticker': ticker,
                        'action': 'buy',
                        'qty': qty,
                        'price': price,
                        'index': i,
                        'rationale': f"Buy: {ticker} at index {i} due to price increase"
                    })
        pf.update_equity(last_prices)
    result = {
        'portfolio_state': pf,
        'trade_log': trade_log,
        'strategy_params': strategy_params,
        'assets': tickers
    }
    return result

# Utility to load config and fetch data with timeframe/frequency
import json
import os
from tech_analysis.data.fetcher import fetch_all_stocks_data

def load_config():
    # Always resolve config.json relative to project root
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    config_path = os.path.join(project_root, 'config.json')
    with open(config_path, 'r') as f:
        cfg = json.load(f)
    return cfg

# Example utility to get data for backtests using new config fields
def get_data_for_backtest():
    cfg = load_config()
    return fetch_all_stocks_data(
        period=cfg.get('period'),
        start_date=cfg.get('start_date'),
        end_date=cfg.get('end_date'),
        frequency=cfg.get('frequency')
    )
