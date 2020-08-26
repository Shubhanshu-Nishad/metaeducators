from django.shortcuts import render ,HttpResponse,redirect
from home.models import Cont,Donar,Winner,Customer,Notice,Announcement
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth import authenticate, login,logout
from django.conf import settings


# Create your views here.

#HTML PAGES..............................................................................................................................

def home(request):
    notice=Notice.objects.all()
    announcement = Announcement.objects.all()
    context={'notices':notice,'announcements':announcement}
    return render(request,'home/home.html',context)


def winner(request):
    winner = Winner.objects.all()
    context = {'Winners': winner}
    return render(request,'home/W&C.html',context)


def service(request):
    customer = Customer.objects.all()
    context = {'Customers': customer}
    return render(request,'home/service.html',context)

def donate(request):
    Donars = Donar.objects.all()
    nSlides=len(Donars)
    params={'no_of_slides':nSlides, 'range':range(1,nSlides),'Donar': Donars}
    messages.success(request,"मौका मिले किसी को मदद करने का,तो बनना सारथी  ना कि स्वार्थी ... ")
    return render(request,'home/donate.html',params)


def contact(request):
    messages.success(request,"Can I help you Sir ? ")
    if(request.method=='POST'):
        name=request.POST['name']
        edu_qul = request.POST['edu_qul']
        email=request.POST['email']
        phone=request.POST['phone']
        content=request.POST['content']       
        if len(name)<2 or len(email)<4 or len(phone)<10 or len(content)<5:
            messages.error(request, 'Sorry ,please fill the form in a right manner')
        else:
            contact=Cont(name=name,email=email,phone=phone,desc=content,edu_qul=edu_qul)
            contact.save()
            messages.success(request, ' metaeducator : Thanks a lot for connecting with us . Very soon I will contact with you...')

    return render(request,'home/contact.html')

#Authentication pages....................................................................................................................


def handlesignup(request):
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
  
        myuser=User.objects.create_user(username=username, email=email, password=password)
        # myuser = form.save(commit=False)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        messages.success(request,'Your metaeducator account has been successfull created & A Confirmations e-mail has been send to your register email address ,Please verified it ')
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