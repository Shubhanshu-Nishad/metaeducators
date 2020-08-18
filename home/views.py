from django.shortcuts import render ,HttpResponse,redirect
from home.models import Cont
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth import authenticate, login,logout
from django.core import mail
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage

# Create your views here.

#HTML PAGES..............................................................................................................................

def home(request):
    return render(request,'home/home.html')


def donate(request):
    messages.success(request,"This is About Page1 ")
    return render(request,'home/donate.html')


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
            messages.success(request, ' metaeducator : Thanks a lot for connecting with us.')

    return render(request,'home/contact.html')

#Authentication pages....................................................................................................................


def handlesignup(request):

    # if request.method=='POST':
        
        # message= '56952'
        # try:
        #     send_mail('Contact Form',message, settings.EMAIL_HOST_USER,['email'], fail_silently=False )
        # except BadHeaderError:
        #     return HttpResponse('Invalid header found.')

    if request.method=='POST':
        #Get the signup parameters 
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['password2']
        # check for errorness
       
         
        if User.objects.filter(username=username).exists():
            messages.error(request,'metaeducator : Sorry! This username is taken by any another meta user.Please, Sign up with other username.')
            return render(request,'home/home.html')

        if len(username) >15:
            messages.error(request,'metaeducator say, Choose your username with  less that 15 characters .')
            return render(request,'home/home.html')

        if not username.isalnum():
            messages.error(request, 'metaeducator say , Username should contanis alphabet and number only. ')
            return render(request,'home/home.html')

        if password != password2:
            messages.error(request,'Please Enter same password .')
            return render(request,'home/home.html')
      
        # Creating the user 
        myuser=User.objects.create_user(username=username, email=email, password=password)
        # myuser = form.save(commit=False)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        # email_subject='Activate your account'
        # email_body='Test body'

        # email = EmailMessage(
        # email_subject,
        # email_body,
        # 'metaeducatorshubu@gmail.com',
        # ['email'],
        # )
        # email.send(fail_silently=False)
        messages.success(request,'Your metaeducator account has been successfull created ')
        # render redirect('home')
        return render(request,'home/home.html')

    else:
        return HttpResponse('404 - Not found')


def handlelogin(request):
    if request.method=='POST':
        #Get the login parameters 
        loginuname=request.POST['loginuname']
        loginpassword=request.POST['loginpassword']
        user=authenticate(request, username=loginuname, password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully logged in META')
            return render(request,'home/home.html')
        else:
            messages.error(request,'Invalid Credentials,please try again...')
            return render(request,'home/home.html')
    return HttpResponse('404 - Not found')


def handlelogout(request):
    logout(request)
    messages.success(request,'Successfully logged out your metaeducator')
    return render(request,'home/home.html')