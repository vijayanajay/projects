"""
Utility module for standardized NaN handling across all components.

This module provides a consistent interface for detecting and handling NaN values
in DataFrames across the main.py, app.py, scanner.py, and other components.
"""

import pandas as pd
import numpy as np
import logging

# Setup logging
logger = logging.getLogger(__name__)


def detect_nan_columns(df, critical_columns=None):
    """
    Detect NaN values in a DataFrame, with emphasis on critical columns.

    Args:
        df (pd.DataFrame): DataFrame to check for NaN values
        critical_columns (list, optional): List of column names that are considered critical.
                                           If None, all columns are considered critical.

    Returns:
        pd.Series: Series with count of NaN values per column (only columns with NaNs)
        bool: True if critical columns contain NaNs, False otherwise
    """
    if df is None or df.empty:
        return pd.Series(), False

    # Count NaNs in all columns
    nan_counts = df.isna().sum()

    # Filter to only columns with NaNs
    nan_columns = nan_counts[nan_counts > 0]

    # Check critical columns if specified
    critical_columns_have_nans = False
    if critical_columns is not None:
        # Ensure all specified critical columns exist in the DataFrame
        existing_critical_cols = [
            col for col in critical_columns if col in df.columns
        ]
        if existing_critical_cols:
            critical_nan_counts = df[existing_critical_cols].isna().sum()
            critical_columns_have_nans = (critical_nan_counts > 0).any()
    else:
        # If no critical columns specified, consider all columns with NaNs as critical
        critical_columns_have_nans = not nan_columns.empty

    return nan_columns, critical_columns_have_nans


def handle_nans(
    df, method="drop", drop_na_threshold=None, critical_columns=None
):
    """
    Handle NaN values in a DataFrame using a consistent strategy.

    Args:
        df (pd.DataFrame): DataFrame to process
        method (str): NaN handling method - one of:
                      'drop' - Drop rows with NaNs based on threshold
                      'fillna' - Fill NaNs with appropriate values (coming in future version)
        drop_na_threshold (float or int, optional):
                      If < 1: Drop rows where more than this fraction of columns are NaN
                      If >= 1: Drop rows where more than this number of columns are NaN
                      If None: Use default threshold of 0.25 (25% of columns)
        critical_columns (list, optional): List of columns considered critical.
                                          If any of these contain NaNs, a warning is logged.

    Returns:
        pd.DataFrame: DataFrame with NaNs handled according to the specified method
        dict: Statistics about NaN handling (rows_before, rows_after, rows_dropped, pct_dropped)
    """
    if df is None or df.empty:
        return df, {
            "rows_before": 0,
            "rows_after": 0,
            "rows_dropped": 0,
            "pct_dropped": 0.0,
        }

    # Detect NaNs in the DataFrame
    nan_columns, critical_have_nans = detect_nan_columns(df, critical_columns)

    # Log warning if critical columns have NaNs
    if critical_have_nans:
        if critical_columns:
            critical_with_nans = [
                col
                for col in critical_columns
                if col in df.columns and df[col].isna().any()
            ]
            logger.warning(
                f"NaN values detected in critical columns: {critical_with_nans}"
            )
        else:
            logger.warning(
                f"NaN values detected in columns: {nan_columns.index.tolist()}"
            )

    rows_before = len(df)
    stats = {
        "rows_before": rows_before,
        "rows_after": rows_before,
        "rows_dropped": 0,
        "pct_dropped": 0.0,
    }

    # Apply NaN handling based on method
    if method == "drop":
        if not nan_columns.empty:  # Only proceed if there are NaNs
            # Handle based on threshold
            if drop_na_threshold is None:
                # Default: drop rows with more than 25% NaNs
                default_threshold = 0.25
                thresh = int((1.0 - default_threshold) * len(df.columns))
                df_result = df.dropna(thresh=thresh)
                logger.info(
                    f"Using default threshold: Dropping rows with more than {default_threshold*100:.1f}% NaN columns"
                )
            elif drop_na_threshold < 1:
                # Interpret as fraction
                thresh = int((1.0 - drop_na_threshold) * len(df.columns))
                df_result = df.dropna(thresh=thresh)
                logger.info(
                    f"Dropping rows with more than {drop_na_threshold*100:.1f}% NaN columns"
                )
            else:
                # Interpret as count
                thresh = len(df.columns) - drop_na_threshold
                if thresh < 0:
                    logger.warning(
                        f"Drop NA threshold ({drop_na_threshold}) is greater than column count ({len(df.columns)}). No rows will be dropped."
                    )
                    thresh = 0
                df_result = df.dropna(thresh=thresh)
                logger.info(
                    f"Dropping rows with more than {drop_na_threshold} NaN columns"
                )

            # Calculate statistics
            rows_after = len(df_result)
            rows_dropped = rows_before - rows_after
            pct_dropped = (
                (rows_dropped / rows_before * 100) if rows_before > 0 else 0.0
            )

            stats.update(
                {
                    "rows_after": rows_after,
                    "rows_dropped": rows_dropped,
                    "pct_dropped": pct_dropped,
                }
            )

            # Log warning if high percentage dropped
            if pct_dropped > 25:
                logger.warning(
                    f"More than 25% of rows ({pct_dropped:.2f}%) were dropped due to NaN values."
                )

            # Log error if all rows dropped
            if rows_after == 0 and rows_before > 0:
                logger.error(
                    "All rows were dropped due to NaN values! Consider adjusting drop_na_threshold."
                )

            return df_result, stats

    # Default: return original DataFrame if no matching method or no NaNs to handle
    return df, stats


def check_dataframe_compatibility(df1, df2, context="DataFrame comparison"):
    """
    Check if two DataFrames are compatible for operations (same columns, same index type).

    Args:
        df1 (pd.DataFrame): First DataFrame
        df2 (pd.DataFrame): Second DataFrame
        context (str): Context for logging

    Returns:
        bool: True if DataFrames are compatible, False otherwise
        str: Information about compatibility issues (empty string if compatible)
    """
    info = ""

    # Check if either DataFrame is None or empty
    if df1 is None or df2 is None:
        return False, f"{context}: One or both DataFrames are None"

    if df1.empty and df2.empty:
        return True, ""  # Both empty is valid

    if df1.empty or df2.empty:
        return (
            False,
            f"{context}: One DataFrame is empty while the other is not",
        )

    # Check index types
    if df1.index.dtype != df2.index.dtype:
        info += f"{context}: Index dtype mismatch: {df1.index.dtype} vs {df2.index.dtype}. "

    # Check timezone awareness
    if isinstance(df1.index, pd.DatetimeIndex) and isinstance(
        df2.index, pd.DatetimeIndex
    ):
        if df1.index.tz != df2.index.tz:
            info += f"{context}: Index timezone mismatch: {df1.index.tz} vs {df2.index.tz}. "

    # Check column compatibility
    df1_cols = set(df1.columns)
    df2_cols = set(df2.columns)

    missing_in_df2 = df1_cols - df2_cols
    missing_in_df1 = df2_cols - df1_cols

    if missing_in_df1 or missing_in_df2:
        info += f"{context}: Column mismatch. "
        if missing_in_df2:
            info += f"Columns in df1 not in df2: {missing_in_df2}. "
        if missing_in_df1:
            info += f"Columns in df2 not in df1: {missing_in_df1}. "

    # Check data types for common columns
    common_cols = df1_cols.intersection(df2_cols)
    dtype_mismatches = []

    for col in common_cols:
        if df1[col].dtype != df2[col].dtype:
            dtype_mismatches.append(
                f"{col}: {df1[col].dtype} vs {df2[col].dtype}"
            )

    if dtype_mismatches:
        info += (
            f"{context}: Data type mismatches: {', '.join(dtype_mismatches)}. "
        )

    return not bool(info), info.strip()


def ensure_compatible_datetime_index(df):
    """
    Ensure a DataFrame has a timezone-aware DatetimeIndex.

    Args:
        df (pd.DataFrame): DataFrame to check/modify

    Returns:
        pd.DataFrame: DataFrame with timezone-aware DatetimeIndex (UTC if none was specified)
    """
    if df is None or df.empty:
        return df

    # Check if index is DatetimeIndex
    if not isinstance(df.index, pd.DatetimeIndex):
        logger.warning(
            "DataFrame index is not a DatetimeIndex. No timezone conversion performed."
        )
        return df

    # Check if timezone aware
    if df.index.tz is None:
        logger.info(
            "Converting timezone-naive DatetimeIndex to timezone-aware (UTC)"
        )
        df_copy = df.copy()
        df_copy.index = df_copy.index.tz_localize("UTC")
        return df_copy

    return df
