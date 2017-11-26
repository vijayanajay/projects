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
    test_DF = pd.DataFrame(
        list(StockHistory.objects.filter(symbol=stock).order_by('date').values('id', 'date')))
    if test_DF.empty:
        test_DF = pd.DataFrame(columns=[['id', 'date']])
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
            localTimeZone = pytz.timezone('Asia/Kolkata')
            history_date = localTimeZone.localize(datetime.datetime.strptime(line[0], "%d-%B-%Y"))
            is_existing = test_DF[test_DF['date'] == history_date]
            if is_existing.empty == False:
                continue
            history = StockHistory(symbol=stock)
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
        return 3
    log.debug("completed read_csv_file")
    return dataReader

def calculate_and_store_sma3(stock):
    log.debug("inside utils.calculate_and_store_sma3")
    originalDF = pd.DataFrame(
        list(StockHistory.objects.filter(symbol=stock).order_by('date').values('id', 'closePrice', 'sma3')))
    updatedDF = originalDF[['id', 'closePrice']]
    updatedDF.insert(2, column="sma3", value=pd.Series(updatedDF["closePrice"]).rolling(window=3).mean())
    updatedDF = updatedDF.fillna(method='bfill')
    insertToDbDF = pd.DataFrame(data=None, columns=['id', 'closePrice', 'sma3'])

    for n in range(0, len(updatedDF), 1):
        first_condition = updatedDF.iloc[n,2] == originalDF.iloc[n,2]
        second_condition = originalDF.iloc[n,2] != None
        if first_condition and second_condition:
            continue
        insertToDbDF.loc[n] = updatedDF.loc[n]
        #db_row = StockHistory.objects.get(id = row_real["id"])
        #row[0].save(

    return insertToDbDF.values