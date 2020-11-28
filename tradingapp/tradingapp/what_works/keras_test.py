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


history_points = 60
period_of_returns = 60
expected_returns = 0.001
percent_return_expected = 0.001
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

data = pd.read_csv("data.csv", sep=';')
data.drop('Volume', axis=1, inplace=True)

info = data[{'Open', 'High', 'Low','Close'}]
info.loc[:,"returns"] = info.iloc[period_of_returns:,0] / info.iloc[:-period_of_returns, 0].values - 1
info.returns = info.returns.shift(periods=-period_of_returns)
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
info = info.iloc[:128000,]

#p = create_graphs(info)
#show (p)


# using the last {history_points} open high low close volume data points, predict the next open value

x_info = info.drop('returns', axis=1).values


data_normaliser = preprocessing.MinMaxScaler()
data_normalised = data_normaliser.fit_transform(x_info)

X = data_normalised
X = np.array([data_normalised[i:i+history_points].copy() for i in range(len(data_normalised) - history_points)])


y = info.loc[:,'returns'].apply(lambda x: 1 if x>=expected_returns else 0)
y = y.iloc[:len(info)-history_points,]
y =  np.asarray(y)



X = X.astype('float32')
y = y.astype('float32')

test_data = 0.2
X_train = X[:int(len(X)*test_data)]
y_train = y[:int(len(X)*test_data)]
X_test = X[int(len(X)*test_data):]  
y_test = y[int(len(X)*test_data):]  

print ("Percentage of y=1 in train data")
print (len(X_train[y_train==1])/len(X_train) * 100)
print ("Percentage of y=1 in test data")
print (len(X_test[y_test==1])/len(X_test) * 100)


model = Sequential()
model.add(LSTM(60, activation='relu', input_shape = (60,13)))
model.add(Dense(200, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(200, activation='relu'))
model.add(BatchNormalization())
model.add(Dense(200, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss= 'binary_crossentropy', optimizer='sgd', metrics=['accuracy'])
tensorboard = TensorBoard(log_dir="./logs")
history = model.fit(X_train,y_train,epochs=10, 
                    validation_split = 0.2,
                    callbacks=[tensorboard])

yhat_probs = model.predict(X_test, verbose=0)
yhat_classes = model.predict_classes(X_test, verbose=0)
yhat_probs = yhat_probs[:, 0]
yhat_classes = yhat_classes[:, 0]


# accuracy: (tp + tn) / (p + n)
accuracy = accuracy_score(y_test, yhat_classes)
print('Accuracy: %f' % accuracy)
# precision tp / (tp + fp)
precision = precision_score(y_test, yhat_classes)
print('Precision: %f' % precision)
# recall: tp / (tp + fn)
recall = recall_score(y_test, yhat_classes)
print('Recall: %f' % recall)
# f1: 2 tp / (2 tp + fp + fn)
f1 = f1_score(y_test, yhat_classes)
print('F1 score: %f' % f1)


# kappa
kappa = cohen_kappa_score(y_test, yhat_classes)
print('Cohens kappa: %f' % kappa)
# ROC AUC
auc = roc_auc_score(y_test, yhat_probs)
print('ROC AUC: %f' % auc)
# confusion matrix
matrix = confusion_matrix(y_test, yhat_classes)
print(matrix)

_, train_acc = model.evaluate(X_train, y_train, verbose=0)
_, test_acc = model.evaluate(X_test, y_test, verbose=0)

# plot loss during training
pyplot.subplot(211)
pyplot.title('Loss')
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='test')
pyplot.legend()
# plot accuracy during training
pyplot.subplot(212)
pyplot.title('Accuracy')
pyplot.plot(history.history['accuracy'], label='train')
pyplot.plot(history.history['val_accuracy'], label='test')
pyplot.legend()
pyplot.show()


