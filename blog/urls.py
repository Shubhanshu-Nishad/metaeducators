from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('blogread/postcomment/',views.postcomment,name='postcomment'),
    path('bloghome/',views.bloghome,name='bloghome'), 
    path('blogsearch/', views.blogsearch, name='blogsearch'), 
    path('blogread/<str:slug>', views.blogread, name='blogread'), 
    # API to Post Comment 
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# <str:slug_text>