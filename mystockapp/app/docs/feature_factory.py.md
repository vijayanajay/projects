# File: D:/Code/projects/mystockapp/app/feature_factory.py

This module defines the `FeatureFactory` class, which is responsible for generating a variety of technical indicators from OHLCV (Open, High, Low, Close, Volume) stock data. It is designed to be configurable, allowing users to specify which types of features to generate and with which parameters. The implementation leverages pandas and numpy for vectorized calculations to ensure performance.

## Main Components:

1.  **`FeatureFactory` Class:**
    *   **Purpose:** The central class that encapsulates the logic for generating technical features.
    *   **`DEFAULT_PARAMS` Class Attribute:** A dictionary holding default parameter sets for each supported feature family (SMA, EMA, RSI, MACD, Bollinger Bands, ATR, Volume). These defaults specify the windows or other parameters to use if custom parameters are not provided.
    *   **`__init__(self, ohlcv_data, feature_families=None, params=None, use_float32=True)` Method:**
        *   **Purpose:** Initializes the factory with the input OHLCV data and configuration.
        *   **Inputs:**
            *   `ohlcv_data` (pd.DataFrame): The input data containing 'Open', 'High', 'Low', 'Close', and 'Volume' columns.
            *   `feature_families` (list, optional): A list of strings specifying which feature families to generate (e.g., `['sma', 'rsi']`). If `None`, all supported families are included.
            *   `params` (dict, optional): A dictionary to override or extend the `DEFAULT_PARAMS`.
            *   `use_float32` (bool): If `True`, generated features are cast to `float32` to save memory; otherwise, `float64` is used. Defaults to `True`.
        *   **Logic:**
            *   Stores a copy of the input `ohlcv_data`.
            *   Validates that the required OHLCV columns are present.
            *   Sets the list of feature families to generate, validating against the known supported families.
            *   Merges the provided `params` with the `DEFAULT_PARAMS`.
            *   Sets the target data type (`self.dtype`) based on `use_float32`.
            *   Converts the 'Open', 'High', 'Low', and 'Close' columns of the internal data copy to the specified `self.dtype`.
    *   **`generate_features(self)` Method:**
        *   **Purpose:** Executes the feature generation pipeline based on the configuration set during initialization.
        *   **Logic:**
            *   Creates a copy of the internal OHLCV DataFrame to add features to.
            *   Iterates through the list of `self.feature_families`.
            *   For each family, it calls the corresponding private helper method (e.g., `_add_sma_features` for 'sma').
            *   After adding all specified features, it drops any rows that contain `NaN` values, which typically occur at the beginning of the DataFrame due to the lookback periods required for indicator calculations.
            *   Logs the number of features generated and the number of rows remaining after dropping NaNs.
        *   **Output:** Returns the pandas DataFrame containing the original OHLCV data plus the newly generated technical feature columns.

2.  **Private Helper Methods (`_add_*_features`)**:
    *   **Purpose:** Each private method (`_add_sma_features`, `_add_ema_features`, `_add_rsi_features`, `_add_macd_features`, `_add_bollinger_bands_features`, `_add_atr_features`, `_add_volume_features`) is responsible for calculating and adding features for a specific family.
    *   **Inputs:** Each method takes the DataFrame (`df`) being built as input.
    *   **Logic:**
        *   Retrieves the relevant parameters (windows, fast/slow/signal periods, std deviations) from `self.params` for its specific feature family.
        *   Uses pandas' built-in functions (`.rolling()`, `.ewm()`, `.diff()`, `.pct_change()`, `.cumsum()`) and numpy operations for vectorized calculations based on the OHLCV columns.
        *   Calculates the indicator values for the specified parameters.
        *   Adds new columns to the input DataFrame `df` with descriptive names (e.g., `sma_50`, `rsi_14`, `macd_12_26_9_line`, `bb_20_2.0_upper`, `atr_14`, `volume_sma_20`).
        *   Includes calculations for related metrics like relative SMAs/EMAs, Bollinger Bands %B and Bandwidth, ATR percentage, Volume ratios, OBV, PVT, and MFI.
        *   Casts the resulting feature columns to `self.dtype`.
    *   **Output:** Returns the modified DataFrame `df` with the new feature columns added.

The module uses logging to track the progress of feature generation. The `if __name__ == "__main__":` block provides an example of how to instantiate the `FeatureFactory` with data fetched by the `data_fetcher` module and generate/print the resulting features.
