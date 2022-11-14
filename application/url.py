from django.contrib import admin
from django.urls import path, include
from application import views

urlpatterns = [
    path('', views.index, name="index"),
    path('callback', views.callback.as_view(), name="callback"),
    path('home', views.home, name="home"),
]