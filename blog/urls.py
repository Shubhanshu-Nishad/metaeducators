from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # path('db', views.db, name='db'),
    path('blogpost/', views.blogpost, name='blogpost'),    
    path('blogread/', views.blogread, name='blogread'),    

]

