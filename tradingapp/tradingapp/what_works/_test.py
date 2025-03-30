# This is basic regression model for future prediction. 
# loss: 2.7448e-05 - mean_squared_error: 2.7448e
# so-so accuracy

from sklearn import preprocessing
import numpy as np
import pandas as pd
#import tensorflow as tf
#from keras.models import Sequential
#from keras.layers import Dense, Dropout, LSTM, Input, Activation, concatenate
#from keras.layers import BatchNormalization, MaxPooling1D
#from keras import optimizers
#from keras.utils import to_categorical
#from bokeh.plotting import figure, show
#from bokeh.layouts import column 
#from keras.callbacks import TensorBoard
import talib
from matplotlib import pyplot
from sklearn.metrics import *
import plotly.offline as py
import plotly.io as pio
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import cufflinks as cf
import statsmodels.api as sm
import statsmodels.formula.api as smf
import seaborn as sns

cf.go_offline()
pio.renderers.default = "browser"



history_points = 60
period_of_returns = 3
small_period = int(.3 * history_points)
large_period = int(.9 * history_points)

    
data = pd.read_csv("infosys_data.csv")
data.drop({'Volume', 'Close'}, axis=1, inplace=True)
data.rename(columns={'Adj Close': 'Close'}, inplace=True)

info = data[{'Open','High','Low', 'Close'}]
#info.loc[:,"returns"] = info.iloc[period_of_returns:,0] / info.iloc[:-period_of_returns, 0].values - 1
#info.returns = info.returns.shift(periods=-period_of_returns)
info.loc[:,'exp_C'] = info.Close.shift(periods=-period_of_returns)
info.loc[:, 'SMA'] = talib.SMA(info.Close,small_period)
#info.loc[:, 'EMA'] = talib.EMA(info.Close,small_period)
info.loc[:,'APO'] = talib.APO(info.Close, fastperiod=small_period, slowperiod=large_period)
#info.loc[:,'RSI'] = talib.RSI(info.Close,small_period)
#nfo.loc[:,'WillR'] = talib.WILLR(info.High, info.Low, info.Close, timeperiod=large_period)
info.loc[:,'STDDEV'] = talib.STDDEV(info.Close, 
                                    timeperiod=small_period, nbdev=1)
info.loc[:,'MOM'] = talib.MOM(info.Close, timeperiod=large_period)
macd, macdsignal, macdhist = talib.MACD(info.Close, 12, 26,9)
info.loc[:,'MACD'] = macd
#info.loc[:,'MACDSIGNAL'] = macdsignal
del [macd, macdsignal, macdhist]





info = info.dropna()
#info = info.loc[:len(info)/2,:]

pd.DataFrame.to_csv(info[-5500:],"info_beforenp.csv")

X = np.array(info.drop({'exp_C', 'Open','High', 'Low'}, axis=1))
train_data = 0.8
y = info.exp_C.values
y_test = y[-5500:]  

X_train = X[:int(len(X)*train_data)]
y_train = y[:int(len(X)*train_data)]
X_test = X[-5500:]  

X_test = sm.add_constant(X_test)
linear_regression = sm.OLS(y_test,X_test)
fitted_model = linear_regression.fit()
print (fitted_model.summary())



#lr_schedule = tf.keras.callbacks.LearningRateScheduler(
#        lambda epoch: 1e-3 * 10**(epoch / 6))
'''
optimizer = optimizers.Adam()
#for forex data using LTSM
model = Sequential()

model.add(LSTM(history_points, activation='relu', return_sequences=True, 
               input_shape = (history_points,X.shape[2])))
model.add(LSTM(history_points, activation='relu', return_sequences=False))
model.add(Dropout(0.2))
model.add(Dense(100, activation='relu'))
model.add(Dense(1))

model.compile(loss= 'mean_squared_error', optimizer=optimizer, 
              metrics=['mean_squared_error'])
epochs=7
history = model.fit(X_train,y_train,epochs=epochs, batch_size=256)

y_pred = model.predict(X_test)

y_pred_actuals = y_pred

'''

#x_axis = list(range(1,len(y_test)+1))



fig = make_subplots(rows=4, cols=1, vertical_spacing=0.02,
                    subplot_titles=('Actuals', 'Loss', 'MSE'))


fig.add_trace(go.Scatter(y=fitted_model.fittedvalues[-200:], mode='lines', 
                         name='Y_pred'), row=1,col=1)
fig.add_trace(go.Scatter(y=y_test[-200:], mode='lines', 
                         name='Y_real'), row=1,col=1)


fig.add_trace(go.Scatter(y=fitted_model.fittedvalues[-200:], mode='lines', 
                         name='Y_pred'), row=2,col=1)
fig.add_trace(go.Scatter(y=info.Close[-200:], mode='lines', 
                         name='Y_real'), row=2,col=1)

fig.update_layout(height=2000, width=1000)
fig.show()

