import quandl

quandl.ApiConfig.api_key = 'fRsTyQJZaBbXBcKsnahq'
stock_price = quandl.get('BSE/BOM500325', start_date='2018-11-26', end_date='2018-11-26')
print (stock_price)
print (type(stock_price))
