from django import forms 
from django.forms import Form
from app001 .models import *


class DateInput(forms.DateInput):
    input_type = "date"

class Adduser_form(forms.Form):
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    repassword=forms.CharField(label="Retype-Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))   
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )   
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    image_file=forms.ImageField(label="Photo")

class User_Profile_Form(forms.Form):
    image_file=forms.ImageField(label="Photo")
    username = forms.CharField(label="Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))     
    gender = forms.ChoiceField(label="Gender", widget=forms.TextInput(attrs={"class":"form-control"}))
    