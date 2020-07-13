# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 20:16:56 2020

@author: vijay
"""

import backtrader as bt
import pandas as pd
import backtrader.analyzers as btanalyzers
import backtrader.strategies as btstrats
import datetime as dt

# import btoandav20
# class SmaSignal(bt.Signal):
#     params = (('period',10),)
#
#     def __init__(self):
#         self.lines.signal = self.data - bt.ind.SMA(period=self.p.period)
def pretty_print(dict):
    for key, value in dict.items():
        print(key, ' : ', value)

class TestStrategy(bt.Strategy):
    params = (
        ('maperiod', 19),
        ('printlog', False),
    )

    def log(self, txt, dt=None, doprint=False):
        if self.params.printlog or doprint:
            dt = dt or self.datas[0].datetime.date(0)
            print('%s, %s' % (dt.isoformat(), txt))

    def __init__(self):
        # Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close
        self.sma = bt.indicators.MovingAverageSimple(self.datas[0], period=self.params.maperiod)
        # bt.indicators.ExponentialMovingAverage(self.datas[0], period=25)
        # bt.indicators.WeightedMovingAverage(self.datas[0], period=25).subplot = True
        # bt.indicators.StochasticSlow(self.datas[0])
        # bt.indicators.MACDHisto(self.datas[0])
        # rsi = bt.indicators.RSI(self.datas[0])
        # bt.indicators.SmoothedMovingAverage(rsi, period=10)
        # bt.indicators.ATR(self.datas[0]).plot = False
        self.order = None
        self.buyprice = None
        self.buycomm = None

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    'BUY EXECUTED, Price: %.5f, Cost: %.5f, Comm %.5f' %
                    (order.executed.price,
                     order.executed.value,
                     order.executed.comm))
                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            elif order.issell():
                self.log('SELL EXECUTED, Price: %.5f, Cost: %.5f, Comm %.5f' %
                         (order.executed.price,
                          order.executed.value,
                          order.executed.comm))

            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')

        # Write down: no pending order
        self.order = None

    def notify_trade(self, trade):
        if not trade.isclosed:
            return

        self.log('OPERATION PROFIT, GROSS %.5f, NET %.5f' %
                 (trade.pnl, trade.pnlcomm))

    def next(self):
        # Simply log the closing price of the series from the reference
        #self.log('Close, %.5f' % self.dataclose[0])

        # Check if an order is pending ... if yes, we cannot send a 2nd one
        if self.order:
            return

        # Check if we are in the market
        if not self.position:

            # Not yet ... we MIGHT BUY if ...
            if self.dataclose[0] < self.dataclose[-1]:
                # current close less than previous close

                if self.dataclose[0] > self.sma[0]:
                    # BUY, BUY, BUY!!! (with all possible default parameters)
                    self.log('BUY CREATE, %.2f' % self.dataclose[0])

                    # Keep track of the created order to avoid a 2nd order
                    self.order = self.buy()

        else:

            # Already in the market ... we might sell
            if self.dataclose[0] < self.sma[0]:
                # SELL, SELL, SELL!!! (with all possible default parameters)
                self.log('SELL CREATE, %.2f' % self.dataclose[0])

                # Keep track of the created order to avoid a 2nd order
                self.order = self.sell()

    def stop(self):
        self.log('(MA Period %2d) Ending Value %.2f' %
                 (self.params.maperiod, self.broker.getvalue()), doprint=True)

cerebro = bt.Cerebro()
cerebro.addstrategy(TestStrategy)
# strats = cerebro.optstrategy(
#         TestStrategy,
#         maperiod=range(10, 31))

#cerebro.addstrategy(btstrats.SMA_CrossOver)
#cerebro.add_signal(bt.SIGNAL_LONG, SmaSignal)
cerebro.addobserver(bt.observers.BuySell)
cerebro.addobserver(bt.observers.Value)
#cerebro.addanalyzer(bt.analyzers.PyFolio, _name='pyfolio')

cerebro.broker.setcash(10000.0)
cerebro.broker.setcommission(commission=0.001)
cerebro.addsizer(bt.sizers.SizerFix, stake=10)
cerebro.addanalyzer(btanalyzers.SharpeRatio, _name='mysharpe')
cerebro.addanalyzer(btanalyzers.AnnualReturn, _name='annual_return')
cerebro.addanalyzer(btanalyzers.TradeAnalyzer, _name='trade_analyser')

# for infosys
info = pd.read_csv('infosys_data.csv', skiprows=1, index_col=0)
info.index = pd.to_datetime(info.index, format='%Y-%m-%d')

# for forex
# info = pd.read_csv('data.csv',sep=';', skiprows=1, index_col=0)
# info.index = pd.to_datetime(info.index, format='%Y%m%d %H:%M:%S.%f')

# for infosys
data = bt.feeds.PandasData(dataname=info.iloc[-600:,:],
                           open=0,
                           high=1,
                           low=2,
                           close=4,
                           volume=5,
                           openinterest=None)


# for forex
# data = bt.feeds.PandasData(dataname=info.iloc[-1000:,:],
#                            open=0,
#                            high=1,
#                            low=2,
#                            close=3,
#                            volume=None,
#                            openinterest=None)

cerebro.adddata(data)

print('Starting Portfolio Value: %.2f' % cerebro.broker.getvalue())
thestrats = cerebro.run(maxcpus=1)
thestrat = thestrats[0]
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
print('Sharpe Ratio:', thestrat.analyzers.mysharpe.get_analysis())
print('Annual Return:', thestrat.analyzers.annual_return.get_analysis())
print('Trade Analyser:')
trade_analysis = thestrat.analyzers.trade_analyser.get_analysis()
print ('Total Trades')
pretty_print(trade_analysis.total)
print ('Streak Won:')
pretty_print(trade_analysis.streak.won)
print ('Streak Lost:')
pretty_print(trade_analysis.streak.lost)
print ('ProfitAndLoss Total (Gross):')
pretty_print(trade_analysis.pnl.gross)
print ('ProfitAndLoss Total (Net):')
pretty_print(trade_analysis.pnl.net)


#cerebro.plot(style='bar',volume=True)

