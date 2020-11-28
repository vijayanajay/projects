# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 19:17:28 2020

@author: vijay
"""

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


history_points = 60
period_of_returns = 15
small_period = int(.2 * period_of_returns)
large_period = int(.6 * period_of_returns)


data = pd.read_csv("test_data.csv", sep=',')
data.drop('Volume', axis=1, inplace=True)


info = data[{'Close'}]

info.loc[:,'exp_C'] = info.Close.shift(periods=-period_of_returns)
info.loc[:, 'SMA'] = talib.SMA(info.Close,small_period)

info = info.dropna()
#X_data_normalised = np.array(info.drop('exp_C', axis=1))
X_data_normalised = np.array(info)
X = np.array([X_data_normalised[i-history_points:i].copy() for i in range(history_points,len(info))])
y = info.exp_C[history_points:len(X_data_normalised)].values
real_C =info.Close[history_points:len(X_data_normalised)].values