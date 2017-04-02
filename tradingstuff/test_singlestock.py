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

#data = DataReader('MANAPPURAM.NS',  'yahoo', datetime(2010, 1, 1), date.today())
data = wb.DataReader('MANAPPURAM.NS',  'yahoo', datetime(2010, 1, 1), date.today())


X = pd.DataFrame(data = data[["Volume", "Adj Close"]])
#filter all o volume days
X = X[X["Volume"]!=0]
X.insert(2, column="SMA3", value = pd.Series(X["Adj Close"]).rolling(window=3).mean())
X.insert(3, column="SMA6", value = pd.Series(X["Adj Close"]).rolling(window=6).mean())
X.insert(4, column="SMA9", value = pd.Series(X["Adj Close"]).rolling(window=9).mean())
X.insert(5, column="Daily Returns", value = X.iloc[1:,1] / X.iloc[:-1, 1].values - 1)
X.insert(6, column="RSI3", value = relative_strength_index(X["Daily Returns"],3))
X.insert(7, column="RSI6", value = relative_strength_index(X["Daily Returns"],6))
X.insert(8, column="RSI9", value = relative_strength_index(X["Daily Returns"],9))
X.insert(9, column="Y", value = X.iloc[1:,1] > X.iloc[:-1,1].values)
X.iloc[:,2:] = X.iloc[:,2:].fillna(method='bfill')

inputX = X[["Volume", "SMA3", "SMA6", "SMA9", "RSI3", "RSI6", "RSI9"]].values
inputY = X["Y"].values


# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(inputX, inputY, test_size = 0.25, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting Kernel SVM to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'rbf', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))


"""
inputX = X.iloc[:,[0,1,2,3,4,6,7,8]].values
inputY = X.iloc[:,1].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(inputX, inputY, test_size = 0.25, random_state = 0)

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 650, random_state = 0)
regressor.fit(X_train, y_train)

y_predict = regressor.predict(X_test)

y_accuracy = (y_predict/y_test - 1) *100

x_series = pd.Series(range(1, len(y_test)+1))

#plt.plot (x_series, y_test)
#plt.show()


import statsmodels.formula.api as sm
regressor_OLS = sm.OLS(endog = inputY, exog = inputX).fit()
regressor_OLS.summary()
"""
