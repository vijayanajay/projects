from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Price, Company
import pandas as pd
from django.conf import settings
import csv, datetime, quandl

quandl.ApiConfig.api_key = 'fRsTyQJZaBbXBcKsnahq'

def test(request):
    #stock_price = quandl.get('BSE/BOM500325')
    #text = len(stock_price)
    return HttpResponse(text)

def refresh_data(request, id):
    all_companies = Company.objects.all()
    company = Company.objects.get(id=id)
    if company.last_updated_date is None:
        company_info = 'BSE/' + company.bom_id
        stock_history = quandl.get(company_info)
        debuginfo = insert_into_db(stock_history, company.id).head()
    else:
        debuginfo = str(type(company.last_updated_date))
    request.session['debuginfo'] = debuginfo
    return redirect('data_index')


def data_index(request):
    all_companies = Company.objects.all()
    context = {'all_companies': all_companies}
    if 'debuginfo' in request.session and request.session['debuginfo'] is not None:
        context['debuginfo'] = request.session['debuginfo']
    return render(request,'frontend/data_index.html', context)


def insert_into_db(stock_history, id):
    stock_history = stock_history.dropna()
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
    
    entries = []
    for e in stock_history.T.to_dict().values():
        entries.append(Price(**e))
    Price.objects.bulk_create(entries)
    company = Company.objects.get(id=id)
    company.last_updated_date = datetime.datetime.today()
    company.save()
    
    return stock_history
    