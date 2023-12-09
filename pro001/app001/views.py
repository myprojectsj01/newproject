from django.shortcuts import render
from django.contrib import messages
from .forms import *
from django.contrib.auth.decorators import login_required
#Create your views here.
def base_page(request):
    return render(request, 'base_home_html/home.html')

def contact_page(request):
    return render(request,'base_home_html/contact.html')

@login_required(redirect_field_name='login_page')
def user_page(request):
    
    user_obj=Cuser.objects.get(admin=request.user.id)
    #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",user_obj)
    return render(request,"user_template/home.html")

@login_required(redirect_field_name='login_page')
def admin_page(request):
    return render(request,'admin_templates/home.html')

def signup_page(request):
    form=Adduser_form()
    context ={ 'form':form }
    return render(request,"signin_login/signup_template.html",context)

def login_page(request):
    return render(request,"signin_login/login_template.html") 



def agri_page(request):
    return render(request,"base_home_html/agri_page.html")

def fitness_page(request):
    return render(request,"base_home_html/fitness_page.html")

def food_page(request):
    return render(request,"base_home_html/food_page.html")

def homeservice_page(request):
    return render(request,"base_home_html/homeservice_page.html")


def make_online(request):
    return render(request,'user_template/make_online_page.html')
