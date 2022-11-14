from django.contrib import admin
from django.urls import path, include
from application import views

urlpatterns = [
    path('', views.index, name="index")
]