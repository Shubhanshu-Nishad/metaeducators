from django.db import models
# Create your models here.

class Cont(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,)
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
    