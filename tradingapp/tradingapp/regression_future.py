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
#from keras.utils import to_categorical
#from bokeh.plotting import figure, show
#from bokeh.layouts import column 
#from keras.callbacks import TensorBoard
import talib
from matplotlib import pyplot
from sklearn.metrics import *
import pickle
import plotly.offline as py
import plotly.io as pio
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import cufflinks as cf

cf.go_offline()
pio.renderers.default = "browser"

physical_devices = tf.config.list_physical_devices('GPU') 
tf.config.experimental.set_memory_growth(physical_devices[0], True)

history_points = 90
period_of_returns = 5
small_period = int(.3 * history_points)
large_period = int(.9 * history_points)

    
data = pd.read_csv("data.csv", sep=';')
data.drop('Volume', axis=1, inplace=True)

info = data[{'Open', 'High', 'Low','Close'}]
#info.loc[:,"returns"] = info.iloc[period_of_returns:,0] / info.iloc[:-period_of_returns, 0].values - 1
#info.returns = info.returns.shift(periods=-period_of_returns)
info.loc[:,'exp_C'] = info.Close.shift(periods=-period_of_returns)
info.loc[:, 'SMA'] = talib.SMA(info.Close,small_period)
info.loc[:, 'EMA'] = talib.EMA(info.Close,small_period)
#info.loc[:,'APO'] = talib.APO(info.Close, fastperiod=small_period, slowperiod=large_period)
info.loc[:,'RSI'] = talib.RSI(info.Close,small_period)
#info.loc[:,'WillR'] = talib.WILLR(info.High, info.Low, info.Close, timeperiod=large_period)
info.loc[:,'STDDEV'] = talib.STDDEV(info.Close, 
                                    timeperiod=small_period, nbdev=1)
info.loc[:,'MOM'] = talib.MOM(info.Close, timeperiod=small_period)
#macd, macdsignal, macdhist = talib.MACD(info.Close, 12, 26,9)
#info.loc[:,'MACD'] = macd
#info.loc[:,'MACDSIGNAL'] = macdsignal
#del [macd, macdsignal, macdhist]

#info.loc[:,'PLUS_DI'] = talib.PLUS_DI(info.High, info.Low, info.Close, large_period)
#info.loc[:,'PLUS_DM'] = talib.PLUS_DM(info.High, info.Low, large_period)

del data

info = info.dropna()
info = info.loc[:len(info)/2,:]


scalerX = preprocessing.StandardScaler()
scalery = preprocessing.StandardScaler()
X_data_normalised = scalerX.fit_transform(info.drop({'exp_C', 'Low', 'High'}, axis=1))
X = np.array([X_data_normalised[i-history_points:i].copy() for i in range(history_points,len(X_data_normalised))])

train_data = 0.8


y = info.exp_C[history_points:len(X_data_normalised)].values
real_C =info.Close[history_points:len(X_data_normalised)].values
y_test = y[int(len(X)-2000):]  
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
X_test = X[int(len(X)-2000):]  



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

#for forex data using LTSM
model = Sequential()
model.add(LSTM(history_points, activation='relu', return_sequences=True, 
               input_shape = (history_points,X.shape[2])))
model.add(LSTM(history_points, activation='relu', return_sequences=False))
model.add(Dropout(0.3))
model.add(Dense(100, activation='relu'))
model.add(Dense(1))
opt = optimizers.Adam(learning_rate=6e-5)

model.compile(loss= 'mae', optimizer=opt, 
              metrics=['mae'])
epochs=50
history = model.fit(X_train,y_train,epochs=epochs, batch_size=512)

y_pred = model.predict(X_test)

y_pred_actuals = scalery.inverse_transform(y_pred)


print ("RMSE")
#print (np.sqrt(np.mean(((y_pred_actuals - y_test) ** 2))))


x_axis = list(range(1,len(y_test)+1))



fig = make_subplots(rows=4, cols=1, vertical_spacing=0.02,
                    subplot_titles=('Actuals', 'Loss', 'MSE'))


fig.add_trace(go.Scatter(x=x_axis, y=y_pred_actuals[:,0], mode='lines', 
                         name='Y_pred'), row=1,col=1)
fig.add_trace(go.Scatter(x=x_axis, y=y_test, mode='lines', 
                         name='Y_real'), row=1,col=1)



fig.add_trace(go.Scatter(x=x_axis, y=history.history['loss'][18:], mode='lines', 
                         name='Y_real'), row=2,col=1)

fig.add_trace(go.Scatter(x=x_axis, y=history.history['mae'][18:], 
                         mode='lines', name='Y_real'), row=3,col=1)

fig.add_trace(go.Scatter(y=real_C[-500:], 
                         mode='lines', name='infoClose'), row=4,col=1)
fig.add_trace(go.Scatter(y=y_pred_actuals[:,0][-500:], 
                         mode='lines', name='Ypred'), row=4,col=1)
fig.add_trace(go.Scatter(y=y_test[-500:], 
                          mode='lines', name='Y_real'), row=4,col=1)

fig.update_layout(height=2000, width=2000)
fig.show()

'''
with open('models_mse_values.txt', 'a') as f:
    np.savetxt(fname=f,X=history.history['mean_squared_error'], 
               comments='LTSM60-LTSM60-DO0.25-DE-50, adam')
f.close()
'''

'''
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


#to save the mode in a json file
'''
model_json = model.to_json()
with open("regression_future_model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("regression_future_model.h5")
print("Saved model to disk")
'''
