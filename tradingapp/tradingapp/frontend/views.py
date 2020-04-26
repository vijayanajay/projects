from django.shortcuts import render
from django.http import HttpResponse
from .models import Price, Company
import pandas as pd
from django.conf import settings
import csv
import datetime

def test(request):
    return HttpResponse("it works fine")
