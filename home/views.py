from django.shortcuts import render 
from home.models import Cont
from django.contrib import messages
from datetime import datetime



# Create your views here.

def home(request):
    return render(request,'home/home.html')


def about(request):
    messages.success(request,"This is About Page1 ")
    return render(request,'home/about.html')


def contact(request):
    messages.success(request,"Can I help you Sir ji ? ")
    if(request.method=='POST'):
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']       
        if len(name)<2 or len(email)<4 or len(phone)<10 or len(content)<5:
            messages.error(request, 'Sorry ,please fill the form in a right manner')
        else:
            contact=Cont(name=name,email=email,phone=phone,desc=content)
            contact.save()
            messages.success(request, 'Form submitted successfully')

    return render(request,'home/contact.html')
    