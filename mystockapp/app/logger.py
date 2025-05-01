def log_trade_event(trade_event):
    # Output CSV string of required fields in order
    fields = ['timestamp', 'symbol', 'price', 'quantity', 'side']
    return ','.join(str(trade_event[field]) for field in fields) 