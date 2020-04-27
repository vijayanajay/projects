from django.urls import path
from .views import *

urlpatterns = [
        path('test', test, name = 'test'),
        path('refresh_data', refresh_data, name = 'refresh_data')
]