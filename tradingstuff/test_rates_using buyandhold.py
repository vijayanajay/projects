import urllib,datetime
from decimal import *
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as wb

class Quote(object):
  
  DATE_FMT = '%Y-%m-%d'
  TIME_FMT = '%H:%M:%S'
  
  def __init__(self):
    self.symbol = ''
    self.date,self.time,self.open_,self.high,self.low,self.close,self.volume = ([] for _ in range(7))
    getcontext().prec = 6

  def append(self,dt,open_,high,low,close,volume):
    self.date.append(dt.date())
    self.time.append(dt.time())
    self.open_.append(float(open_))
    self.high.append(float(high))
    self.low.append(float(low))
    self.close.append(float(close))
    self.volume.append(int(volume))
      
  def to_csv(self):
    return ''.join(["{0},{1},{2},{3:.6f},{4:.6f},{5:.6f},{6:.6f},{7}\n".format(self.symbol,
              self.date[bar].strftime('%Y-%m-%d: %H:%M:%S'),self.time[bar].strftime('%H:%M:%S'),
              self.open_[bar],self.high[bar],self.low[bar],self.close[bar],self.volume[bar]) 
              for bar in range(len(self.close))])
    
  def write_csv(self,filename):
    with open(filename,'w') as f:
      f.write(self.to_csv())
        
  def read_csv(self,filename):
    self.symbol = ''
    self.date,self.time,self.open_,self.high,self.low,self.close,self.volume = ([] for _ in range(7))
    for line in open(filename,'r'):
      symbol,ds,ts,open_,high,low,close,volume = line.rstrip().split(',')
      self.symbol = symbol
      dt = datetime.datetime.strptime(ds+' '+ts,self.DATE_FMT+' '+self.TIME_FMT)
      self.append(dt,open_,high,low,close,volume)
    return True

  def __repr__(self):
    return self.to_csv()

class GoogleIntradayQuote(Quote):
  ''' Intraday quotes from Google. Specify interval seconds and number of days '''
  def __init__(self,symbol,interval_seconds=300,num_days=5):
    super(GoogleIntradayQuote,self).__init__()
    self.symbol = symbol.upper()
    url_string = "http://www.google.com/finance/getprices?q={0}".format(self.symbol)
    url_string += "&i={0}&p={1}d&f=d,o,h,l,c,v".format(interval_seconds,num_days)
    csv = urllib.request.urlopen(url_string).readlines()
    for n in range(0, len(csv)): csv[n] = csv[n].decode("utf-8") 
    for bar in range(7,len(csv)):
      if csv[bar].count(',')!=5: continue
      offset,close,high,low,open_,volume = csv[bar].split(',')
      if offset[0]=='a':
        day = float(offset[1:])
        offset = 0
      else:
        offset = float(offset)
      open_,high,low,close = [float(x) for x in [open_,high,low,close]]
      dt = datetime.datetime.fromtimestamp(day+(interval_seconds*offset))
      self.append(dt,open_,high,low,close,volume)
   
   

#from pandas_datareader import web
def relative_strength_index(df, n):
    dUp = df > 0
    dDown = df < 0
    
    RollUp=pd.Series(dUp).rolling(window=n).mean() 
    RollDown=pd.Series(dDown).rolling(window=n).mean().abs()
    
    RS = RollUp / RollDown
    rsi= 100.0 - (100.0 / (1.0 + RS))
    return rsi


#q = GoogleIntradayQuote('EURUSD',60,5)
#q.write_csv("EurUsd.csv")
#q.write_csv('EURUSD.csv')

data = pd.read_csv('EURUSD.csv', header=None, names=["Symbol", "Date","Time", "Open", 
                                                     "High", "Low", "Adj Close",
                                                     "Volume"])



X = pd.DataFrame(data = data[["Volume", "Adj Close"]])
#filter all o volume days
#X = X[X["Volume"]!=0]

#Configuration of days
rollingdays = 3
ewma_fast_days = 2
ewma_slow_days = 15

X.insert(2, column="SMA", value = pd.Series(X["Adj Close"]).rolling(window=rollingdays).mean())
X.insert(3, column="Daily_Returns", value = X.iloc[1:,1] / X.iloc[:-1, 1].values - 1)
X.insert(4, column="RSI3", value = relative_strength_index(X["Daily_Returns"],rollingdays))

emaSlow =  pd.Series(X["Adj Close"]).ewm(adjust=True,ignore_na=False,span=ewma_slow_days,min_periods=1).mean()
emaFast =  pd.Series(X["Adj Close"]).ewm(adjust=True,ignore_na=False,span=ewma_fast_days,min_periods=1).mean()
X.insert(5, column="MACD", value = emaFast - emaSlow)

low_min = pd.Series(X["Adj Close"]).rolling(window=rollingdays).min()
high_max = pd.Series(X["Adj Close"]).rolling(window=rollingdays).max()
k_fast = 100 * (X["Adj Close"] - low_min)/(high_max - low_min)
d_fast = k_fast.rolling(window=3).mean()

X.insert(6, column="K_Stok", value = k_fast)
X.insert(7, column="D_Stok", value = d_fast)

will_r = 100 * (high_max - X["Adj Close"])/(high_max - low_min)
X.insert(8, column="Will_R", value = will_r)
X.iloc[:,2:] = X.iloc[:,2:].fillna(method='bfill')

test = pd.Series(pd.Series(X["SMA"]).rolling(window=3))

x = [X.iloc[n:n+6,2] for n in range(0, len(X["SMA"]))]
interval_trend = [pd.Series(x[n]).is_monotonic for n in range(0,len(x))]

trend=[]
for n in range(0,len(interval_trend)):
    if X.iloc[n,1] > X.iloc[n,2] and interval_trend[n]:
        trend.append(1)
    elif X.iloc[n,1] < X.iloc[n,2] and not interval_trend[n]:
        trend.append(0.5)
        #trend[n] = "Down"
    else:
        trend.append(0)
        #trend[n] = "nothing"

#correct trend to contain only single buy
buy = False
sell = False
for n in range (0,len(trend)):
    if trend[n]==1:
        sell = False
        if buy == True:
            trend[n]= 0.5
        if buy == False: 
            buy = True 
            lastBuyPrice = X.iloc[n,1]
    if trend[n]==0: 
        buy = False
        if sell == True:
            trend[n]= 0.5
        if sell == False: 
            sell = True


#checking earnings of last 1 year
initialAmount = finalamount = 100
lastBuyPrice = 0
numberoftrades = 0
tradeHistory = pd.DataFrame(columns=[["Buy Price", "Number of Stocks", "Sell Price", "Earned", "Final Amount", "Number of Days", "Percentage"]])
for n in range (len(trend)-352,len(trend)):
    if trend[n]==1:
        lastBuyPrice = X.iloc[n,1]
        #print ("last buy price =", lastBuyPrice)
        numberofstocks = finalamount/lastBuyPrice
        #print ("number of stocks = ", numberofstocks)
        tradeHistory.set_value(numberoftrades, "Buy Price", lastBuyPrice)
        tradeHistory.set_value(numberoftrades, "Number of Stocks", numberofstocks)
        buyDate = X.iloc[n].name
    if trend[n]==0: 
        #print ("sell price =", X.iloc[n,1])
        if tradeHistory.empty == True: continue
        finalamount =  X.iloc[n,1]*numberofstocks
        if finalamount <= 0: 
            finalamount = 1000
            initialAmount += 1000
        #print ("final amount =", finalamount)
        print (n)
        tradeHistory.set_value(numberoftrades, "Sell Price", X.iloc[n,1])
        tradeHistory.set_value(numberoftrades, "Earned",  (X.iloc[n,1]- lastBuyPrice)*numberofstocks)
        tradeHistory.set_value(numberoftrades, "Final Amount", finalamount)
        tradeHistory.set_value(numberoftrades, "Number of Days", pd.Timedelta(X.iloc[n].name - buyDate).days)
        tradeHistory.set_value(numberoftrades, "Percentage",  (X.iloc[n,1]- lastBuyPrice)*100/lastBuyPrice )
        numberoftrades += 1
        
                          
 #toplot = pd.Series(data = "0", index=X[1300:].index)
tobuy = pd.Series()
tosell= pd.Series()
for n in range(1300,len(X["Adj Close"])):
    if trend[n]==1: 
        tobuy.set_value(X.iloc[n].name, X.iloc[n,1])
    if trend[n]==0: 
        tosell.set_value(X.iloc[n].name, X.iloc[n,1]) 
print ("the end")
  
  
"""