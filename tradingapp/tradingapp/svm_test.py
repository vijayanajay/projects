import quandl
from bokeh.plotting import figure, show
from bokeh.layouts import column
import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import preprocessing, tree
from sklearn.tree.export import export_text
from sklearn.ensemble import RandomForestClassifier





percent_return_expected = 0.03
ewma_fast_days = 12
ewma_slow_days = 26
ewma_signal_days =9


def relative_strength_index(df, n):
    dUp = df > 0
    dDown = df < 0
    
    RollUp=pd.Series(dUp).rolling(window=n).mean() 
    RollDown=pd.Series(dDown).rolling(window=n).mean().abs()
    
    RS = RollUp / RollDown
    rsi= 100.0 - (100.0 / (1.0 + RS))
    return rsi

def test_svm_model(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20)
    
    min_max_scaler = preprocessing.MinMaxScaler()
    X_train_scaled = min_max_scaler.fit_transform(X_train)
    X_test_scaled = min_max_scaler.fit_transform(X_test)
    
    #model = SVC(kernel = 'rbf')
    model = SVC(kernel = 'rbf',
                C = 1e-04,
                random_state=0)
    model.fit(X_train_scaled, y_train)
    y_pred_acc = model.predict(X_test_scaled)
    
    #model.fit(X_train_scaled, y_train)
    #y_pred = model.predict(X_test_scaled)
    
    
    print("Confusion Matrix")
    print(confusion_matrix(y_test,y_pred_acc))
    print(pd.crosstab(y_test, y_pred_acc, rownames=['True'], 
                      colnames=['Predicted'], margins=True))        
    return True
    
def test_decision_trees(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                        test_size=0.2, 
                                                        random_state=0)
    min_max_scaler = preprocessing.MinMaxScaler()
    X_train_scaled = min_max_scaler.fit_transform(X_train)
    X_test_scaled = min_max_scaler.fit_transform(X_test)
    
    model = tree.DecisionTreeClassifier(random_state=0)
    decision_tree = model.fit(X_train_scaled,y_train)
    y_pred_acc = model.predict(X_test_scaled)
    
    print("Confusion Matrix")
    print(confusion_matrix(y_test,y_pred_acc))
    print(pd.crosstab(y_test, y_pred_acc, rownames=['True'], 
                      colnames=['Predicted'], margins=True))        
    
    print ()
    print ("Decision Tree")
    r = export_text(decision_tree, feature_names=X.columns.values.tolist())
    print (r)
    return True
    
def test_random_forest(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                        test_size=0.2, 
                                                        random_state=0)
    min_max_scaler = preprocessing.MinMaxScaler()
    X_train_scaled = min_max_scaler.fit_transform(X_train)
    X_test_scaled = min_max_scaler.fit_transform(X_test)
    
    model = RandomForestClassifier(n_estimators=1000, random_state=0)
    model.fit(X_train_scaled,y_train)
    y_pred = model.predict(X_test_scaled)
        
    print("Confusion Matrix")
    print(confusion_matrix(y_test,y_pred))
    print(pd.crosstab(y_test, y_pred, rownames=['True'], 
                      colnames=['Predicted'], margins=True))        
    
    print ()
    print(classification_report(y_test, y_pred))
    #print ("Decision Tree")
    #r = export_text(decision_tree, feature_names=X.columns.values.tolist())
    #print (r)
    return True
    
    
def test_best_svm_model(X,y):
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                                        test_size=0.2, 
                                                        random_state=0)
    
    min_max_scaler = preprocessing.MinMaxScaler()
    X_train_scaled = min_max_scaler.fit_transform(X_train)
    X_test_scaled = min_max_scaler.fit_transform(X_test)

    # Set the parameters by cross-validation
    tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4, 1e-5],
                         'C': [1e-6, 1e-5, 0.001,.009,0.01,.09, 1, 10, 100, 1000]},
                        {'kernel': ['linear'], 
                         'C': [1e-6, 1e-5, 0.001,.009,0.01,.09, 1, 10, 100, 1000]}]
    
    scores = ['precision', 'recall']
    
    for score in scores:
        print("# Tuning hyper-parameters for %s" % score)
        print()
    
        clf = GridSearchCV(
            SVC(), tuned_parameters, scoring='%s_macro' % score
        )
        clf.fit(X_train_scaled, y_train)
    
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
        y_true, y_pred = y_test, clf.predict(X_test_scaled)
        print(classification_report(y_true, y_pred))
        print()
    
    return True

def create_graphs(info):
    source = pd.DataFrame()
    source['Date'] = info.loc[:,'Date']
    source['Open'] = info.loc[:, 'Open']
    marker = pd.DataFrame()
    marker['X'] = info.loc[info.RSI3 >= 80, 'Date']
    marker['Y'] = info.loc[info.RSI3 >= 80, 'Open']
    
    
    s1 = figure(title='Open Price', 
               plot_width=1000, 
               plot_height=300,
               x_axis_label="datetime",
               x_axis_type="datetime",
               y_axis_label = 'Open Price')
    
    s1.line(source.Date,source.Open, line_width=2)
    s1.asterisk(marker.X, marker.Y, color = 'red', size=5)
    
    #To create the graph s2
    hist, edges = np.histogram(info.daily_returns, density=True, bins=30)
    source = pd.DataFrame()
    source ['hist']  = hist
    source ['left']  = edges[:-1]
    source ['right']  = edges[1:]
    #source['color'] = ['cyan' if x >= y else 'blue' for x in source.right]
    source.loc[source.index <= 0.05 * len(source), 'color'] = 'powderblue'
    source.loc[source.index > 0.05 * len(source), 'color'] = 'deepskyblue'
    source.loc[source.right >= 0, 'color'] = 'blue'
    source.loc[source.right >= percent_return_expected, 'color'] = 'red'
    source.loc[source.index > 0.95 * len(source), 'color'] = 'midnightblue'
    
    s2 = figure(plot_width=1000,
                plot_height=300,
                title = "Histogram of returns",
                y_axis_label = "Count")  
    
    s2.quad(bottom = 0, top = "hist" ,left = "left", 
        right = "right", source = source, color = "color")
        
    
    # To create the graph s3 and s4 and s5
    source = pd.DataFrame()
    source['SMA3'] = info.loc[:,'SMA3']
    source['daily_returns'] = info.loc[:,'daily_returns']
    source['RSI3'] = info.loc[:,'RSI3']
    source['MACD'] = info.loc[:,'MACD']
    source['color'] = 'deepskyblue'
    source.loc[info.daily_returns >= 0, 'color'] = 'blue'
    source.loc[info.daily_returns >= percent_return_expected, 'color'] = 'red'
    
    s3 = figure(plot_width=1000,
                plot_height=300,
                title = "SMA3 vs Daily Returns",
                x_axis_label = 'SMA3',
                y_axis_label = "daily_returns")  
    
    s3.scatter(source.SMA3, source.daily_returns)
    
    
    # To create the graph s4
    
    s4 = figure(plot_width=1000,
                plot_height=300,
                title = "RSI3 vs SMA3",
                x_axis_label = 'SMA3',
                y_axis_label = "RSI3")  
    
    s4.scatter(source.SMA3, source.RSI3, color=source.color)
    
    s5 = figure(plot_width=1000,
                plot_height=300,
                title = "MACD vs daily_returns",
                x_axis_label = 'MACD',
                y_axis_label = "daily_returns")  
    
    s5.scatter(source.MACD, source.daily_returns, color=source.color)
    
    s6 = figure(plot_width=1000,
                plot_height=300,
                title = "MACD vs RSI3",
                x_axis_label = 'MACD',
                y_axis_label = "RSI3")  
    
    s6.scatter(source.MACD, source.RSI3, color=source.color)
    
    p = column(s1, s2, s3, s4, s5, s6)
    return p    

   
    
    
quandl.ApiConfig.api_key = 'fRsTyQJZaBbXBcKsnahq'
stock_price = quandl.get('BSE/BOM500325', start_date='2017-01-01', 
                         end_date='2019-12-31')
info = stock_price[{'Open','WAP'}]
info.loc[:, 'Date'] = pd.to_datetime(info.index, format='%m/%d/%Y')
info.loc[:,"daily_returns"] = info.iloc[3:,1] / info.iloc[:-3, 1].values - 1
info.daily_returns = info.daily_returns.shift(periods=-3)


info.loc[:,'SMA3']= pd.Series(info.Open).rolling(window=3).mean()
info.loc[:,'SMA6']= pd.Series(info.Open).rolling(window=6).mean()
#info.loc[:,'SMA7']= pd.Series(info.Open).rolling(window=7).mean()
#info.loc[:,'SMA15']= pd.Series(info.Open).rolling(window=15).mean()
info.loc[:,'RSI3'] = relative_strength_index(info.daily_returns,3)
emaSlow =  pd.Series(info.loc[:,'Open']).ewm(adjust=True,ignore_na=False,
                    span=ewma_slow_days,min_periods=1).mean()
emaFast =  pd.Series(info.loc[:,'Open']).ewm(adjust=True,ignore_na=False,
                    span=ewma_fast_days,min_periods=1).mean()
emaSignal =  pd.Series(info.loc[:,'Open']).ewm(adjust=True,ignore_na=False,
                    span=ewma_signal_days,min_periods=1).mean()
low_min = pd.Series(info.loc[:, "Open"]).rolling(window=3).min()
high_max = pd.Series(info.loc[:, "Open"]).rolling(window=3).max()
info.loc[:,'WillR'] = 100 * (high_max - info['Open'])/(high_max - low_min)
info.loc[:,'MACD'] = emaFast - emaSlow
info = info.dropna()

info = info.drop(info[info.daily_returns >= 0.065].index)
info = info.drop(info[info.daily_returns <= -0.055].index)


#X = info[{'RSI3','MACD', 'WillR'}]
y = info['daily_returns'].apply(lambda x: 1 if x>=percent_return_expected else 0)

#svm_model_return = test_svm_model(X,y)
#test_best_svm_model (X,y)

#for decision trees only
X = info[{'RSI3','MACD', 'WillR'}]
#test_decision_trees(X,y)
test_random_forest(X,y)

#Create graphs
#p = create_graphs(info)
#show (p)



#To create the graph s1



