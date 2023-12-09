from django.contrib import admin
from django.urls import path
from .import views
from .import sigupViews,userViews
urlpatterns = [
    
    path('',views.base_page,name="base_page"),
    #path('base_page',views.base_page,name="base_page"),
    path('contact_page/',views.contact_page,name="contact_page"),
    path('signup_page/',views.signup_page,name="signup_page"),
    path('login_page/',views.login_page,name="login_page"),
    path('add_user/',sigupViews.add_user,name="add_user"),

    path('do_login/',sigupViews.do_login,name="do_login"),
    path('logout_user/',sigupViews.logout_user,name="logout_user"),

    ###HOME####
    path('agri_page/',views.agri_page,name="agri_page"),
    path('fitness_page/',views.fitness_page,name="fitness_page"),
    path('homeservice_page/',views.homeservice_page,name="homeservice_page"),
    path('food_page/',views.food_page,name="food_page"),

    path('admin_page/',views.admin_page,name="admin_page"),

    ##USER### 
    path('user_home/',views.user_page,name="user_home"),
    path('user_profile_page/<cuser_id>/',userViews.user_profile_page,name="user_profile_page"),
    path('make_online/',views.make_online,name="make_online"),
    path('create_business/',userViews.create_business,name="create_business"),
]