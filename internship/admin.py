from django.contrib import admin
from internship.models import Courses,Instructor,Testimonials,Verification

# Register your models here.
admin.site.register((Courses,Instructor,Testimonials,Verification))