from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
import pandas as pd
import quandl
from yahoo_finance import YahooFinance as yf
import pytz
import frontend.utils as utils
import frontend.forms
import logging

tz = pytz.timezone('Asia/Kolkata')
quandl.ApiConfig.api_key = 'fRsTyQJZaBbXBcKsnahq'
logger = logging.getLogger(__name__)


def test(request):
    stock_price = quandl.get('BSE/BOM500325')
    text = len(stock_price)
    return HttpResponse(text)


def refresh_data(request, id):
    company = Company.objects.get(id=id)
    if company.last_updated_date is None:
        stock_history = yf(company.yahoo_id, result_range='7d', interval='1m').result
        utils.insert_into_db(stock_history, company.id, 'yahoo', '1m')
        stock_history_daily = yf(company.yahoo_id, result_range='6mo', interval='1d').result
        debuginfo = utils.insert_into_db(stock_history_daily, company.id, 'yahoo', '1d')
    else:
        stock_history = pd.DataFrame()
        stock_history_daily = pd.DataFrame()
        latest_price_history = IntradayPrice.objects.latest('created_at').created_at.astimezone(tz=tz)
        latest_daily_price_history = DailyPrice.objects.latest('created_at').created_at.astimezone(tz=tz)
        stock_history = yf(company.yahoo_id, result_range='7d', interval='1m').result
        stock_history_daily = yf(company.yahoo_id, result_range='6mo', interval='1d').result
        stock_history['date'] = stock_history.index.tz_localize(tz=tz)
        stock_history_daily['date'] = stock_history_daily.index.tz_localize(tz=tz)
        stock_history.date = pd.to_datetime(stock_history.date, unit='s')
        stock_history_daily.date = pd.to_datetime(stock_history_daily.date, unit='s')
        max_date = stock_history.date[-1].to_pydatetime().astimezone(tz=tz)
        max_daily_date = stock_history_daily.date[-1].to_pydatetime().astimezone(tz=tz)
        stock_history = stock_history[(stock_history.date > latest_price_history) & (stock_history.date <= max_date)]
        stock_history_daily = stock_history_daily[(stock_history_daily.date > latest_daily_price_history) &
                                                  (stock_history_daily.date <= max_daily_date)]
        utils.insert_into_db(stock_history, company.id, 'yahoo', '1m')
        debuginfo = utils.insert_into_db(stock_history_daily, company.id, 'yahoo', '1d')
    request.session['debuginfo'] = debuginfo
    return redirect('data_index')


def data_index(request):
    all_companies = Company.objects.all()
    context = {'all_companies': all_companies}
    if 'debuginfo' in request.session and request.session['debuginfo'] is not None:
        context['debuginfo'] = request.session['debuginfo']
    logger.info('inside data_index')
    return render(request, 'frontend/data_index.html', context)


def analysis_index(request, id):
    if request.method == 'POST':
        form = frontend.forms.SelectCompany(request.POST)
        if form.is_valid():
            context = {'debuginfo': 'success'}
    else:
        form = frontend.forms.SelectCompany()
        context = {'form': form}
        company = Company.objects.get(id=id)
        debuginfo = company.update_daily_stats()
        #debuginfo = frontend.utils.get_single_stock_data(id)
        context['debuginfo'] = debuginfo
        # context['price_data'] = price_data
    return render(request, 'frontend/analysis_index.html', context)


def mf_index(request):
    context = {'debuginfo': utils.scrap_webpage(url=None)}
    return render(request, 'frontend/mf_index.html', context)


def analysis_single_stock(request, id):
    context = {'debuginfo': id}
    return render(request, 'frontend/analysis_index.html', context)
