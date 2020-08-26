from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('playvideo/postcomment/',views.postcomment,name='postcomment'),
    path('playlist/', views.playvideo, name='playvideo'), 
    path('playvideo/<str:slug>', views.Watchvideo, name='Watchvideo'), 
    path('videosearch/', views.videosearch, name='videosearch'), 

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)