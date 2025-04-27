import unittest
from tech_analysis.data.fetcher import fetch_stock_data, clean_and_validate_data, cache_to_parquet, load_from_parquet
import pandas as pd

class TestDataFetcher(unittest.TestCase):
    def test_fetch_reliance_daily(self):
        df = fetch_stock_data('HCLTECH.NS', period='20y')
        self.assertIsInstance(df, pd.DataFrame)
        print(df)
        self.assertFalse(df.empty)
        self.assertIn('Close', df.columns)

    def test_clean_and_validate_data(self):
        # Create a DataFrame with missing and outlier values
        import numpy as np
        data = {
            'Open': [100, 101, None, 103, 10000],  # 10000 is an outlier
            'Close': [100, None, 102, 103, 104],
            'Volume': [1000, 1050, None, 1100, 1000000]  # 1000000 is an outlier
        }
        df = pd.DataFrame(data)
        cleaned = clean_and_validate_data(df)
        # Assert missing values are handled (e.g., filled or dropped)
        self.assertFalse(cleaned.isnull().any().any(), "There should be no missing values after cleaning.")
        # Assert outliers are handled (e.g., capped or removed)
        self.assertTrue((cleaned['Open'] < 10000).all(), "Outlier in 'Open' should be handled.")
        self.assertTrue((cleaned['Volume'] < 1000000).all(), "Outlier in 'Volume' should be handled.")

    def test_cache_to_parquet(self):
        import os
        data = {
            'Open': [100, 101, 102],
            'Close': [100, 101, 102],
            'Volume': [1000, 1050, 1100]
        }
        df = pd.DataFrame(data)
        filename = 'test_cache.parquet'
        cache_to_parquet(df, filename)
        # Check if file exists
        self.assertTrue(os.path.exists(filename), "Parquet file should be created.")
        # Read back and compare
        df2 = pd.read_parquet(filename)
        pd.testing.assert_frame_equal(df, df2)
        os.remove(filename)

    def test_load_from_parquet(self):
        import os
        data = {
            'Open': [100, 101, 102],
            'Close': [100, 101, 102],
            'Volume': [1000, 1050, 1100]
        }
        df = pd.DataFrame(data)
        filename = 'test_load.parquet'
        df.to_parquet(filename)
        loaded = load_from_parquet(filename)
        pd.testing.assert_frame_equal(df, loaded)
        os.remove(filename)

if __name__ == '__main__':
    unittest.main()
