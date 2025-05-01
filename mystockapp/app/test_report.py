import pytest

# Minimal stub for report generation (to be implemented later)
def generate_report(results):
    return results

def test_report_contains_required_metrics():
    # Define minimal fake results
    fake_results = {
        'sharpe_ratio': 1.2,
        'max_drawdown': -0.15,
        'win_rate': 0.55,
        'trades': 20
    }
    report = generate_report(fake_results)
    # The test expects the report to contain all required metrics as keys
    for metric in ['sharpe_ratio', 'max_drawdown', 'win_rate', 'trades']:
        assert metric in report, f"Report missing required metric: {metric}" 