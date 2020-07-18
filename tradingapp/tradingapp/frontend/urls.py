from django.urls import path
from .views import *

urlpatterns = [
        path('test', test),
        path('refresh_data/<int:id>', refresh_data, name='refresh_data'),
        path('refresh_data/', refresh_data, name='refresh_data'),
        path('', data_index, name='data_index'),
        path('analysis', analysis_index, name='analysis_index'),
]