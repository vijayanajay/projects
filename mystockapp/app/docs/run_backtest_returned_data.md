# run_backtest Return Value Documentation

## Overview

This document details the structure of the data returned by the `run_backtest` function in `src/backtester.py`. This information is crucial for writing accurate tests and understanding how to interpret backtest results.

## Return Structure

The `run_backtest` function returns a dictionary with the following key components:

```python
{
    "initial_capital": float,  # The starting capital amount
    "final_value": float,      # Final portfolio value (cash + positions)
    "total_return": float,     # Total return as a decimal (e.g., 0.25 for 25%)
    "num_trades": int,         # Total number of executed trades
    "sharpe_ratio": float,     # Sharpe ratio (annualized)
    "max_drawdown": float,     # Maximum drawdown as a decimal
    "trades": [                # List of executed trades, each as a dictionary
        {
            "date": pd.Timestamp,  # Date of the trade
            "type": str,           # "buy" or "sell"
            "shares": float,       # Number of shares transacted
            "actual_price": float, # Execution price including slippage
            "commission": float,   # Commission paid for this trade
            "slippage_cost": float # Cost due to slippage (difference from close price)
        },
        # ... more trades ...
    ],
    "total_commission": float,     # Sum of all commissions paid
    "total_slippage_cost": float,  # Sum of all slippage costs
    "performance": pd.DataFrame    # DataFrame containing daily portfolio performance
}
```

## Notes on Trade Dictionary Structure

Each entry in the `trades` list is a dictionary with the following keys:

1. `date`: Pandas Timestamp object representing when the trade occurred
2. `type`: String, either "buy" or "sell"
3. `shares`: Float, number of shares traded (can be fractional)
4. `actual_price`: Float, the execution price including slippage
5. `commission`: Float, the commission paid for this trade
6. `slippage_cost`: Float, the cost due to slippage (difference from the close price)

### Key Calculations

- **Total cost of a buy trade**: `shares * actual_price + commission`
- **Value of a position**: `shares * actual_price` (excluding commission)
- **Profit/Loss of a sell trade**: `(sell_price - buy_price) * shares - commission`

## Common Test Mistakes

1. **❌ Incorrect**: Accessing `trade["price"]` or `trade["value"]`
   **✅ Correct**: Use `trade["actual_price"]` for price and calculate value as `trade["shares"] * trade["actual_price"]`

2. **❌ Incorrect**: Assuming commissions are included in position value
   **✅ Correct**: Calculate total cost separately as `shares * actual_price + commission`

3. **❌ Incorrect**: Treating `trade["shares"]` as always being whole numbers
   **✅ Correct**: Handle `trade["shares"]` as potentially fractional values

## Example Test Usage

```python
def test_example():
    results = run_backtest(...)

    # Check number of trades
    assert results["num_trades"] > 0

    # Validate a buy trade
    buy_trade = next(t for t in results["trades"] if t["type"] == "buy")
    total_cost = buy_trade["shares"] * buy_trade["actual_price"] + buy_trade["commission"]

    # Validate final portfolio value
    assert results["final_value"] > results["initial_capital"]
```

## Recommendations for Tests

1. Use precise calculations based on the exact structure described above
2. Include small tolerance values when comparing floating-point values: `pytest.approx(expected_value, abs=1e-9)`
3. Verify total trade costs manually rather than expecting a "value" key
4. Check the relationship between trade values and portfolio changes in the performance DataFrame
