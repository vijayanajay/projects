#from bokeh.plotting import figure, show
#from bokeh.layouts import column
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.metrics import *
from pycaret.classification import *
import talib
import matplotlib.pyplot as plt
import plotly
import plotly.offline as py
import plotly.io as pio
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import cufflinks as cf
import plotly.express as px
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

cf.go_offline()
pio.renderers.default = "browser"


sma_period = 20
period_of_returns = 60
rsi_period = 20


data = pd.read_csv("data.csv", sep=';')
data.drop('Volume', axis=1, inplace=True)
#data = data.loc[len(data)-5000:,]

info = data[{'Open', 'High', 'Low','Close'}]
#info.loc[:,"returns"] = info.iloc[period_of_returns:,0] / info.iloc[:-period_of_returns, 0].values - 1
#info.returns = info.returns.shift(periods=-period_of_returns)
info.loc[:,'exp_C'] = info.Close.shift(periods=-period_of_returns)

info.loc[:, 'SMA'] = talib.SMA(info.Close,sma_period)
info.loc[:, 'EMA'] = talib.EMA(info.Close,sma_period)
info.loc[:,'RSI'] = talib.RSI(info.Close,rsi_period)
info.loc[:,'APO'] = talib.APO(info.Close, fastperiod=10, slowperiod=40)
macd, macdsignal, macdhist = talib.MACD(info.Close, 12, 26,9)
info.loc[:,'MACD'] = macd
info.loc[:,'MACDSIGNAL'] = macdsignal
del [macd, macdsignal, macdhist]
upperband, middleband, lowerband = talib.BBANDS(info.Close, 
                                                timeperiod=sma_period, 
                                                nbdevup=2, nbdevdn=2, matype=0)
info.loc[:,'STDDEV'] = talib.STDDEV(info.Close, 
                                    timeperiod=sma_period, nbdev=1)
info.loc[:,'MOM'] = talib.MOM(info.Close, timeperiod=sma_period)

#additional
info.loc[:,'WillR'] = talib.WILLR(info.High, info.Low, info.Close, timeperiod=sma_period)
info.loc[:,'PLUS_DI'] = talib.PLUS_DI(info.High, info.Low, info.Close, sma_period)
info.loc[:,'PLUS_DM'] = talib.PLUS_DM(info.High, info.Low, sma_period)
info.loc[:,'ADX'] = talib.ADX(info.High, info.Low, info.Close, 15)
info.loc[:,'TRIX'] = talib.TRIX(info.Close, 15)


info = info.dropna()
info = info.loc[len(info)-5000:,:]

X = info.values
y = info.Close.shift(periods=-period_of_returns).values
scalerX = preprocessing.StandardScaler()
X_scaled = x = scalerX.fit_transform(X)

pca = PCA(n_components=18)
pca_components = pca.fit_transform(X_scaled)
print('Explained variation per principal component: {}'.format(pca.explained_variance_ratio_))



'''
fig = make_subplots(rows=10, cols=1, shared_xaxes=True, vertical_spacing=0.02,
                    subplot_titles=('Close Prices', 'SMA', 'EMA', 'RSI',
                                    'APO', 'MACD', 'Bollinger Bands', 
                                    'STD DEV', 'MOM'))
fig.add_trace(go.Scatter(x=info.index,y=info.Close, mode='lines', name='Close'),
              row=1,col=1)
fig.add_trace(go.Scatter(x=info.index,y=info.SMA, mode='lines'),row=2,col=1)
fig.add_trace(go.Scatter(x=info.index,y=info.EMA, mode='lines'),row=3,col=1)
fig.add_trace(go.Scatter(x=info.index,y=info.RSI,mode='lines'),row=4,col=1)
fig.add_trace(go.Scatter(x=info.index,y=np.full(len(info),30),mode='lines'),
              row=4,col=1)
fig.add_trace(go.Scatter(x=info.index,y=np.full(len(info),70),mode='lines'),
              row=4,col=1)
fig.add_trace(go.Scatter(x=info.index,y=info.APO,mode='lines'),row=5,col=1)
fig.add_trace(go.Scatter(x=info.index,y=info.MACD, mode='lines'),row=6,col=1)
fig.add_trace(go.Scatter(x=info.index,y=upperband, mode='lines',
                         line=dict(color='firebrick', width=2,
                              dash='dot')),row=7,col=1)
fig.add_trace(go.Scatter(x=info.index,y=middleband, mode='lines',
                         line=dict(color='royalblue', width=2,)),row=7,col=1)
fig.add_trace(go.Scatter(x=info.index,y=lowerband, mode='lines',
                         line=dict(color='firebrick', width=2,
                              dash='dot')),row=7,col=1)
fig.add_trace(go.Scatter(x=info.index,y=info.STDDEV,mode='lines'),row=8,col=1)
fig.add_trace(go.Scatter(x=info.index,y=info.MOM,mode='lines'),row=9,col=1)

        
fig.update_layout(height=3000, width=1000)
fig.show()
'''

### this is for scatter matrix to find the correlation
'''
fig2 = go.Figure(data = go.Splom(
        dimensions = [dict(label='SMA', 
                           values= info.SMA),
                    dict(label='EMA', 
                           values= info.EMA),
                    dict(label='RSI', 
                           values= info.RSI),
                    dict(label='APO', 
                           values= info.APO),
                    dict(label='MOM', 
                           values= info.MOM)]))
fig2.show()
'''

fig3=go.Figure(go.Scatter(y=np.cumsum(pca.explained_variance_ratio_), mode='lines'))
fig3.show()