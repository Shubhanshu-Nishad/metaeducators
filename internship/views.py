from django.shortcuts import render ,HttpResponse,redirect
# from internship.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime
from internship.models import Courses,Instructor,Testimonials,Verification
from django.contrib.auth import authenticate, login,logout
from django.conf import settings
import requests
import json






# Create your views here.
def project(request):
    return render(request,'internship/project.html')

def courses(request):
    allcourses = Courses.objects.all()
    alinstructor = Instructor.objects.all()
    alltestimonial = Testimonials.objects.all()
    context={'allcourses':allcourses,'alinstructor':alinstructor,'alltestimonial':alltestimonial}
    return render(request,'internship/courses.html',context)

def internship(request):
    return render(request,'internship/internship.html')

def freelancer(request):
    return render(request,'internship/freelancer.html')

def verification(request,slug):
    verification=Verification.objects.filter(slug=slug).first()
    context = {'verification':verification}
    return render(request,'internship/verification.html',context)