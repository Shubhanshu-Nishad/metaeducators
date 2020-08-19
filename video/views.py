from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages

# Create your views here.


# Managing HTML PAGES....................................................................................................................

def playlist(request ):
    return render(request,'video/playlist.html')


def playvideo(request ):
    return render(request,'video/playvideo.html')