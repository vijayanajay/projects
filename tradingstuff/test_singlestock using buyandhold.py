# -*- coding: utf-8 -*-


from datetime import datetime, date
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pandas_datareader.data as wb
#from pandas_datareader import web
def relative_strength_index(df, n):
    dUp = df > 0
    dDown = df < 0
    
    RollUp=pd.Series(dUp).rolling(window=n).mean() 
    RollDown=pd.Series(dDown).rolling(window=n).mean().abs()
    
    RS = RollUp / RollDown
    rsi= 100.0 - (100.0 / (1.0 + RS))
    return rsi

#data = wb.DataReader('MANAPPURAM.NS',  'yahoo', datetime(2010, 1, 1), date.today())
data = wb.DataReader('CHAMBLFERT',  'google', datetime(2010, 1, 1), datetime.now())



X = pd.DataFrame(data = data[["Volume", "Adj Close"]])
X = pd.DataFrame(data = data[["Volume", "Adj Close"]])
X["Adj_Close"] = X["Adj Close"]
del X["Adj Close"]
#filter all o volume days
X = X[X["Volume"]!=0]

#Configuration of days
rollingdays = 3
ewma_fast_days = 5
ewma_slow_days = 12

X.insert(2, column="SMA", value = pd.Series(X["Adj_Close"]).rolling(window=rollingdays).mean())
X.insert(3, column="Daily_Returns", value = X.iloc[1:,1] / X.iloc[:-1, 1].values - 1)
X.insert(4, column="RSI3", value = relative_strength_index(X["Daily_Returns"],rollingdays))

emaSlow =  pd.Series(X["Adj_Close"]).ewm(adjust=True,ignore_na=False,span=ewma_slow_days,min_periods=1).mean()
emaFast =  pd.Series(X["Adj_Close"]).ewm(adjust=True,ignore_na=False,span=ewma_fast_days,min_periods=1).mean()
X.insert(5, column="MACD", value = emaFast - emaSlow)

low_min = pd.Series(X["Adj_Close"]).rolling(window=rollingdays).min()
high_max = pd.Series(X["Adj_Close"]).rolling(window=rollingdays).max()
k_fast = 100 * (X["Adj_Close"] - low_min)/(high_max - low_min)
d_fast = k_fast.rolling(window=3).mean()

X.insert(6, column="K_Stok", value = k_fast)
X.insert(7, column="D_Stok", value = d_fast)

will_r = 100 * (high_max - X["Adj_Close"])/(high_max - low_min)
X.insert(8, column="Will_R", value = will_r)
X.iloc[:,2:] = X.iloc[:,2:].fillna(method='bfill')

test = pd.Series(pd.Series(X["SMA"]).rolling(window=3))

x = [X.iloc[n-6:n,2] for n in range(6, len(X["SMA"]))]
interval_trend = [pd.Series(x[n]).is_monotonic for n in range(0,len(x))]

trend=[]
for n in range(0,len(interval_trend)):
    if X.iloc[n,1] > X.iloc[n,2] and interval_trend[n]:
        trend.append(2)
    elif X.iloc[n,1] < X.iloc[n,2] and not interval_trend[n]:
        trend.append(1)
        #trend[n] = "Down"
    else:
        trend.append(0)
        #trend[n] = "nothing"

#correct trend to contain only single buy
buy = False
sell = False
for n in range (0,len(trend)):
    if trend[n]==2:
        sell = False
        if buy == True:
            trend[n]= 0
        if buy == False: 
            buy = True 
            lastBuyPrice = X.iloc[n,1]
    if trend[n]==1: 
        buy = False
        if sell == True:
            trend[n]= 0
        if sell == False: 
            sell = True


#checking earnings of last 1 year
initialAmount = finalamount = 10000
lastBuyPrice = 0
numberoftrades = 0
tradeHistory = pd.DataFrame(columns=[["Buy Price", "Number of Stocks", 
                                      "Sell Price", "Earned", "Final Amount", 
                                      "Number of Days", "Percentage"]])
for n in range (len(trend)-252,len(trend)):
    if trend[n]==2:
        lastBuyPrice = X.iloc[n,1]
        #print ("last buy price =", lastBuyPrice)
        numberofstocks = finalamount/lastBuyPrice
        #print ("number of stocks = ", numberofstocks)
        tradeHistory.set_value(numberoftrades, "Buy Price", lastBuyPrice)
        tradeHistory.set_value(numberoftrades, "Number of Stocks", numberofstocks)
        buyDate = X.iloc[n].name
    if trend[n]==1: 
        #print ("sell price =", X.iloc[n,1])
        if tradeHistory.empty == True: continue
        finalamount =  X.iloc[n,1]*numberofstocks
        #print ("final amount =", finalamount)
        #print (n)
        tradeHistory.set_value(numberoftrades, "Sell Price", X.iloc[n,1])
        tradeHistory.set_value(numberoftrades, "Earned",  
                               (X.iloc[n,1]- lastBuyPrice)*numberofstocks)
        tradeHistory.set_value(numberoftrades, "Final Amount", finalamount)
        tradeHistory.set_value(numberoftrades, "Number of Days", 
                               pd.Timedelta(X.iloc[n].name - buyDate).days)
        tradeHistory.set_value(numberoftrades, "Percentage",  
                               (X.iloc[n,1]- lastBuyPrice)*100/lastBuyPrice )
        numberoftrades += 1
        
                          
 #toplot = pd.Series(data = "0", index=X[1300:].index)
"""
tobuy = pd.Series()
tosell= pd.Series()
for n in range(1300,len(X["Adj_Close"])):
    if trend[n]==2: 
        tobuy.set_value(X.iloc[n].name, X.iloc[n,1])
    if trend[n]==1: 
        tosell.set_value(X.iloc[n].name, X.iloc[n,1])
        #toplot[n-1300]=  X.iloc[n,1]
"""

#plt.plot(X.iloc[1400:,1].index.values, X.iloc[1400:,1]) 
#plt.scatter (X.iloc[1400:,1].index.values, [trend[n] for n in range(1300,len(X["Adj Close"]))])
#plt.show()


fig, ax1 = plt.subplots()
X.iloc[1300:,1].plot(ax=ax1)
ax1.plot(tobuy,'g^')
ax1.plot(tosell,'o')   # This is where I get held up.
plt.show()

inputX = X[["SMA", "RSI3", "MACD", "K_Stok", "D_Stok", "Will_R"]].values
print (len(inputX))
inputX = inputX[:-rollingdays]
print (len(inputX))
inputY = X.Adj_Close[rollingdays:].values

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(inputX, 
                                                    inputY, test_size = 0.25, 
                                                    random_state = 0)

# Fitting Kernel SVM to the Training set

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 350, random_state = 0)
regressor.fit(X_train, y_train)

# Predicting the Test set results
#y_pred = regressor.predict(X_test)

regressor = predict(inputX, inputY)
print ("Expected_Price", sum(regressor.predict(inputX[-4:-1]))/3)