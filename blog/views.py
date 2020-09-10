from django.shortcuts import render,HttpResponse,redirect
from blog.models import Post, blogcomment
from django.contrib import messages
from blog.templatestags import extras

# from . models import Post

# Create your views here.

# Managing HTML PAGES....................................................................................................................

def bloghome(request ):
    allposts = Post.objects.all()
    context={'allposts':allposts}
    return render(request,'blog/bloghome.html',context)


def blogread(request,slug):
    # readpost=Post.objects.filter(slug=slug).first()
    readpost=Post.objects.filter(slug=slug).first()
    comments=blogcomment.objects.filter(post=readpost , parant=None)
    # Managing replies..................................................................................................................
    replies=blogcomment.objects.filter(post=readpost).exclude(parant=None)
    replyDict = { }
    for reply in replies:
        if reply.parant.sno not in replyDict.keys():
            replyDict[reply.parant.sno] = [reply]
        else:
            replyDict[reply.parant.sno].append(reply) 
    context={'readpost':readpost,'comments':comments,'user':request.user, 'replyDict':replyDict}
    return render(request,'blog/blogread.html',context)

# Managing MOdels........................................................................................................................

# def blogsearch(request ):
    
#     query=request.GET['query']
#     if len(query)>78:
#         allposts=Post.objects.none()
#     else:
#         allpostscontent=Post.objects.filter(content__icontains=query)
#         allpoststitle=Post.objects.filter(title__icontains=query) 
#         allposts=allpoststitle.union(allpostscontent)
#     if allposts.count() == 0:
#         messages.warning(request,'No search result found. Please refine  your query')
#     params={'allposts':allposts,'query':query}
#     return render(request,'blog/blogsearch.html',params)


def postcomment(request ):
    if request.method=='POST':
        comment =request.POST.get('comment')
        user = request.user
        PostSno =request.POST.get("PostSno")
        post=Post.objects.get(sno=PostSno)
        parantSno=request.POST.get("parantSno")
        if parantSno=="":
            
            comment = blogcomment(comment=comment,user=user,post=post)
            comment.save()
            messages.success(request,' Your comment has been  posted successfully.')
        else:
            parant = blogcomment.objects.get(sno=parantSno)
            comment = blogcomment(comment=comment,user=user,post=post , parant=parant)
            comment.save()
            messages.success(request,' Your reply  has been  posted successfully.')


    return redirect(f"/blogread/{post.slug}")




# def db(request):
#     return render(request,'blog/db.html')