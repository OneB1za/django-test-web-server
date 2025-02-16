
from django.contrib import admin
from django.urls import path
from . import views
from django_prometheus import exports

urlpatterns = [
    path('', views.home, name='home'),  # отобразит 'web/index.html'
    path("metrics/", exports.ExportToDjangoView, name="metrics"),
]