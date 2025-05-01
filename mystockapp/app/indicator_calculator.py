import pandas as pd
import numpy as np

def calculate_volume_ma(series, period):
    if not isinstance(series, pd.Series):
        series = pd.Series(series)
    ma = series.rolling(window=period, min_periods=1).mean()
    ma[series.isna()] = np.nan
    return ma 