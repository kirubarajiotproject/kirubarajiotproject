from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('home/',include('home.urls')),
    url(r'^$',views.home)
]
