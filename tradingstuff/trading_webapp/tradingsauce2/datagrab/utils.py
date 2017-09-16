from django.conf import settings
from .models import StockSymbol, StockHistory
import os
import pandas as pd
import csv

def get_csv_filename(stocksymbol):
    file_name = os.path.join (settings.BASE_DIR, 'datagrab/csvData', (str(
                stocksymbol.tickerNumber) + '.csv'))
    #print (file_name)
    return file_name

def read_csv_file(stock, file_name):
    try:
        dataReader = csv.reader(open(file_name), delimiter=',')
    except:
        #assuming it's always filenotfounderror. Can be something else too, 
        #to check later
        return False
    try:
        for line in dataReader:
            if line[0] == "Date":
                 continue
            history = StockHistory(stock = stock)
            history.date = line[0]
            history.save()
    except:
        return 1
    return dataReader
