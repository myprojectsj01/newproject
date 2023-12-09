from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from app001.EmailBackEnd import EmailBackEnd
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from .forms import *



def user_profile_page(request,cuser_id):
    request.session['student_id'] = cuser_id
    cusers_objs = Cuser.objects.get(admin=cuser_id)
   
    return render(request,"user_template/user_profile.html")

def create_business(request):
    
    if request.method == 'POST' :
        
        company =    request.POST['companyname']
        email   =    request.POST['emailid']
        phone   =    request.POST['phoneno']
        landlineno=  request.POST['lineno']
        web     =    request.POST['webpage']
        buskey  =    request.POST['businesskey']
        area    =    request.POST['business_type']
        profile =    request.FILES['profile']
        user_obj=    Cuser.objects.get(admin=request.user.id)
        com_create=  make_online_webpage.objects.create(admin=user_obj,companyname=company,
                                                       emailid=email,phoneno=phone,
                                                       landline=landlineno,webpage=web,
                                                       businesskey=buskey,typeoption=area, 
                                                       profimage=profile) 
        messages.success(request,"Registered Successfully")
        return redirect('make_online')
    else:
        messages.error(request,"error")
        return redirect('make_online')