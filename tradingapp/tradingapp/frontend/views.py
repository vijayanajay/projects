from django.shortcuts import render
from django.http import HttpResponse
from .models import Price, Company
import pandas as pd
from django.conf import settings
import csv, datetime, quandl

quandl.ApiConfig.api_key = 'fRsTyQJZaBbXBcKsnahq'

def test(request):
    stock_price = quandl.get('BSE/BOM500325')
    return HttpResponse(len(stock_price))

def refresh_data(request):
    test_data = "Ajay"
    context = {'test_data': test_data}
    return render(request,'frontend/refresh_data.html', context)

