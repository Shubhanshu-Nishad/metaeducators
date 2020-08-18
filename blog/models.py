from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.text import slugify

# Create your models here.

# Model for Articles.....................................................................................................................

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
    author = models.CharField(max_length=50)
    slug=models.CharField(max_length=155,unique=True)
    timeStamp=models.DateTimeField(blank=True)


    # def save(self, *args, **kwargs):
    #     self.slug = slugify(title)
    #     super(Post, self).save(*args, **kwargs)    


    def __str__(self):
        return self.title +' by '+ self.author


    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Article.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug
 
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

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
    
