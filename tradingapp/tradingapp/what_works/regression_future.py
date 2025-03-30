# This is basic regression model for future prediction. 
# loss: 2.7448e-05 - mean_squared_error: 2.7448e
# so-so accuracy

from sklearn import preprocessing
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, Input, Activation, concatenate
from keras.layers import BatchNormalization, MaxPooling1D
from keras import optimizers
from keras.utils import to_categorical
from bokeh.plotting import figure, show
from bokeh.layouts import column 
from keras.callbacks import TensorBoard
import talib
from matplotlib import pyplot
from sklearn.metrics import *
import quandl
import pickle


physical_devices = tf.config.list_physical_devices('GPU') 
tf.config.experimental.set_memory_growth(physical_devices[0], True)

history_points = 60
period_of_returns = 60
expected_returns = 0.001
small_period = 3
large_period = 10

def create_graphs(info):
    source = pd.DataFrame()
    source['Open'] = info.loc[:, 'Open']
    #marker = pd.DataFrame()
    #marker['X'] = info.loc[info.RSI3 >= 80, 'Date']
    #marker['Y'] = info.loc[info.RSI3 >= 80, 'Open']
    
    
    s1 = figure(title='Open Price', 
               plot_width=1000, 
               plot_height=300,
               x_axis_label="datetime",
               y_axis_label = 'Open Price')
    
    s1.line(source.index,source.Open, line_width=2)
    #s1.asterisk(marker.X, marker.Y, color = 'red', size=5)
    
    #To create the graph s2
    hist, edges = np.histogram(info.returns, density=True, bins=50)
    source = pd.DataFrame()
    source ['hist']  = hist
    source ['left']  = edges[:-1]
    source ['right']  = edges[1:]
    #source['color'] = ['cyan' if x >= y else 'blue' for x in source.right]
    source.loc[source.index <= 0.1 * len(source), 'color'] = 'powderblue'
    source.loc[source.index > 0.05 * len(source), 'color'] = 'deepskyblue'
    source.loc[source.right >= 0, 'color'] = 'blue'
    source.loc[source.right >= expected_returns, 'color'] = 'red'
    source.loc[source.index > 0.9 * len(source), 'color'] = 'midnightblue'
    
    s2 = figure(plot_width=1000,
                plot_height=300,
                title = "Histogram of returns",
                y_axis_label = "Count")  
    
    s2.quad(bottom = 0, top = "hist" ,left = "left", 
        right = "right", source = source, color = "color")
    
    
    source = pd.DataFrame()
    source['returns'] = info.loc[:len(info)/6, 'returns']
    
    source.loc[source.returns <=0, 'color'] = 'blue'
    source.loc[source.returns > 0, 'color'] = 'red'
    s3 = figure(title='Returns', 
               plot_width=1000, 
               plot_height=300,
               x_axis_label="datetime",
               y_axis_label = 'Returns')
    
    s3.scatter(source.index,source.returns, color=source.color)
    
    p = column(s1, s2, s3)
    return p   
        
    
#quandl.ApiConfig.api_key = 'fRsTyQJZaBbXBcKsnahq'
#data = quandl.get('BSE/BOM500325', start_date='2010-01-01', 
#                         end_date='2019-12-31')

#quandl.ApiConfig.api_key = 'fRsTyQJZaBbXBcKsnahq'
#data = quandl.get('BSE/BOM500325', start_date='2010-01-01', 
#                        end_date='2019-12-31')
    
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


info = info.dropna()
info = info.loc[:len(info)/2,:]

#p = create_graphs(info)
#show (p)


# using the last {history_points} open high low close volume data points, predict the next open value






scalerX = preprocessing.MinMaxScaler(feature_range=(0,1))
scalery = preprocessing.MinMaxScaler(feature_range=(0,1))
X_data_normalised = scalerX.fit_transform(info.drop('exp_C', axis=1))
X = np.array([X_data_normalised[i:i+history_points].copy() for i in range(len(X_data_normalised) - history_points)])

train_data = 0.8

y = info.exp_C[:len(X_data_normalised) - history_points].values
y_test = y[int(len(X)*train_data):]  
y = y.reshape(-1,1)
y = scalery.fit_transform(y)

with open('scalerX.pkl', 'wb') as f:
    pickle.dump(scalerX, f)
with open('scalery.pkl', 'wb') as f:
    pickle.dump(scalery, f)    


X = X.astype('float32')
y = y.astype('float32')

X_train = X[:int(len(X)*train_data)]
y_train = y[:int(len(X)*train_data)]
X_test = X[int(len(X)*train_data):]  



# for indian stock data
'''
model = Sequential()
model.add(LSTM(60, activation='relu', return_sequences=True, 
               input_shape = (history_points,14)))
model.add(LSTM(60, activation='relu', return_sequences=False))
model.add(Dropout(0.15))
model.add(Dense(30, activation='relu'))
model.add(Dense(1))

model.compile(loss= 'mean_squared_error', optimizer='adam', 
              metrics=['mean_squared_error'])
#tensorboard = TensorBoard(log_dir="./logs")
epochs=14
'''

#for forex data
model = Sequential()
model.add(LSTM(60, activation='relu', return_sequences=True, 
               input_shape = (history_points,14)))
model.add(LSTM(60, activation='relu', return_sequences=False))
model.add(Dropout(0.25))
model.add(Dense(50, activation='relu'))
model.add(Dense(1))

model.compile(loss= 'mean_squared_error', optimizer='adam', 
              metrics=['mean_squared_error'])
epochs=20
history = model.fit(X_train,y_train,epochs=epochs, batch_size=512)

y_pred = model.predict(X_test)

y_pred_actuals = scalery.inverse_transform(y_pred)


print ("RMSE")
#print (np.sqrt(np.mean(((y_pred_actuals - y_test) ** 2))))


x_axis = list(range(1,len(y_test)+1))

s1 = figure(title='Open Price', 
           plot_width=1000, 
           plot_height=300,
           x_axis_label="datetime",
           y_axis_label = 'Open Price')

s1.line(x_axis,y_pred_actuals[:,0], line_width=2, color ='red')
s1.line(x_axis,y_test, line_width=2, color ='blue')

s2=figure(title='Loss/error', 
           plot_width=1000, 
           plot_height=300,
           x_axis_label="epoch",
           y_axis_label = 'loss/error')


s2.line(list(range(1,epochs+1)), history.history['loss'],color='red')
s2.line(list(range(1,epochs+1)), history.history['mean_squared_error'], color='blue')

show(column(s1, s2))

'''
model_json = model.to_json()
with open("regression_future_model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("regression_future_model.h5")
print("Saved model to disk")
'''
