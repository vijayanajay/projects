from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Price, Company
import pandas as pd
from django.conf import settings
import csv, datetime, quandl
from yahoo_finance import YahooFinance as yf
import pytz
import frontend.utils as utils

tz = pytz.timezone('Asia/Kolkata')
quandl.ApiConfig.api_key = 'fRsTyQJZaBbXBcKsnahq'


def test(request):
    #stock_price = quandl.get('BSE/BOM500325')
    #text = len(stock_price)
    return HttpResponse(text)

def refresh_data(request, id):
    company = Company.objects.get(id=id)
    if company.last_updated_date is None:
        company_info = 'BSE/' + company.bom_id
        stock_history = yf(company.yahoo_id, result_range='7d', interval='1m').result
        debuginfo = utils.insert_into_db(stock_history, company.id, 'yahoo')
    else:
        stock_history = pd.DataFrame()
        latest_price_history = Price.objects.latest('created_at').created_at.astimezone(tz=tz)
        stock_history = yf(company.yahoo_id, result_range='7d', interval='1m').result
        stock_history['date'] = stock_history.index.tz_localize(tz=tz)
        stock_history.date = pd.to_datetime(stock_history.date, unit='s')
        max_date = stock_history.date[-1].to_pydatetime().astimezone(tz=tz)
        stock_history = stock_history[(stock_history.date > latest_price_history) & (stock_history.date <= max_date)]
        debuginfo = utils.insert_into_db(stock_history, company.id, 'yahoo')
    request.session['debuginfo'] = debuginfo
    request.session['debugpage'] = 'data_index'
    return redirect('data_index')


def data_index(request):
    all_companies = Company.objects.all()
    context = {'all_companies': all_companies, 'page': 'data_index'}
    if request.session['debugpage'] == 'data_index' and request.session['debugpage'] is not None:
        if 'debuginfo' in request.session and request.session['debuginfo'] is not None:
            context['debuginfo'] = request.session['debuginfo']
    return render(request,'frontend/data_index.html', context)


def analysis_index(request):
    del request.session['debuginfo']
    context = {'page': 'analysis_index'}
    return render(request,'frontend/analysis_index.html')


def mf_index(request):
    del request.session['debuginfo']
    context = {'page': 'mf_index'}
    context = {'debuginfo': utils.scrap_webpage(url=None)}
    return render(request,'frontend/mf_index.html', context)