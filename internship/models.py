from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils.text import slugify



# Create your models here.
class Courses(models.Model):
    sno = models.AutoField(primary_key=True)
    img_link =  models.CharField(max_length=1000)
    payment_link =  models.CharField(max_length=1000,default="")
    duration = models.CharField(max_length=15)
    last_date = models.CharField(max_length=15,default="")
    timeStamp = models.DateTimeField(blank=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
    teacher = models.CharField(max_length=50)
    cost = models.CharField(max_length=50)


    def __str__(self):
        return self.title +' its cost is '+ self.cost + ' & time duration ' + self.duration


class Instructor(models.Model):
    sno = models.AutoField(primary_key=True)
    img_link =  models.CharField(max_length=1000)
    instructor_name = models.CharField(max_length=100)
    about = models.TextField()
    skills = models.CharField(max_length=150)
    instagram_link = models.CharField(max_length=150)
    linkedin_link = models.CharField(max_length=150)
    


    def __str__(self):
        return self.instructor_name +' his/her skills is  '+ self.skills

class Testimonials(models.Model):
    sno = models.AutoField(primary_key=True)
    img_link =  models.CharField(max_length=1000)
    name =  models.CharField(max_length=100)
    work =  models.CharField(max_length=100)
    testimonial =  models.CharField(max_length=256)

    def __str__(self):
        return self.name + ' name '


class Verification(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    course_name =  models.CharField(max_length=150)
    credential_id =  models.CharField(max_length=150)
    slug = models.CharField(max_length=150,unique=True)
    issued_date = models.DateTimeField(blank=True)
    certificate_link =  models.CharField(max_length=1000)
    instructor_name = models.CharField(max_length=150)
    def __str__(self):
        return self.name +"'s certificate of  " + self.course_name