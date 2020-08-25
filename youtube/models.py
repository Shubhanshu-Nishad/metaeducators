from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.text import slugify

# Create your models here.
# class Video(models.Model):
#     video_id = models.AutoField
#     video_title = models.CharField(max_length=300)
#     video_desc = models.TextField()
#     playlist_title = models.CharField(max_length=200, default="")
#     slug=models.CharField(max_length=250,unique=True,default="")
#     video_link=models.CharField(max_length=250,unique=True,default="")
#     upload = models.FileField(upload_to='static/video/playvideo', default="")
#     announcement=models.CharField(max_length=400, default="")

#     def __str__(self):
#         return self.video_title 

# class Playlist(models.Model):
#     playlist_id = models.AutoField
#     playlist_title = models.CharField(max_length=200, default="")
#     playlist_desc = models.CharField(max_length=300)
#     playlist_img = models.ImageField(upload_to='static/video/playlist', default="")
#     slug=models.CharField(max_length=250,unique=True,default="")

#     def __str__(self):
#         return self.playlist_title


class Video(models.Model):
    sno = models.AutoField(primary_key=True)
    video_title = models.CharField(max_length=300)
    video_desc = models.TextField()
    playlist_title = models.CharField(max_length=200, default="")
    slug=models.CharField(max_length=250,unique=True,default="")
    video_link=models.CharField(max_length=250,unique=True,default="")
    image = models.FileField(upload_to='static/video/playvideo', default="")
    timestamp=models.DateTimeField(blank=True)

    def __str__(self):
        return self.video_title + ' of  ' + self.playlist_title



# Model for Comment and reply ...........................................................................................................

class videocomment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    video=models.ForeignKey(Video,on_delete=models.CASCADE)
    parant=models.ForeignKey('self',on_delete=models.CASCADE, null=True)
    timeStamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + '... by ' + self.user.username