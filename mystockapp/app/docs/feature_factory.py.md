# Feature Factory Documentation

This file provides specific documentation for the `feature_factory.py` module, which is responsible for generating a variety of technical indicators from OHLCV (Open, High, Low, Close, Volume) stock data.

## Overview

The `FeatureFactory` class is designed to be configurable, allowing users to specify which types of features to generate and with which parameters. The implementation leverages pandas and numpy for vectorized calculations to ensure performance.

## Main Components

### `FeatureFactory` Class

The central class that encapsulates the logic for generating technical features.

#### `DEFAULT_PARAMS` Class Attribute

A dictionary holding default parameter sets for each supported feature family:
- SMA (Simple Moving Averages)
- EMA (Exponential Moving Averages)
- RSI (Relative Strength Index)
- MACD (Moving Average Convergence Divergence)
- Bollinger Bands
- ATR (Average True Range)
- Volume Indicators

#### Initialization

```python
def __init__(self, ohlcv_data, feature_families=None, params=None, indicator_params=None, use_float32=True):
```

- **ohlcv_data** (pd.DataFrame): Input data with 'Open', 'High', 'Low', 'Close', and 'Volume' columns
- **feature_families** (list, optional): Which feature families to generate (e.g., `['sma', 'rsi']`)
- **params** (dict, optional): DEPRECATED - Use indicator_params instead
- **indicator_params** (dict, optional): Dictionary to override or extend DEFAULT_PARAMS
- **use_float32** (bool): If True, features are cast to float32 to save memory

#### Feature Generation

```python
def generate_features(self, drop_na=False, drop_na_threshold=None):
```

- **drop_na** (bool): Whether to drop rows with NaN values within the factory
- **drop_na_threshold** (float or int): Controls NaN dropping behavior:
  - If < 1: Drops rows where more than this fraction of values are NaN
  - If >= 1: Drops rows where more than this number of columns have NaN values
  - If None and drop_na=True: Any row with a NaN is dropped

## NaN Handling

The FeatureFactory itself can handle NaNs during feature generation, but the recommended approach is:

1. Generate features with `drop_na=False` in FeatureFactory
2. Handle NaNs externally (e.g., in main.py) after feature generation but before signal generation
3. This ensures signals are not generated on incomplete data rows

This approach prevents signals being generated on data rows that still contain NaNs from indicator lookback periods, which could lead to unexpected signal behavior.

## Example Usage

```python
# Create the factory with data and configuration
factory = FeatureFactory(
    ohlcv_data=data,
    feature_families=['sma', 'rsi', 'macd'],
    indicator_params={
        'sma': {'windows': [20, 50, 200]},
        'rsi': {'windows': [14]}
    }
)

# Generate features without dropping NaNs in the factory
df_with_features = factory.generate_features(drop_na=False)

# Handle NaNs externally before generating signals
df_with_features = df_with_features.dropna()

# Now generate signals on clean data
strategy = SomeStrategy()
df_with_signals = strategy.generate_signals(df_with_features)
```

## Feature Families

The following feature families are supported:

1. **SMA**: Simple Moving Averages with configurable windows
2. **EMA**: Exponential Moving Averages with configurable windows
3. **RSI**: Relative Strength Index with configurable windows
4. **MACD**: Moving Average Convergence Divergence with configurable fast/slow/signal periods
5. **Bollinger Bands**: With configurable window and std deviation
6. **ATR**: Average True Range with configurable window
7. **Volume**: Various volume-based indicators including OBV, PVT, and MFI

Each family has its own set of parameters that can be configured via the indicator_params argument.
