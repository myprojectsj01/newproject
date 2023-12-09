from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from app001.EmailBackEnd import EmailBackEnd
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from .forms import *

def add_user(request):
    
        form=Adduser_form(request.POST,request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            address = form.cleaned_data['address']
            gender = form.cleaned_data['gender']
            imagefile=form.cleaned_data['image_file']
            user = CustomUser.objects.create_user(username=username, password=password,email=email,user_type=2 ) 
            user.cuser.name=username     
            user.cuser.email=email
            user.cuser.password=password
            user.cuser.address = address     
            user.cuser.gender = gender
            user.cuser.image_file=imagefile
            user.save()
            #imagefile.save() 
            messages.success(request,"Successfull !!! ")
            return redirect('signup_page')   
    
        else:
            messages.error(request,"Please try again...")
            return redirect('signup_page')

def do_login(request):
    if request.method != "POST":
            return HttpResponse("<h2>## Error 404 ##</h2>")
    else:
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = EmailBackEnd.authenticate(request,username, password)
            if user != None:
                login(request, user)
                user_type = user.user_type
                if user_type == '1':

                    return redirect('admin_page')
                        
                elif user_type == '2':
                    #use=Cuser.objects.get(name=request.user.username)
                    # return HttpResponse("Student Login")
                    return redirect('user_home')
                #elif user_type == '3':
                    # return HttpResponse("Staff Login")
                   # return redirect('staff_home')
                else:
                    messages.error(request, "Invalid Login!")
                    return redirect('login_page')
            else:
                messages.error(request, "Invalid Login Credentials!")
                return redirect("login_page")
                


def logout_user(request):
    logout(request)
    return redirect('login_page')
    