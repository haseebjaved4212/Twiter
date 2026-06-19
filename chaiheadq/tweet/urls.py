
from django.urls import path
from django import dispatch
from . import views



urlpatterns = [
    path('', views.index, name='index'),
]
