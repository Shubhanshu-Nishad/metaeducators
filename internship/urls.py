from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings

from internship import views




urlpatterns = [
    path('internship/', views.internship, name='internship'),
    path('courses/', views.courses, name='courses'),
    path('project/', views.project, name='project'),
    path('freelancer/', views.freelancer, name='freelancer'),
     path('verification/<str:slug>', views.verification, name='verification'),
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)