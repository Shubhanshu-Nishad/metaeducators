from django.shortcuts import render,HttpResponse
from blog.models import Post

# from . models import Post

# Create your views here.

def bloghome(request ):
    return render(request,'blog/bloghome.html')

def blogpost(request ):
    allPosts=Post.objects.all()
    context={'allPosts': allPosts}
    return render(request,'blog/blogpost.html',context)

def blogread(request,slug):
    readpost=Post.objects.filter(slug=slug).first()
    context={'readpost':readpost}
    return render(request,'blog/blogread.html',context)
# def db(request):
#     return render(request,'blog/db.html')