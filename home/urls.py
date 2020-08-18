from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home, name='home'),
    path('donate/', views.donate, name='donate'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.handlesignup, name='handlesignup'),
    path('logout/', views.handlelogout, name='handlelogout'),
    path('login/', views.handlelogin, name='handlelogin'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)