"""
FeatureFactory module for generating technical indicators from OHLCV data.
Implements a configurable feature generation pipeline optimized for performance.
"""

import logging
import numpy as np
import pandas as pd

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


class FeatureFactory:
    """
    Feature factory for generating technical indicators from OHLCV data.

    Supports the following feature families:
    - Moving Averages (SMA, EMA)
    - RSI (Relative Strength Index)
    - MACD (Moving Average Convergence Divergence)
    - Bollinger Bands
    - ATR (Average True Range)
    - Volume Indicators

    All calculations are vectorized for efficiency using NumPy/Pandas.
    """

    # Default parameter sets for each indicator
    DEFAULT_PARAMS = {
        "sma": {"windows": [5, 10, 20, 50, 100, 200]},
        "ema": {"windows": [5, 10, 20, 50, 100, 200]},
        "rsi": {"windows": [6, 14, 21]},
        "macd": {"fast": [8, 12], "slow": [21, 26], "signal": [9]},
        "bollinger_bands": {"window": [20], "std_devs": [2.0]},
        "atr": {"windows": [7, 14, 21]},
        "volume": {"windows": [5, 10, 20, 50]},
    }

    def __init__(
        self, ohlcv_data, feature_families=None, params=None, use_float32=True
    ):
        """
        Initialize the FeatureFactory.

        Args:
            ohlcv_data (pd.DataFrame): DataFrame with OHLCV data
                Required columns: ['Open', 'High', 'Low', 'Close', 'Volume']
            feature_families (list): List of feature families to generate
                If None, generates all available feature families
            params (dict): Custom parameters for feature generation
                If None, uses default parameters
            use_float32 (bool): Whether to use float32 data type for features
        """
        self.ohlcv = ohlcv_data.copy()

        # Verify required columns
        required_cols = ["Open", "High", "Low", "Close", "Volume"]
        missing_cols = [
            col for col in required_cols if col not in self.ohlcv.columns
        ]
        if missing_cols:
            raise ValueError(f"Missing required columns: {missing_cols}")

        # Set feature families
        self.all_families = [
            "sma",
            "ema",
            "rsi",
            "macd",
            "bollinger_bands",
            "atr",
            "volume",
        ]
        self.feature_families = (
            feature_families if feature_families else self.all_families
        )

        # Validate feature families
        invalid_families = [
            f for f in self.feature_families if f not in self.all_families
        ]
        if invalid_families:
            raise ValueError(f"Invalid feature families: {invalid_families}")

        # Set parameters
        self.params = self.DEFAULT_PARAMS.copy()
        if params:
            # Update default params with custom params
            for family, family_params in params.items():
                if family in self.params:
                    self.params[family].update(family_params)

        # Set data type
        self.dtype = np.float32 if use_float32 else np.float64

        # Convert numeric columns to specified dtype
        for col in ["Open", "High", "Low", "Close"]:
            self.ohlcv[col] = self.ohlcv[col].astype(self.dtype)

    def generate_features(self):
        """
        Generate all specified feature families.

        Returns:
            pd.DataFrame: DataFrame with original data and generated features
        """
        logger.info(
            f"Generating features for families: {self.feature_families}"
        )

        # Create a copy of the original DataFrame to add features to
        df = self.ohlcv.copy()

        # Generate features for each specified family
        for family in self.feature_families:
            logger.info(f"Generating {family} features")

            if family == "sma":
                df = self._add_sma_features(df)
            elif family == "ema":
                df = self._add_ema_features(df)
            elif family == "rsi":
                df = self._add_rsi_features(df)
            elif family == "macd":
                df = self._add_macd_features(df)
            elif family == "bollinger_bands":
                df = self._add_bollinger_bands_features(df)
            elif family == "atr":
                df = self._add_atr_features(df)
            elif family == "volume":
                df = self._add_volume_features(df)

        # Drop NaN values resulting from feature calculations
        df = df.dropna()
        logger.info(
            f"Generated {len(df.columns) - 5} features, {len(df)} rows remaining after dropping NaNs"
        )

        return df

    def _add_sma_features(self, df):
        """Add Simple Moving Average features."""
        windows = self.params["sma"]["windows"]
        for window in windows:
            col_name = f"sma_{window}"
            df[col_name] = (
                df["Close"].rolling(window=window).mean().astype(self.dtype)
            )
            # Add SMA relative to close price (normalized) as a percentage
            df[f"{col_name}_rel"] = (
                (df["Close"] / df[col_name]) - 1.0
            ).astype(self.dtype)
        return df

    def _add_ema_features(self, df):
        """Add Exponential Moving Average features."""
        windows = self.params["ema"]["windows"]
        for window in windows:
            col_name = f"ema_{window}"
            df[col_name] = (
                df["Close"]
                .ewm(span=window, adjust=False)
                .mean()
                .astype(self.dtype)
            )
            # Add EMA relative to close price (normalized) as a percentage
            df[f"{col_name}_rel"] = (
                (df["Close"] / df[col_name]) - 1.0
            ).astype(self.dtype)
        return df

    def _add_rsi_features(self, df):
        """Add Relative Strength Index features."""
        windows = self.params["rsi"]["windows"]
        for window in windows:
            # Calculate daily price changes
            delta = df["Close"].diff()

            # Separate gains and losses
            gain = delta.where(delta > 0, 0).astype(self.dtype)
            loss = -delta.where(delta < 0, 0).astype(self.dtype)

            # Calculate average gain and loss over the window
            avg_gain = gain.rolling(window=window).mean()
            avg_loss = loss.rolling(window=window).mean()

            # Calculate relative strength
            rs = avg_gain / avg_loss

            # Calculate RSI
            df[f"rsi_{window}"] = (100 - (100 / (1 + rs))).astype(self.dtype)
        return df

    def _add_macd_features(self, df):
        """Add Moving Average Convergence Divergence features."""
        for fast in self.params["macd"]["fast"]:
            for slow in self.params["macd"]["slow"]:
                if fast >= slow:  # Skip invalid combinations
                    continue

                for signal in self.params["macd"]["signal"]:
                    # Calculate MACD components
                    fast_ema = df["Close"].ewm(span=fast, adjust=False).mean()
                    slow_ema = df["Close"].ewm(span=slow, adjust=False).mean()

                    # MACD Line
                    macd_line = (fast_ema - slow_ema).astype(self.dtype)

                    # Signal Line
                    signal_line = (
                        macd_line.ewm(span=signal, adjust=False)
                        .mean()
                        .astype(self.dtype)
                    )

                    # MACD Histogram
                    histogram = (macd_line - signal_line).astype(self.dtype)

                    # Add to dataframe
                    prefix = f"macd_{fast}_{slow}_{signal}"
                    df[f"{prefix}_line"] = macd_line
                    df[f"{prefix}_signal"] = signal_line
                    df[f"{prefix}_histogram"] = histogram
        return df

    def _add_bollinger_bands_features(self, df):
        """Add Bollinger Bands features."""
        for window in self.params["bollinger_bands"]["window"]:
            for std_dev in self.params["bollinger_bands"]["std_devs"]:
                # Calculate middle band (SMA)
                middle_band = df["Close"].rolling(window=window).mean()

                # Calculate standard deviation
                std = df["Close"].rolling(window=window).std()

                # Calculate upper and lower bands
                upper_band = (middle_band + (std * std_dev)).astype(self.dtype)
                lower_band = (middle_band - (std * std_dev)).astype(self.dtype)

                # Add bands to dataframe
                prefix = f"bb_{window}_{std_dev}"
                df[f"{prefix}_upper"] = upper_band
                df[f"{prefix}_middle"] = middle_band.astype(self.dtype)
                df[f"{prefix}_lower"] = lower_band

                # Add %B indicator: (Price - Lower) / (Upper - Lower)
                df[f"{prefix}_percent_b"] = (
                    (df["Close"] - lower_band) / (upper_band - lower_band)
                ).astype(self.dtype)

                # Add bandwidth indicator: (Upper - Lower) / Middle
                df[f"{prefix}_bandwidth"] = (
                    (upper_band - lower_band) / middle_band
                ).astype(self.dtype)
        return df

    def _add_atr_features(self, df):
        """Add Average True Range features."""
        for window in self.params["atr"]["windows"]:
            # Calculate True Range
            high_low = df["High"] - df["Low"]
            high_close_prev = abs(df["High"] - df["Close"].shift(1))
            low_close_prev = abs(df["Low"] - df["Close"].shift(1))

            # True Range is the maximum of the three
            tr = pd.concat(
                [high_low, high_close_prev, low_close_prev], axis=1
            ).max(axis=1)

            # Calculate ATR
            atr = tr.rolling(window=window).mean().astype(self.dtype)

            # Add to dataframe
            df[f"atr_{window}"] = atr

            # Add ATR as percentage of close price
            df[f"atr_{window}_pct"] = (atr / df["Close"]).astype(self.dtype)
        return df

    def _add_volume_features(self, df):
        """Add Volume-based features."""
        # Volume moving averages
        for window in self.params["volume"]["windows"]:
            df[f"volume_sma_{window}"] = (
                df["Volume"].rolling(window=window).mean().astype(self.dtype)
            )

            # Volume relative to its moving average
            df[f"volume_sma_{window}_ratio"] = (
                df["Volume"] / df[f"volume_sma_{window}"]
            ).astype(self.dtype)

        # On-Balance Volume (OBV)
        obv = pd.Series(0, index=df.index).astype(np.int64)

        for i in range(1, len(df)):
            if df["Close"].iloc[i] > df["Close"].iloc[i - 1]:
                obv.iloc[i] = obv.iloc[i - 1] + df["Volume"].iloc[i]
            elif df["Close"].iloc[i] < df["Close"].iloc[i - 1]:
                obv.iloc[i] = obv.iloc[i - 1] - df["Volume"].iloc[i]
            else:
                obv.iloc[i] = obv.iloc[i - 1]

        df["obv"] = obv

        # OBV moving average
        df["obv_sma_10"] = (
            df["obv"].rolling(window=10).mean().astype(self.dtype)
        )

        # Price-Volume Trend (PVT)
        price_change_pct = df["Close"].pct_change()
        df["pvt"] = (
            (price_change_pct * df["Volume"]).cumsum().astype(self.dtype)
        )

        # Money Flow Index components
        typical_price = (df["High"] + df["Low"] + df["Close"]) / 3
        money_flow = typical_price * df["Volume"]

        # Positive and negative money flow
        positive_flow = money_flow.where(
            typical_price > typical_price.shift(1), 0
        ).astype(self.dtype)
        negative_flow = money_flow.where(
            typical_price < typical_price.shift(1), 0
        ).astype(self.dtype)

        # Money Flow Index (14-period)
        period = 14
        positive_mf = positive_flow.rolling(window=period).sum()
        negative_mf = negative_flow.rolling(window=period).sum()

        money_ratio = positive_mf / negative_mf
        df["mfi_14"] = (100 - (100 / (1 + money_ratio))).astype(self.dtype)

        return df


if __name__ == "__main__":
    # Example usage
    import data_fetcher

    # Fetch data
    data = data_fetcher.get_reliance_data()

    if data is not None:
        # Create feature factory with default settings
        factory = FeatureFactory(data)

        # Generate all features
        features_df = factory.generate_features()

        # Print feature info
        print(f"Generated DataFrame shape: {features_df.shape}")
        print(f"Feature columns: {list(features_df.columns)}")

        # Print sample of the data
        print("\nSample data:")
        print(features_df.iloc[-5:, :10])  # Last 5 rows, first 10 columns
