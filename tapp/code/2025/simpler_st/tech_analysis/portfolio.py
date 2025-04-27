class PortfolioState:
    def __init__(self, starting_cash, strategy_params=None):
        self.cash = starting_cash
        self.holdings = {}  # ticker -> quantity
        self.transaction_log = []
        self.equity_curve = []  # Track portfolio value over time
        self.strategy_params = strategy_params or {}

    def buy(self, ticker, qty, price, rationale):
        total_cost = qty * price
        if self.cash < total_cost:
            raise ValueError("Insufficient cash")
        self.cash -= total_cost
        self.holdings[ticker] = self.holdings.get(ticker, 0) + qty
        self.log_trade('buy', ticker, qty, price, rationale)

    def sell(self, ticker, qty, price, rationale):
        if self.holdings.get(ticker, 0) < qty:
            raise ValueError("Cannot short sell or sell more than held")
        self.cash += qty * price
        self.holdings[ticker] -= qty
        self.log_trade('sell', ticker, qty, price, rationale)

    def log_trade(self, action, ticker, qty, price, rationale):
        self.transaction_log.append({
            'action': action,
            'ticker': ticker,
            'qty': qty,
            'price': price,
            'rationale': rationale
        })

    def update_equity(self, price_dict):
        """
        Update the equity curve by calculating total portfolio value (cash + holdings at current prices).
        price_dict: dict of ticker -> current price
        """
        holdings_value = sum(self.holdings.get(ticker, 0) * price_dict.get(ticker, 0) for ticker in self.holdings)
        total_value = self.cash + holdings_value
        self.equity_curve.append(total_value)
