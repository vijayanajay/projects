from sklearn import preprocessing
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, Input, Activation, concatenate
from keras import optimizers
from keras.utils import to_categorical
from bokeh.plotting import figure, show
from bokeh.layouts import column 



history_points = 60
period_of_returns = 60
expected_returns = 0.001

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

data = pd.read_csv("data.csv", sep=';')
data.drop('Volume', axis=1, inplace=True)

info = data[{'Open', 'Close'}]
info.loc[:,"returns"] = info.iloc[period_of_returns:,0] / info.iloc[:-period_of_returns, 0].values - 1
info.returns = info.returns.shift(periods=-period_of_returns)

info = info.dropna()

#p = create_graphs(info)
#show (p)


# using the last {history_points} open high low close volume data points, predict the next open value

x_info = info.iloc[:,0:2].values

data_normaliser = preprocessing.MinMaxScaler()
data_normalised = data_normaliser.fit_transform(x_info)

X = data_normalised
X = np.array([data_normalised[i:i+history_points].copy() for i in range(len(data_normalised) - history_points)])


y = info.iloc[period_of_returns:,2].apply(lambda x: 1 if x>=expected_returns else 0)
y =  np.asarray(y)



X = X.astype('float32')
y = y.astype('float32')

test_data = 0.2 
X_train = X[:int(len(X)*test_data)]
y_train = y[:int(len(X)*test_data)]
X_test = X[int(len(X)*test_data):]  
y_test = y[int(len(X)*test_data):]  



model = Sequential()
model.add(LSTM(60, activation='relu', input_shape = (60,2)))
model.add(Dropout(0.2))
model.add(Dense(100, activation='relu'))
model.add(Dense(50, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss= 'binary_crossentropy', optimizer='sgd', metrics=['accuracy'])
tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir="./logs")
model.fit(X_test,y_test,epochs=1, 
          batch_size=128,
          validation_split = 0.2,
          callbacks=[tensorboard_callback])


