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


def insert_into_db(stock_history, id, source, interval):
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
        # return str(stock_history.date[0])

    entries = []
    if interval == '1m':
        for e in stock_history.T.to_dict().values():
            entries.append(IntradayPrice(**e))
        IntradayPrice.objects.bulk_create(entries)
    elif interval == '1d':
        for e in stock_history.T.to_dict().values():
            entries.append(DailyPrice(**e))
        DailyPrice.objects.bulk_create(entries)
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


