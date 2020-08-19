from django.contrib import admin
from django.urls import path,include,re_path

from . import views

urlpatterns = [
    path('playlist/', views.playlist, name='playlist'), 
    path('playvideo/', views.playvideo, name='playvideo'), 

]