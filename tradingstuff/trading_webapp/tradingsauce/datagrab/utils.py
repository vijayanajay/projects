from django.conf import settings
from .models import StockSymbol, StockHistory
import os

def get_csv_filename(stocksymbol):
    file_name = os.path.join (settings.BASE_DIR, 'datagrab\csvData', (str(
                stocksymbol.tickerNumber) + '.csv'))
    #print (file_name)
    return file_name

def read_csv_file(file_name):
    try: 
        file = open (file_name, "r")
    except:
        #assuming it's always filenotfounderror. Can be something else too, 
        #to check later
        return False
    return file