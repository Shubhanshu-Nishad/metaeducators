from django.db import models
from django.utils.timezone import now
# Create your models here.

class Cont(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,)
    edu_qul = models.CharField(max_length=100,)
    email = models.CharField(max_length=90)
    phone = models.CharField(max_length=13)
    desc = models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return 'Message from ' +self.name+ ' with email '+ self.email


# class handlesignup(models.Model):
#     uname= models.AutoField(primary_key=True)
#     fname= models.CharField(max_length=100)
#     lname= models.CharField(max_length=100)
#     email = models.CharField(max_length=90)
#     password = models.CharField(max_length=20)



class Donar(models.Model):
    donar_id = models.AutoField(primary_key=True)
    donar_name = models.CharField(max_length=100,)
    donar_amount = models.CharField(max_length=25)
    donar_professional = models.CharField(max_length=13)
    donar_desc = models.TextField()
    image = models.ImageField(upload_to="static/donars", default="")

    def __str__(self):
        return  self.donar_name +  " donate "  +  self.donar_amount
    
class Winner(models.Model):
    winner_id = models.AutoField(primary_key=True)
    winner_name = models.CharField(max_length=100,default="")
    winner_desc = models.TextField()
    image = models.ImageField(upload_to="static/winner", default="")
    timeStamp=models.DateTimeField(blank=True)
     
    
    def __str__(self):
        return  self.winner_name

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    customer_desc = models.TextField()
    customer_urls = models.CharField(max_length=100,default="")
    image = models.ImageField(upload_to="static/customer", default="")
    timeStamp=models.DateTimeField(blank=True)
     
    
    def __str__(self):
        return  self.customer_name


class Notice(models.Model):
    notice=models.TextField()
    
    def __str__(self):
        return  self.notice


class Announcement(models.Model):
    announcement_title =  models.CharField(max_length=100)
    announcement_desc = models.TextField()
    link =  models.CharField(max_length=400)
    about_link = models.CharField(max_length=400)
    image = models.ImageField(upload_to="static/annoucement", default="")

    def __str__(self):
        return  self.announcement_title