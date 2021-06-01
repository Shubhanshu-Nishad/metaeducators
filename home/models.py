from django.db import models
from django.conf import settings
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



class Donar(models.Model):
    donar_id = models.AutoField(primary_key=True)
    donar_name = models.CharField(max_length=100,)
    donar_amount = models.CharField(max_length=25)
    donar_professional = models.CharField(max_length=13)
    donar_desc = models.TextField()
    img_link=  models.CharField(max_length=5000)

    def __str__(self):
        return  self.donar_name +  " donate "  +  self.donar_amount
    
class Winner(models.Model):
    winner_id = models.AutoField(primary_key=True)
    winner_name = models.CharField(max_length=100,default="")
    winner_desc = models.TextField()
    img_link=  models.CharField(max_length=1000,default="")
    url_name=  models.CharField(max_length=100,default="")
    url=  models.CharField(max_length=1000,default="")
    timeStamp=models.DateTimeField(blank=True)
     
    
    def __str__(self):
        return  self.winner_name

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    customer_desc = models.TextField()
    customer_urls = models.CharField(max_length=100,default="")
    img_link=  models.CharField(max_length=5000)
   
    timeStamp=models.DateTimeField(blank=True)
     
    
    def __str__(self):
        return  self.customer_name

class News_letter(models.Model):
    email = email = models.CharField(max_length=100)

    def __str__(self):
        return  self.email

class Notice(models.Model):
    notice=models.TextField()
    
    def __str__(self):
        return  self.notice


class Announcement(models.Model):
    announcement_title =  models.CharField(max_length=100)
    announcement_desc = models.TextField()
    link =  models.CharField(max_length=400)
    about_link = models.CharField(max_length=400)
    img_link=  models.CharField(max_length=5000)
    

    def __str__(self):
        return  self.announcement_title

class Correction_form(models.Model):
    sno = models.AutoField(primary_key=True)
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default='',max_length=100,)
    u_name = models.CharField(max_length=100)
    correction = models.CharField(max_length=500)
    def __str__(self):
        return " Request from  " + self.u_name

class Update_profile(models.Model):
    sno = models.AutoField(primary_key=True)
    user_name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,default='',max_length=100,)
    request_of_update = models.CharField(max_length=10)
    edu_qul = models.CharField(max_length=100,)
    email = models.CharField(max_length=90)
    phone = models.CharField(max_length=13)
    wmobile = models.CharField(max_length=13)
    teacher = models.CharField(max_length=3,default="")
    about=models.CharField(max_length=150)
    street=models.CharField(max_length=100)    
    city =models.CharField(max_length=100)    
    state =models.CharField(max_length=100)    
    zip_code =models.CharField(max_length=20)
    linkedin = models.CharField(max_length=100)   
    github = models.CharField(max_length=100)   
    instagram = models.CharField(max_length=100)
    twitter = models.CharField(max_length=100)
    remark = models.CharField(max_length=200,default="")
    img_link = models.CharField(max_length=200,default="https://bootdey.com/img/Content/avatar/avatar7.png")
    are_of_working_in_metaeducator = models.CharField(max_length=3,default="NO")
    position = models.CharField(max_length=100,default="")
    are_we_helping_in_project = models.CharField(max_length=3,default="No")
    project_name = models.CharField(max_length=100,default="")
    are_you_doing_intrenship_through_metaeducator = models.CharField(max_length=3,default="No")
    company_name = models.CharField(max_length=100,default="")
    def __str__(self):
        return  " Request from  "  +  self.email 