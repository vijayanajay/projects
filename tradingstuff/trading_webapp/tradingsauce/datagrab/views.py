from django.http import HttpResponse
from django.shortcuts import render
from .models import StockSymbol, StockHistory
import pandas as pd
from django.conf import settings

def index(request):
    symbols = StockSymbol.objects.all()   
    for symbol in symbols:
        file_name = settings.BASE_DIR + '\csvData\\' + str(
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