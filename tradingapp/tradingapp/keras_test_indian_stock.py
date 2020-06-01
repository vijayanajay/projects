from sklearn import preprocessing
import numpy as np
import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM, Input, Activation, concatenate
from keras.layers import BatchNormalization
from keras import optimizers
from keras.utils import to_categorical
from bokeh.plotting import figure, show
from bokeh.layouts import column 
from keras.callbacks import TensorBoard
import talib
from matplotlib import pyplot
from sklearn.metrics import *
import quandl
from keras import regularizers


history_points = 60
period_of_returns = 5
expected_returns = 0.03
small_period = 3
large_period = 10

      
    
#quandl.ApiConfig.api_key = 'fRsTyQJZaBbXBcKsnahq'
#data = quandl.get('BSE/BOM500325', start_date='2010-01-01', 
#                         end_date='2019-12-31')

quandl.ApiConfig.api_key = 'fRsTyQJZaBbXBcKsnahq'
data = quandl.get('BSE/BOM500325', start_date='2009-01-01', 
                         end_date='2019-12-31')
#data += quandl.get('BSE/BOM500209', start_date='2010-01-01', 
#                         end_date='2019-12-31')

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
#info = info.iloc[:128000,]

#p = create_graphs(info)
#show (p)


# using the last {history_points} open high low close volume data points, predict the next open value

X = info.drop('returns', axis=1).values
X = np.array([X[i:i+history_points].copy() for i in range(len(X) - history_points)])

y = info.loc[:,'returns'].apply(lambda x: 1 if x>=expected_returns else 0)
y = y.iloc[:len(info)-history_points,]
y =  np.asarray(y)

X = X.astype('float32')
y = y.astype('float32')

train_data = 0.8
X_train = X[:int(len(X)*train_data)]
y_train = y[:int(len(X)*train_data)]
X_test = X[int(len(X)*train_data):]  
y_test = y[int(len(X)*train_data):]  


scalers_train = {}
scalers_test = {}
for i in range(X_train.shape[1]):
    scalers_train[i] = preprocessing.StandardScaler()
    X_train[:, i, :] = scalers_train[i].fit_transform(X_train[:, i, :]) 

for i in range(X_test.shape[1]):
    scalers_test[i] = preprocessing.StandardScaler()
    X_test[:, i, :] = scalers_test[i].fit_transform(X_test[:, i, :]) 
    


print ("Percentage of y=1 in train data")
print (len(X_train[y_train==1])/len(X_train) * 100)
print ("Percentage of y=1 in test data")
print (len(X_test[y_test==1])/len(X_test) * 100)

'''
model = Sequential()
model.add(LSTM(60, activation='relu', return_sequences=True, input_shape = (60,13)))
model.add(LSTM(50, return_sequences= False))
model.add(Dense(50, activation='relu',kernel_regularizer=regularizers.l2(0.009)))
model.add(Dense(1, activation='sigmoid'))


#adamOpti = optimizers.Adam(lr = 0.0005)

model.compile(loss= 'binary_crossentropy', optimizer='adam', 
              metrics=['accuracy'])

tensorboard = TensorBoard(log_dir="./logs")

history = model.fit(X_train,y_train,epochs=20, 
                    validation_split = 0.2)
                    
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

print('Train: %.3f, Test: %.3f' % (train_acc, test_acc))

# plot loss during training
pyplot.subplot(211)
pyplot.title('Loss')
pyplot.plot(history.history['loss'], label='train')
pyplot.plot(history.history['val_loss'], label='val')
pyplot.legend()
# plot accuracy during training
pyplot.subplot(212)
pyplot.title('Accuracy')
pyplot.plot(history.history['accuracy'], label='train')
pyplot.plot(history.history['val_accuracy'], label='val')
pyplot.legend()
pyplot.show()

'''
