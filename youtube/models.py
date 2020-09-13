from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.text import slugify

# Create your models here.

class Video(models.Model):
    sno = models.AutoField(primary_key=True)
    video_title = models.CharField(max_length=300)
    video_desc = models.TextField()
    playlist_title = models.CharField(max_length=200, default="")
    slug=models.CharField(max_length=250,unique=True,default="")
    video_link=models.CharField(max_length=250,unique=True,default="")
    numbe=models.IntegerField(default="0")

    def __str__(self):
        return self.video_title + ' of  ' + self.playlist_title + ' (' + str(self.numbe) + ')'




class Ytlist(models.Model):
    sno = models.AutoField(primary_key=True)
    ytlist_desc = models.TextField()
    ytlist_title = models.CharField(max_length=200, default="")
    slug=models.CharField(max_length=250,unique=True,default="")
    img_link=  models.CharField(max_length=5000)

    def __str__(self):
        return self.ytlist_title 
        return self.ytlist_title + ' of  ' + self.slug



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