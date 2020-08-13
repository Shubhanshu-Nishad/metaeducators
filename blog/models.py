from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

# Model for Articles.....................................................................................................................

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.CharField(max_length=50)
    slug=models.CharField(max_length=155)
    timeStamp=models.DateTimeField(blank=True)

    def __str__(self):
        return self.title +' by '+ self.author

# Model for Comment and reply ...........................................................................................................

class blogcomment(models.Model):
    sno = models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    parant=models.ForeignKey('self',on_delete=models.CASCADE, null=True)
    timeStamp=models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:13] + '... by ' + self.user.username
    
