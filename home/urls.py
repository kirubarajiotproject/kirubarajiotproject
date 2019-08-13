from django.conf.urls import url
from . import views
from home.views import ajax_data
urlpatterns = [
    url(r'^$', views.index),
    url('data', ajax_data)
]