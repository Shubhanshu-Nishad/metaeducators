from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.home, name='home'),
    path('donate/', views.donate, name='donate'),
    path('contact/', views.contact, name='contact'),
    path('correction_form/', views.correction_form, name='correction_form'),
    path('newsletter/', views.newsletter, name='newsletter'),
    path('W&C/', views.winner, name='W&C'),
    path('service/', views.service, name='service'),
    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_in'),
    path('signup/', views.handlesignup, name='handlesignup'),
    path('logout/', views.handlelogout, name='handlelogout'),
    path('login/', views.handlelogin, name='handlelogin'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('update_profile/', views.update_profile, name='update_profile'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)