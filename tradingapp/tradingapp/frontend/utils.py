from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Price, Company
import pandas as pd
from django.conf import settings
import csv, datetime, quandl
from yahoo_finance import YahooFinance as yf
import pytz

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