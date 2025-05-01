import pandas as pd
from typing import List, Tuple

def generate_walk_forward_periods(dates: pd.DatetimeIndex, train_years: int, test_months: int) -> List[Tuple[slice, slice]]:
    periods = []
    n = len(dates)
    start = 0
    while True:
        # Find train period end
        train_end = start
        train_days = 0
        while train_end < n and train_days < train_years * 365:
            if train_end > start:
                train_days = (dates[train_end] - dates[start]).days
            train_end += 1
        if train_end >= n:
            break
        # Find test period end
        test_start = train_end
        test_end = test_start
        test_days = 0
        while test_end < n and test_days < test_months * 30:
            if test_end > test_start:
                test_days = (dates[test_end] - dates[test_start]).days
            test_end += 1
        if test_end > n:
            test_end = n
        if test_start >= n or test_end <= test_start:
            break
        periods.append((slice(start, train_end), slice(test_start, test_end)))
        start = test_end
    return periods 