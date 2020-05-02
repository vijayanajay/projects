from django.urls import path
from .views import *

urlpatterns = [
        path('test', test),
        path('refresh_data/<int:companyid>', refresh_data, name='refresh_data'),
        path('refresh_data/', refresh_data, name='refresh_data'),
        path('', data_index),
]