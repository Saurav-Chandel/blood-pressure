from django.shortcuts import render
from django.shortcuts import render , redirect , HttpResponseRedirect,HttpResponse
from django.views import  View
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model,login
from django.contrib.auth.hashers import  check_password
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import filters, permissions, serializers, status, viewsets
from .models import *
from user.models import User,Profile
from buisness.models import Buisness

 
def Login(request):
    dictValues={}
    dictValues['error'] = None
    if request.method=='POST':
        Email=request.POST.get('email')
        print(Email)
        Password=request.POST.get('password')
        print(Password)
        try:
            u=User.objects.get(email=Email,is_superuser=True)
            if u.check_password(Password):
                login(request,u)
             
                return HttpResponseRedirect('/adminapp/dashboard/')
            else:
                dictValues['error'] = 'Invalid username/password combination'
        except:
            dictValues['error'] = 'You are not an admin.'
    return render(request,'login.html',dictValues)


@login_required(redirect_field_name='next', login_url='/adminapp/login/')
def dashboard(request):
    data=Profile.objects.all()
    total_users=data.count()
    total_matches=HostMatch.objects.all().count()
    total_buisness=Buisness.objects.all().count()

    context={
        'data':data,
        'total_users':total_users,
        'total_matches':total_matches,
        'total_buisness':total_buisness
    }
    return render(request,'dashboard.html',context)

@login_required(redirect_field_name='next', login_url='/adminapp/login/')
def buisness_management(request):
    data=Buisness.objects.all().values('buisness_images')
    print(data)
    return render(request,'buisness_management.html',{'data':data})    

def buisness_details(request,pk):
    buisness=Buisness.objects.get(id=pk)
    # service=Service.objects.all()
    context={
        'data':buisness,
        # 'service':service
    }
    # print(vars(data1))
    return render(request,'buisness_details.html',context)   

@login_required(redirect_field_name='next', login_url='/adminapp/login/')
def report_management(request):
    data=Report.objects.all()
    return render(request,'report_management.html',{'data':data})    

def suspend(request):
    if request.method == 'GET':
        btn=request.GET.get('conbtn')
        print(btn)
        p=Profile.objects.filter(id=btn).values()
        print(p)
        if p:
            for i in p:
                a=i['user_id_id']
               
        Suspend=User.objects.filter(id=a,is_active=True).values('is_active').update(is_active=False)
        return redirect('dashboard')

    # if request.method == 'POST':
    #     btn1=request.POST.get('conbtn')
    #     print(btn1)
    #     return redirect('dashboard')


@login_required(redirect_field_name='next', login_url='/adminapp/login/')
def user_management(request):
    data=Profile.objects.all()
    return render(request,'user_management.html',{'data':data}) 

from app.SendinSES import *
from user.models import *

class forgot_password(View):
    @csrf_exempt
    def get(self,request):
        return render(request,'forgot_password.html') 
   
    # @csrf_exempt
    def post(self,request):
        try:
           user_email=request.POST.get('email')
           email_body="link is send to your email for forgot your password"
           user=User.objects.get(email=user_email)
           if user:
              send_reset_password_mail(request,user_email,email_body)
              print("mail send")
              return HttpResponse("mail is send successfully")
           else:
               print("thankyou")
               return render(request,"dashboard.html")   
        except:
           return HttpResponse("mail does not exist") 


# @login_required(redirect_field_name='next', login_url='/adminapp/login/')
class  Change_Password(View):
    def get(self,request):
        return render(request,'change_password.html') 

    def post(self,request):    
        old=request.POST.get('old_password')
        print(old)
        new=request.POST.get('new_password')
        print(new)
        # user=User.objects.get(id=user_id)
        u=User.objects.get(password=old)
        print(u)
        if u.checkpassword(old):
            u.set_password(new)
            u.save()
            return HttpResponse('your password is changed')
        return HttpResponse("password did not match")

        # user=User.objects.get(id=user_id)
        # if user.check_password(old_password):
        #     user=User.objects.get(id=user_id)
        #     user.set_password(new_password)
        #     user.save()
        #     return Response({'msg':'your password is changed'})
        # return Response({'msg':'password did not match'})    

    # data=Profile.objects.all()
    # print(data)
    


from django.contrib import auth

def logout(request):
    auth.logout(request)
    return redirect('login')
