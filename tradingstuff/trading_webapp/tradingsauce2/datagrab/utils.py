from django.conf import settings
from .models import StockSymbol, StockHistory
import os
import pandas as pd
import csv
import datetime
import pytz
import logging

log = logging.getLogger(__name__)

def get_csv_filename(stocksymbol):
    file_name = os.path.join (settings.BASE_DIR, 'datagrab/csvData', (str(
                stocksymbol.tickerNumber) + '.csv'))
    #print (file_name)
    return file_name

def read_csv_file(stock, file_name):
    log.debug("inside read_csv_file")
    try:
        dataReader = csv.reader(open(file_name), delimiter=',')
    except:
        #assuming it's always filenotfounderror. Can be something else too,
        #to check later
        log.debug("completed read_csv_file with exception in reading csv file")
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
        log.debug("completed read_csv_file with exception in inserting into db")
        return 1
    log.debug("completed read_csv_file")
    return dataReader

def calculate_and_store_sma3(stock):
    log.debug("inside utils.calculate_and_store_sma3")
    stockHistoryDF = pd.DataFrame(list(StockHistory.objects.filter(symbol = stock).order_by('date').values('id', 'date', 'closePrice')))
    originalDF = pd.DataFrame(list(StockHistory.objects.filter(symbol = stock).order_by('date').values('id', 'date', 'closePrice','sma3')))
    stockHistoryDF.insert(3, column="SMA", value=pd.Series(stockHistoryDF["closePrice"]).rolling(window=3).mean())
    stockHistoryDF = stockHistoryDF.fillna(method='bfill')
    temp_list = []

    for n in range(0, len(stockHistoryDF), 1):
        row = StockHistory.objects.filter(id = stockHistoryDF.iloc[n,2])
        #row_real = originalDF.loc(originalDF['id'] == stockHistoryDF.iloc[n,2])
        #
        if row[0].sma3 == stockHistoryDF.iloc[n,3] and row[0].sma3 != None:
            continue
        row[0].sma3 = stockHistoryDF.iloc[n,3]
        row[0].save()
    return "true"