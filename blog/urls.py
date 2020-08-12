from django.contrib import admin
from django.urls import path,include,re_path

from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('bloghome/',views.bloghome,name='bloghome'),
    path('blogpost/', views.blogpost, name='blogpost'), 
    path('blogread/<str:slug>', views.blogread, name='blogread'), 
]

# <str:slug_text>