def log_trade_event(trade_event):
    # Output CSV string of required fields in order
    fields = ['timestamp', 'symbol', 'price', 'quantity', 'side']
    return ','.join(str(trade_event[field]) for field in fields)

def log_performance_summary(performance_metrics):
    # Output CSV string of all metrics in order of keys
    keys = list(performance_metrics.keys())
    values = [str(performance_metrics[k]) for k in keys]
    return ','.join(values) 