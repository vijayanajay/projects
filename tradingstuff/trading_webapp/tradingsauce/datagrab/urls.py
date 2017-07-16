from django.conf.urls import url
from datagrab import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
]