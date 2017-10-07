from django.conf import settings
from .models import StockSymbol, StockHistory
import os
import pandas as pd
import csv
import datetime
import pytz

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
            history = StockHistory(symbol = stock)
            localTimeZone = pytz.timezone('Asia/Kolkata')
            history.date = localTimeZone.localize(datetime.datetime.strptime(line[0], "%d-%B-%Y"))
            history.openPrice = line[1]
            history.highPrice = line[2]
            history.lowPrice = line[3]
            history.closePrice = line[4]
            history.wap = line[5]
            history.numberOfShares = line[6]
            history.numberOfTrades = line[7]
            history.totalTurnover = line[8]
            history.spreadHighLow = line[11]
            history.spreadCloseOpen = line[12]
            history.save()
    except:
        return 1
    return dataReader

def calculate_and_store_sma3(stock):
    stockHistoryDF = pd.DataFrame(list(StockHistory.objects.filter(symbol = stock).values('author', 'date', 'slug')))
    return stockHistoryDF