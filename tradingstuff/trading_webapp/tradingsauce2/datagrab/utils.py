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
            history_date = localTimeZone.localize(datetime.datetime.strptime(line[0], "%d-%B-%Y"))
            is_existing = StockHistory.objects.filter(symbol = stock, date = history_date).count()
            if is_existing != 0:
                continue
            history.date = history_date
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
    stockHistoryDF = pd.DataFrame(list(StockHistory.objects.filter(symbol = stock).order_by('date').values('date', 'closePrice')))
    stockHistoryDF.insert(2, column="SMA", value=pd.Series(stockHistoryDF["closePrice"]).rolling(window=3).mean())
    stockHistoryDF = stockHistoryDF.fillna(method='bfill')
    for n in (0, len(stockHistoryDF)-1):
        #temp = stockHistory['date']
        row = StockHistory.objects.filter(symbol = stock, date = stockHistoryDF.iloc[n,1])
        if row[0].sma3 == stockHistoryDF.iloc[n,2] and row[0].sma3 != None:
            continue
        row[0].sma3 = stockHistoryDF.iloc[n,2]
        temp = row[0].sma3
        row[0].save()


    return StockHistory.objects.filter(symbol = stock, date = stockHistoryDF.iloc[1,1])