from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import pandas as pd
from django.conf import settings
import csv, datetime, quandl
from yahoo_finance import YahooFinance as yf
import pytz
import requests
from bs4 import BeautifulSoup
import talib

tz = pytz.timezone('Asia/Kolkata')
quandl.ApiConfig.api_key = 'fRsTyQJZaBbXBcKsnahq'


def insert_into_db(stock_history, id, source):
    stock_history = stock_history.dropna()
    if source == 'quandl':
        stock_history = stock_history.rename(columns={'Open': 'open_price',
                                                      'High': 'high_price',
                                                      'Low': 'low_price',
                                                      'Close': 'close_price',
                                                      'WAP': 'wap',
                                                      'No. of Shares': 'volume',
                                                      'No. of Trades': 'trades',
                                                      'Total Turnover': 'turnover',
                                                      'Deliverable Quantity': 'deliverable_quantity',
                                                      '% Deli. Qty to Traded Qty': 'percent_del_traded_qty',
                                                      'Spread H-L': 'spread_highLow',
                                                      'Spread C-O': 'spread_closeOpen'})
        stock_history['date'] = stock_history.index
        stock_history['company_id'] = id

    elif source == 'yahoo':
        stock_history = stock_history.rename(columns={'Open': 'open_price',
                                                      'High': 'high_price',
                                                      'Low': 'low_price',
                                                      'Close': 'close_price',
                                                      'Volume': 'volume'})

        stock_history['date'] = stock_history.index
        stock_history.date = pd.to_datetime(stock_history.date, unit='s')
        stock_history['company_id'] = id
        stock_history['period'] = Price.Period.one_min
        # return str(stock_history.date[0])

    entries = []
    for e in stock_history.T.to_dict().values():
        entries.append(Price(**e))
    Price.objects.bulk_create(entries)
    company = Company.objects.get(id=id)
    company.last_updated_date = datetime.datetime.now(tz)
    company.save()

    return stock_history.head().to_json()


def scrap_webpage(url):
    url = 'https://www.moneycontrol.com/mutual-funds/axis-long-term-equity-fund-direct-plan/portfolio-holdings/MAA192'

    page = requests.get(url)
    soup = BeautifulSoup(page.content, features='lxml')
    rows = soup.find_all("span", attrs={"class":"port_right"})
    table = rows[1].text.strip()
    # with open("output1.html", "w") as file:
    #     file.write(str(soup))
    debuginfo = table
    return debuginfo


def get_single_stock_data(id, type='intraday'):

    start_date = DailyStockStats.objects.filter(company__id=id).order_by('date').dates('date', 'day').last()
    if start_date == None:
        price_data = Price.objects.filter(company__id=id)
        start_date = price_data.order_by('date').dates('date', 'day').first()
    else:
        price_data = Price.objects.filter(company__id=id, date__gte=start_date)
    price_data = price_data.to_dataframe()
    price_data['date'] = price_data['date'].dt.date
    end_date = price_data.date.max()

    df = pd.DataFrame()
    while start_date <= end_date:
        df = price_data[price_data['date'] == start_date]
        if len(df) > 0:
            mean = df.close_price.mean()
            day_high = df.close_price.max()
            day_low = df.close_price.min()
            std_dev = df.close_price.std()
            rsi = talib.RSI(df.close_price, 14)
            macd, macdsignal, macdhist = talib.MACD(df.close_price, 12, 26, 9)
            slowk, slowd = talib.STOCH(df.high_price, df.low_price, df.close_price)
            roc = talib.ROC(df.close_price,20)
            willr = talib.WILLR(df.high_price, df.low_price, df.close_price)
            mfi = talib.MFI(df.high_price, df.low_price, df.close_price, df.volume, 14)
            atr = talib.ATR(df.high_price, df.low_price, df.close_price, 14)
            adx = talib.ADX(df.high_price, df.low_price, df.close_price, 14)
            upperband, middleband, lowerband = talib.BBANDS(df.close_price)
        start_date = start_date + datetime.timedelta(days=1)

    debuginfo = upperband
    return debuginfo
