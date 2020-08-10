from django.shortcuts import render,HttpResponse
# from . models import Post

# Create your views here.

def home(request):
    return render(request,'blog/bloghome.html')

def blogpost(request):
    return render(request,'blog/blogpost.html')

# def db(request):
#     return render(request,'blog/db.html')