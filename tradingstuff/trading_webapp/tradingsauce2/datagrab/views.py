from django.http import HttpResponse
from django.shortcuts import render
from .models import StockSymbol, StockHistory
import pandas as pd
from django.conf import settings
from .utils import *
import csv
import datetime
import logging

log = logging.getLogger(__name__)

def index(request):
    symbols = StockSymbol.objects.all()   
    for symbol in symbols:
        file_name = settings.BASE_DIR + '/csvData/' + str(
                symbol.tickerNumber) + '.csv'        
        #csvData = Load_Data (file_name, symbol.symbol)
    return HttpResponse (file_name) 
"""try:
        csvData = Load_Data(file_name, row.symbol)
        print ("row.symbol = ", row.symbol)
        #dbData = s.query(StockHistory).filter(StockHistory.symbol == row.symbol).all()
        dataFromTable = select()
        csvData.to_sql('StockHistory', engine, if_exists='append')
    except Exception as e:
        print ('exception = ', e, type (e))
        s.rollback() #Rollback the changes on error
        print ('error in reading')
    finally:
        s.close()
"""
    

def Load_Data(file_name, symbol):
    log.debug("inside views.Load_Data")
    data = pd.read_csv(file_name)
    data.insert (0, column = 'symbol', value = symbol)
    data.columns = ['symbol', 'date', 'openPrice', 'highPrice', 'lowPrice', 
                    'closePrice', 'wap', 'numberOfShares', 'numberOfTrades',
                    'totalTurnover', 'todel1', 'todel2', 'spreadHighLow',
                    'spreadCloseOpen']
    del data['todel1']
    del data['todel2']
    data.index += 1
    data.index.names = ['stockHistoryKey']
    return data

def test(request):
    log.debug("inside views.test")
    #DO NOT USE THIS FOR ANYTHING EXCEPT FOR TESTING
    stock =  StockSymbol.objects.get(symbol = 'ASHOKLEY')
    csv_filename = get_csv_filename(stock)
    #count = read_csv_file(stock, csv_filename)
    dataReader = csv.reader(open(csv_filename), delimiter=',')
    test_DF = pd.DataFrame(
        list(StockHistory.objects.filter(symbol=stock).order_by('date').values('id', 'date')))
    if test_DF.empty:
        test_DF = pd.DataFrame(columns=[['id', 'date']])
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
    #count = calculate_and_store_sma3(stock)
    return HttpResponse(count)

