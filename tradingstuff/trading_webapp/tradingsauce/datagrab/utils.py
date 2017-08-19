from django.conf import settings
from .models import StockSymbol, StockHistory

def get_csv_filename(stocksymbol):
    file_name = settings.BASE_DIR + '\csvData\\' + str(
                stocksymbol.tickerNumber) + '.csv'
    print (file_name)
    return file_name