# -*- coding: utf-8 -*-
"""
Created on Wed May 27 00:56:48 2020

@author: vijay
"""

import numpy as np
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.layouts import column 
from keras.models import model_from_json
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, Input, Activation, concatenate
from keras import optimizers
from sklearn import preprocessing
import pickle


history_points = 60
period_of_returns = 60

data = pd.read_csv("data.csv", sep=';')
data.drop('Volume', axis=1, inplace=True)

info = data[{'Open', 'High', 'Low','Close'}]
info.loc[:,"returns"] = info.iloc[period_of_returns:,0] / info.iloc[:-period_of_returns, 0].values - 1
info.returns = info.returns.shift(periods=-period_of_returns)
info.loc[:,'exp_C'] = info.Close.shift(periods=-period_of_returns)
info.loc[:,'RSI3'] = talib.RSI(info.returns,small_period)
info.loc[:,'RSI10'] = talib.RSI(info.returns,large_period)
info.loc[:,'WillR'] = talib.WILLR(info.High, info.Low, info.Close, timeperiod=large_period)
macd, macdsignal, macdhist = talib.MACD(info.Close, 12, 26,9)
info.loc[:,'MACD'] = macd
info.loc[:,'MACDSIGNAL'] = macdsignal
del [macd, macdsignal, macdhist]
info.loc[:,'PLUS_DI'] = talib.PLUS_DI(info.High, info.Low, info.Close, large_period)
info.loc[:,'PLUS_DM'] = talib.PLUS_DM(info.High, info.Low, large_period)
info.loc[:,'ADX'] = talib.ADX(info.High, info.Low, info.Close, 15)
info.loc[:,'TRIX'] = talib.TRIX(info.Close, 15)


with open('scalerX.pkl', 'rb') as fid:
    scalerX = pickle.load(fid)

with open('scalery.pkl', 'rb') as fid:
    scalery = pickle.load(fid)    
    

info = info.loc[len(info)-2000:,:]

X_data_normalised = scalerX.fit_transform(info.drop('exp_C', axis=1))
X = np.array([X_data_normalised[i:i+history_points].copy() for i in range(len(X_data_normalised) - history_points)])


y = info.exp_C[:len(X_data_normalised) - history_points].values
y_test = y
y = y.reshape(-1,1)


X = X.astype('float32')
y = y.astype('float32')


# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")


loaded_model.compile(loss= 'mean_squared_error', optimizer='adam', 
              metrics=['mean_squared_error'])


y_pred = model.predict(X)

y_pred_actuals = scalery.inverse_transform(y_pred)


x_axis = list(range(history_points,len(y_pred)+1))
s1 = figure(title='Open Price', 
           plot_width=1000, 
           plot_height=300,
           x_axis_label="datetime",
           y_axis_label = 'Open Price')

s1.line(x_axis,y_pred_actuals[:,0], line_width=2, color ='red')
s1.line(range(1,len(info.exp_C)+1),info.exp_C, line_width=2, color ='blue')


show(s1)