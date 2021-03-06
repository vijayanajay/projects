from django.http import HttpResponse
from django.shortcuts import render
from .models import StockSymbol, StockHistory
import pandas as pd
from django.conf import settings
from .utils import *
import csv
import datetime
import logging, quandl

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
    quandl.ApiConfig.api_key = 'fRsTyQJZaBbXBcKsnahq'
    end_date = datetime.datetime.now().strftime("%Y-%m-%d")
    dataReader = quandl.get('NSE/ASHOKLEY', start_date='2010-01-01', end_date=end_date)
    log.debug(dataReader)
    #DO NOT USE THIS FOR ANYTHING EXCEPT FOR TESTING
    #stock =  StockSymbol.objects.get(symbol = 'ASHOKLEY')
    #csv_filename = get_csv_filename(stock)
    #read_csv_file(stock, csv_filename)
    #count = calculate_and_store_daily_returns(stock)
    return HttpResponse(dataReader)

