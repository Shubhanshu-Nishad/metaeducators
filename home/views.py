from django.shortcuts import render ,HttpResponse,redirect
from home.models import Cont,Donar,Winner,Customer,Notice,Announcement,Update_profile,News_letter,Correction_form
from django.contrib import messages
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth import authenticate, login,logout
from django.conf import settings
import requests
import json

# Create your views here.

#HTML PAGES..............................................................................................................................

def home(request):
    notice=Notice.objects.all()
    announcement = Announcement.objects.all()
    permission = Update_profile.objects.all().filter(request_of_update='yes')
    query=[p.user_name for p in permission]
    ls = list(query)
    context={'notices':notice,'announcements':announcement,'permissions':permission,'query':query}
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

######################################################### Correction Form ################################################################

def correction_form(request):
    if request.method=="POST":
        user_name= request.user
        u_name = request.POST['u_name']
        correction =request.POST['content']
        correction_form=Correction_form(user_name=user_name,u_name=u_name,correction=correction)
        correction_form.save()
        messages.success(request, 'Thanks ! for reporting error in profile data , very soon we will correct it .')
    return render(request,'home/home.html')


############################################################################################################################################


def profile(request):
    users_name = request.user
    try:
        update_profile = Update_profile.objects.get(user_name=request.user)
        context = {'User':update_profile}
        return render(request,'home/profile.html',context)
    except:
        return render(request,'home/fake_profile.html')
    



############################################################################################################################################
def edit_profile(request):
    return render(request,'home/edit_profile.html')

def sign_in(request):
    return render(request,'home/sign_in.html')

def sign_up(request):
    return render(request,'home/sign_up.html')

def newsletter(request):
    if(request.method=='POST'):
        email=request.POST['email']
        if len(email)>11 and len(email)<100:
            newsletter=News_letter(email=email)
            newsletter.save()
            messages.success(request, ' Thanks for subscribing our news letter .')
        else:
            messages.error(request, 'Sorry ,It seems to be you have done any mistake. Try Again after 5 second .')
    return render(request,'home/home.html')    
        
def contact(request):
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



def update_profile(request):
    if request.method=="POST":
        user_name= request.user
        request_of_update = "yes"
        edu_qul =request.POST['higher_education']
        email =request.POST['email']
        phone =request.POST['phone']
        wmobile =request.POST['wphone']
        teacher =request.POST['teacher']
        about =request.POST['about']
        street =request.POST['street']
        city =request.POST['city']
        state =request.POST['state']
        zip_code =request.POST['zip']
        linkedin =request.POST['linkdinid']
        github =request.POST['githubid']
        instagram =request.POST['instagramid']
        twitter =request.POST['twitterid']
        update_profile=Update_profile(user_name=user_name,request_of_update=request_of_update,edu_qul=edu_qul,email=email,phone=phone,wmobile=wmobile,teacher=teacher,about=about,street=street,city=city,state=state,zip_code=zip_code,linkedin=linkedin,github=github,instagram=instagram,twitter=twitter)
        update_profile.save()
        messages.success(request, 'Thanks ! After verifying your detail.')
    return render(request,'home/home.html')





#Authentication pages....................................................................................................................


def handlesignup(request):
    if request.method=='POST':
        #Get the signup parameters 
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        password2=request.POST['repassword']
        # check for errorness
         
        if User.objects.filter(username=username).exists():
            messages.error(request,'metaeducator : Sorry! This username is taken by any another meta user.Please, Sign up with other username.')
            return render(request,'home/sign_up.html')

        if len(username) >15:
            messages.error(request,'metaeducator say, Choose your username with  less that 15 characters .')
            return render(request,'home/sign_up.html')

        if not username.isalnum():
            messages.error(request, 'metaeducator say , Username should contanis alphabet and number only. ')
            return render(request,'home/sign_up.html')

        if password != password2:
            messages.error(request,'Please Enter same password .')
            return render(request,'home/sign_up.html')
  
        myuser=User.objects.create_user(username=username, email=email, password=password)
        # myuser = form.save(commit=False)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        print(myuser)
        messages.success(request,'Your metaeducator account has been successfull created & A Confirmations e-mail has been send to your register email address ,Please verified it ')
        # render redirect('home')
        return redirect('/')

    else:
        return render(request, 'home/sign_up.html')


def handlelogin(request):
    if request.method=='POST':
        #Get the login parameters 
        loginuname=request.POST['loginuname']
        loginpassword=request.POST['loginpassword']
        print(loginuname,loginpassword)
        user=authenticate(request, username=loginuname, password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully logged in Metaeducator ')
            return redirect('/')
        else:
            messages.error(request,'Invalid Credentials,please try again...')
            return render(request,'home/home.html')
    return render(request,'home/sign_in.html')


def handlelogout(request):
    logout(request)
    messages.success(request,'Successfully logged out your metaeducator')
    return redirect('/')


