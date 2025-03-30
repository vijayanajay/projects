import quandl

quandl.ApiConfig.api_key = 'fRsTyQJZaBbXBcKsnahq'
stock_price = quandl.get('BSE/BOM500325')
info = stock_price.head()
print ('Before removing None: ', len(stock_price))
stock_price.dropna(how='any')
print ('Afte removing None: ', len(stock_price))

