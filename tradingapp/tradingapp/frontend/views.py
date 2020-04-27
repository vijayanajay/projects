from django.shortcuts import render
from django.conf import settings
import os
from django.http import HttpResponse
from .models import Price, Company
import pandas as pd
from django.conf import settings
import csv, datetime, quandl

quandl.ApiConfig.api_key = 'fRsTyQJZaBbXBcKsnahq'

def test(request):
    #stock_price = quandl.get('BSE/BOM500325')
    #text = len(stock_price)
    text = os.path.join(settings.BASE_DIR, 'templates\\')
    return HttpResponse(text)

def refresh_data(request):
    test_data = "Ajay"
    context = {'test_data': test_data}
    return render(request,'frontend/refresh_data.html', context)

