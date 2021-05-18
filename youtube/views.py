from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from youtube.models import Video, videocomment, Ytlist
from youtube.templatestags import extra
from math import ceil

# Create your views here.

def playvideo(request ):
    allytlist = Ytlist.objects.all()
    context={'allytlist':allytlist}
    return render(request,'video/playlist.html',context)


def Watchvideo(request,slug):
    watchvideo = Video.objects.filter(slug=slug).first()
    allwatchvideo = Video.objects.all()
    num=watchvideo.numbe
    watchvid = Video.objects.all()
    ytlist= watchvideo.playlist_title
    ytslug= watchvideo.slug
    res = ''.join([i for i in ytslug if not i.isdigit()]) 
    allwatchvideo=[]
    catprods= watchvid.values('playlist_title', 'sno')
    cats= {item["playlist_title"] for item in catprods}
    
    for cat in cats:
        if cat==ytlist:
            prod=watchvid.filter(playlist_title=cat)
            allwatchvideo.append(prod)
    i = sum( [ len(listElem) for listElem in allwatchvideo])
    comments = videocomment.objects.filter(video=watchvideo , parant=None)
    # Managing replies.................................................................................................................
    replies = videocomment.objects.filter(video=watchvideo).exclude(parant=None)
    replyDict = { }
    for reply in replies:
        if reply.parant.sno not in replyDict.keys():
            replyDict[reply.parant.sno] = [reply]
        else:
            replyDict[reply.parant.sno].append(reply) 
    
    if num==1:
        next= res + str(2) 
        prev=res + str(1) 

    elif num==i:
        prev=res  + str(num - 1) 
        next=res + str(num)
    else :
        prev= res  + str(num - 1) 
        next= res + str(num + 1) 
       

  
    context={'allwatchvideo':allwatchvideo,'watchvideo':watchvideo,'comments':comments,'user':request.user, 'replyDict':replyDict,'prev':prev,'next':next}
    return render(request,'video/playvideo.html',context)

def postcomment(request ):
    if request.method=='POST':
        comment =request.POST.get('comment')
        user = request.user
        VideoSno =request.POST.get("VideoSno")
        video=Video.objects.get(sno=VideoSno)
        parantSno=request.POST.get("parantSno")
        if parantSno=="":
            comment = videocomment(comment=comment,user=user,video=video)
            comment.save()
            messages.success(request,' Your comment has been  posted successfully.')
        else:
            parant = videocomment.objects.get(sno=parantSno)
            comment = videocomment(comment=comment,user=user,video=video , parant=parant)
            comment.save()
            messages.success(request,' Your reply  has been  posted successfully.')

    return redirect(f"/playvideo/{video.slug}")



def videosearch(request ):
    
    query=request.GET['query']
    if len(query)>78:
        allvideos=Video.objects.none()
    else:
        allvideoscontent=Video.objects.filter(video_desc__icontains=query)
        allvideostitle=Video.objects.filter(video_title__icontains=query) 
        allvideosplaylist=Video.objects.filter(playlist_title__icontains=query) 
        allplaylist=allvideostitle.union(allvideosplaylist)
        allvideos=allplaylist.union(allvideoscontent)
    if allvideos.count() == 0:
        messages.warning(request,'No search result found. Please refine  your query')
    params={'allvideos':allvideos,'query':query}
    return render(request,'video/videosearch.html',params)
