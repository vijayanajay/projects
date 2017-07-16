from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select
from time import time
from datetime import datetime
import pandas as pd

Base = declarative_base()


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

class StockSymbol(Base):
    __tablename__ = 'StockSymbol'
    
    stockSymbolKey = Column(Integer, primary_key = True, autoincrement=True)
    name = Column (String(100), nullable = False)
    symbol = Column(String(50), nullable = False, unique = True)
    tickerNumber = Column(Integer, nullable = False, unique = True)

class StockHistory(Base):
    __tablename__ = "StockHistory"
    __table_args__ = {'sqlite_autoincrement': True}
     
    stockHistoryKey = Column (Integer, primary_key= True, autoincrement = True, 
                              unique = True, nullable = False)
    symbol = Column(String(50), ForeignKey('StockSymbol.symbol'))
    date = Column (DateTime)
    openPrice = Column (Float)
    highPrice = Column (Float)
    lowPrice = Column (Float)
    closePrice = Column (Float)
    wap = Column (Float)
    numberOfShares = Column (Integer)
    numberOfTrades = Column (Integer)
    totalTurnover = Column (Float)
    spreadHighLow = Column (Float)
    spreadCloseOpen = Column (Float)

t = time()
print ('creating database')

#Create the database
engine = create_engine('sqlite:///cdb.db')
Base.metadata.create_all(engine)

#Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()

for row in s.query(StockSymbol).all():
    file_name = str(row.tickerNumber) + '.csv'
    
    try:
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
        s.close() #Close the connection

s.close()
print ("Time elapsed: " + str(time() - t) + " s.") #0.091s