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
        stock_price = quandl.get(company_info)
        debuginfo = stock_price 
    else:
        debiginfo = "nothing"
    context = {'all_companies': all_companies,
               'debuginfo' : debuginfo}
    return render(request,'frontend/data_index.html', context)


def data_index(request):
    all_companies = Company.objects.all()
    context = {'all_companies': all_companies}
    return render(request,'frontend/data_index.html', context)
