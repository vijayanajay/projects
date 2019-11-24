import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, CDSView, BooleanFilter
import backtrader as bt
from datetime import datetime
import numpy as np

period_of_returns = 15
minimum_return = 0.01
sma_slow = 7
sma_fast = 15
min_number_of_positive_returns = 4


def datetime(x):
    return np.array(x, dtype=np.datetime64)
                    
def relative_strength_index(df, n):
    dUp = df > 0
    dDown = df < 0
    
    RollUp=pd.Series(dUp).rolling(window=n).mean() 
    RollDown=pd.Series(dDown).rolling(window=n).mean().abs()
    
    RS = RollUp / RollDown
    rsi= 100.0 - (100.0 / (1.0 + RS))
    return rsi


def calculate_return(df, period):
    returns = ((df.openBid - df.openAsk.shift(period))/df.openAsk.shift(period)) * 100
    return returns

def set_buysell_points(df, minimum_return):
    pass


def find_max_range(df):
    # find the maximum range for the dataframe to display on the graph
    max = df['sma_slow'].max()
    max *= 1.05 
    return max
    
def find_min_range(df):
    # find the minimum range for the dataframe to display on the graph
    min = df['sma_slow'].min()
    min *= 0.95 
    return min

def get_positive_returns_df(df):
    # create a df with indication 
    positive_returns_df = pd.Series([])
    num_of_postive_returns = 0
    sum_of_postive_returns = 0
    for n in range (0,len(df)):
        if df[n] > 0:
            sum_of_postive_returns += df[n]
            num_of_postive_returns += 1
            positive_returns_df[n] = sum_of_postive_returns
        if df[n] <= 0:
            if num_of_postive_returns >= min_number_of_positive_returns:
                positive_returns_df[n-1] = sum_of_postive_returns
            positive_returns_df[n] = 0
            num_of_postive_returns = 0
            sum_of_postive_returns = 0
    return positive_returns_df

oanda_data = pd.read_csv('EUR_USD.csv')
#oanda_data = pd.read_csv('EUR_USD.csv')

analysis_df = pd.DataFrame(datetime(oanda_data.time), columns=["time"])

analysis_df['returns'] = calculate_return(oanda_data,period_of_returns)
analysis_df = analysis_df.fillna(method='bfill')
analysis_df['sma_slow'] = oanda_data.openAsk.rolling(window=sma_slow).mean()
analysis_df['sma_fast'] = oanda_data.openAsk.rolling(window=sma_fast).mean()
analysis_df['RSI'] = relative_strength_index(analysis_df["returns"],period_of_returns)
#analysis_df['BuySellIndicator'] = set_buysell_points(analysis_df["returns"],period_of_returns)
analysis_df = analysis_df.fillna(method='bfill')

#find all positive returns for atleast n +ve periods
analysis_df['postive_returns'] = get_positive_returns_df(analysis_df["returns"])
analysis_df['openAsk'] = oanda_data['openAsk']


#print (analysis_df['returns'].between(left=minimum_return,right=2).sum())


output_file("color_scatter.html", title="color_scatter.py example", mode="cdn")

TOOLS = "crosshair,pan,wheel_zoom,box_zoom,reset,box_select,lasso_select"

sample = analysis_df[200:3500]
#sample.time = datetime(sample.time)
source = ColumnDataSource(sample)

p = figure(tools=TOOLS, x_axis_label = 'time', x_axis_type="datetime",
           plot_width=1100)
#p.circle(x='index', y='postive_returns', source = source, size = 10, color = 'green')
#p.circle(x='index', y='returns', source = source, size = 10, color = 'green', legend="returns over time")

#p.line('index','sma_slow', source=source, color = 'red', y_range_name = 'sma' )
p.line('time','sma_slow', source=source, color = 'blue', 
       legend = 'SMA Slow' )
p.line('time','sma_fast', source=source, color = 'green', 
       legend = 'SMA Fast' )
view = CDSView(source=source, filters=[BooleanFilter
                                       ([True if y > 0 else False for y in 
                                         sample['postive_returns']])])
   
p.line('time','openAsk', source=source, color = 'darkturquoise', line_width=6, 
       view=view, legend = 'Positive Returns')
p.line('time','openAsk', source=source, color = 'red', 
       line_width=1, legend = 'Open Ask')

show(p)


#with open('EUR_USD_analysis.csv', 'w', newline='') as csvfile:
#    analysis_df.to_csv(csvfile)