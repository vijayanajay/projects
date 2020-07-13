# -*- coding: utf-8 -*-
"""
Created on Wed May 27 00:56:48 2020

@author: vijay
"""

import numpy as np
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.layouts import column 
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import preprocessing
from sklearn.ensemble import BaggingClassifier, VotingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
import talib
import plotly.offline as py
import plotly.io as pio
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import cufflinks as cf


cf.go_offline()
pio.renderers.default = "browser"


#percent_return_expected = 0.025
percent_return_expected = 0.03
history_points = 20
period_of_returns = 3
small_period = int(.3 * history_points)
large_period = int(.9 * history_points)


stock_price = pd.read_csv("infosys_data.csv")
#stock_price = pd.read_csv("data.csv", sep=';')


info = stock_price[{'Open', 'High', 'Low','Adj Close'}]
#info = stock_price[{'Open', 'High', 'Low','Close'}]
info.rename(columns={'Adj Close': 'Close'}, inplace=True)

info.loc[:,"returns"] = info.iloc[period_of_returns:,0] / info.iloc[:-period_of_returns, 0].values - 1
info.returns = info.returns.shift(periods=-period_of_returns)
#info.loc[:,'exp_C'] = info.Close.shift(periods=-period_of_returns)
info.loc[:, 'SMA'] = talib.SMA(info.Close,small_period)
info.loc[:, 'EMA'] = talib.EMA(info.Close,small_period)
info.loc[:,'APO'] = talib.APO(info.Close, fastperiod=small_period, slowperiod=large_period)
info.loc[:,'RSI'] = talib.RSI(info.Close,small_period)
#info.loc[:,'WillR'] = talib.WILLR(info.High, info.Low, info.Close, timeperiod=large_period)
info.loc[:,'STDDEV'] = talib.STDDEV(info.Close, 
                                    timeperiod=small_period, nbdev=1)
#info.loc[:,'MOM'] = talib.MOM(info.Close, timeperiod=small_period)
#macd, macdsignal, macdhist = talib.MACD(info.Close, 12, 26,9)
#info.loc[:,'MACD'] = macd
#info.loc[:,'MACDSIGNAL'] = macdsignal
#del [macd, macdsignal, macdhist]

#info.loc[:,'PLUS_DI'] = talib.PLUS_DI(info.High, info.Low, info.Close, large_period)
#info.loc[:,'PLUS_DM'] = talib.PLUS_DM(info.High, info.Low, large_period)



info = info.dropna()
#info = info.loc[:len(info)/2,:]
#info = info.loc[:100000,:]



scalerX = preprocessing.StandardScaler()
#scalery = preprocessing.StandardScaler()
#X = scalerX.fit_transform(info.drop({'exp_C'}, axis=1))
X = scalerX.fit_transform(info.drop({'returns'}, axis=1))

    
train_data = 0.8

#y = info.exp_C.values
y = info['returns'].apply(lambda x: 1 if x>=percent_return_expected else 0)
y_test = y[int(len(X)-120):]  
#y = y.reshape(-1,1)
#y = scalery.fit_transform(y)

X_train = X[:int(len(X)*train_data)]
y_train = y[:int(len(X)*train_data)]
X_test = X[int(len(X)-120):]  

print ("Percentage of y=1 in train data")
print (len(X_train[y_train==1])/len(X_train) * 100)
print ("Percentage of y=1 in test data")
print (len(X_test[y_test==1])/len(X_test) * 100)

#svm = SVC(kernel = 'rbf',C=500,
#            gamma=2.27e-2,
#            random_state=2,
#           verbose=3)

svm = SVC(kernel = 'rbf',C=500,
            gamma=2.15e-2,
            probability=True,
            random_state=2,
            verbose=3)
dtr =  DecisionTreeClassifier(max_depth=6, max_features=4, 
                              criterion='entropy', random_state=2)
knn =  KNeighborsClassifier(n_neighbors=7)
#model = BaggingClassifier(base_estimator=svm, n_estimators=5, 
#                          random_state=314, verbose=3, n_jobs=2)


#vcl = VotingClassifier(estimators=[('dt', dtr), ('knn', knn), ('svc', svm)],
#                                    voting='soft', weights=[1, 1.5, 2])


#model.fit(X_train,y_train)
#y_pred = model.predict(X_test)

'''
svm.fit(X_train,y_train)
y_pred = svm.predict(X_test)
print("Confusion Matrix - SVM")
print(confusion_matrix(y_test,y_pred))
print(pd.crosstab(y_test, y_pred, rownames=['True'], 
              colnames=['Predicted'], margins=True))        

print ()
print(classification_report(y_test, y_pred))
'''

dtr.fit(X_train,y_train)
y_pred = dtr.predict(X_test)
print("Confusion Matrix - Decision Tree")
print(confusion_matrix(y_test,y_pred))
print(pd.crosstab(y_test, y_pred, rownames=['True'], 
              colnames=['Predicted'], margins=True))        

print ()
print(classification_report(y_test, y_pred))

'''
knn.fit(X_train,y_train)
y_pred = knn.predict(X_test)
print("Confusion Matrix - Knn")
print(confusion_matrix(y_test,y_pred))
print(pd.crosstab(y_test, y_pred, rownames=['True'], 
              colnames=['Predicted'], margins=True))        

print ()
print(classification_report(y_test, y_pred))


vcl.fit(X_train,y_train)
y_pred = vcl.predict(X_test)
print("Confusion Matrix - Voting Cl")
print(confusion_matrix(y_test,y_pred))
print(pd.crosstab(y_test, y_pred, rownames=['True'], 
              colnames=['Predicted'], margins=True))        

print ()
print(classification_report(y_test, y_pred))
'''

'''
tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4, 1e-5],
                     'C': [1e-6, 1e-5, 0.001,.009,0.01,.09, 1, 10, 100, 1000]},
                    {'kernel': ['linear'], 
                     'C': [1e-6, 1e-5, 0.001,.009,0.01,.09, 1, 10, 100, 1000]}]

scores = ['precision', 'recall']

n=0
    
for score in scores:
    n += 1
    print ()
    print ("n = %s" % n)
    print()
    print("# Tuning hyper-parameters for %s" % score)
    print()

    clf = GridSearchCV(
        SVC(), tuned_parameters, scoring='%s_macro' % score
    )
    clf.fit(X_train, y_train)

    print("Best parameters set found on development set:")
    print()
    print(clf.best_params_)
    print()
    print("Grid scores on development set:")
    print()
    means = clf.cv_results_['mean_test_score']
    stds = clf.cv_results_['std_test_score']
    for mean, std, params in zip(means, stds, clf.cv_results_['params']):
        print("%0.3f (+/-%0.03f) for %r"
              % (mean, std * 2, params))
    print()

    print("Detailed classification report:")
    print()
    print("The model is trained on the full development set.")
    print("The scores are computed on the full evaluation set.")
    print()
    y_true, y_pred = y_test, clf.predict(X_test)
    print(classification_report(y_true, y_pred))
    print()
'''

'''
x_axis = list(range(1,len(y_test)+1))
fig = make_subplots(rows=10, cols=1, vertical_spacing=0.02,
                    subplot_titles=('Actuals', 'Loss', 'MSE'))


fig.add_trace(go.Scatter(x=x_axis, y=y_pred, mode='lines', 
                         name='Y_pred'), row=1,col=1)
fig.add_trace(go.Scatter(x=x_axis, y=y_test, mode='lines', 
                         name='Y_real'), row=1,col=1)


fig.update_layout(height=2000, width=1000)
fig.show()

'''