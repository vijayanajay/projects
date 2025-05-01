import pandas as pd
import numpy as np

def calculate_volume_ma(series, period):
    if not isinstance(series, pd.Series):
        series = pd.Series(series)
    ma = series.rolling(window=period, min_periods=1).mean()
    ma[series.isna()] = np.nan
    return ma

def calculate_rsi(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period, min_periods=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period, min_periods=period).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def calculate_adx(high, low, close, period=14):
    plus_dm = high.diff()
    minus_dm = low.diff()
    plus_dm = np.where((plus_dm > minus_dm) & (plus_dm > 0), plus_dm, 0)
    minus_dm = np.where((minus_dm > plus_dm) & (minus_dm > 0), minus_dm, 0)
    tr1 = high - low
    tr2 = abs(high - close.shift())
    tr3 = abs(low - close.shift())
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    atr = tr.rolling(window=period, min_periods=period).mean()
    plus_di = 100 * pd.Series(plus_dm).rolling(window=period, min_periods=period).sum() / atr
    minus_di = 100 * pd.Series(minus_dm).rolling(window=period, min_periods=period).sum() / atr
    dx = (abs(plus_di - minus_di) / (plus_di + minus_di)).replace([np.inf, -np.inf], np.nan) * 100
    adx = dx.rolling(window=period, min_periods=1).mean()
    return adx

def calculate_macd(series, fast=12, slow=26, signal=9):
    ema_fast = series.ewm(span=fast, adjust=False).mean()
    ema_slow = series.ewm(span=slow, adjust=False).mean()
    macd = ema_fast - ema_slow
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    hist = macd - signal_line
    return macd, signal_line, hist

def calculate_bollinger_bands(series, period=20, num_std=2):
    sma = series.rolling(window=period, min_periods=period).mean()
    std = series.rolling(window=period, min_periods=period).std()
    upper = sma + num_std * std
    lower = sma - num_std * std
    return upper, sma, lower 