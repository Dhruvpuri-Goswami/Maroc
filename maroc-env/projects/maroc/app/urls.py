from django.contrib import admin
from django.urls import path,include
from . import views
from  django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name="index"),
    path('index',views.index,name="index"),
    path('signin',views.signin,name="signin"),
    path('signup',views.signup,name="signup"),  
    path('home',views.home,name="home") ,
    path('activate/<uname>',views.activate,name="activate") ,
    path('logout',views.logout,name="logout") ,
    path('forgot',views.forgot,name="forgot") ,
    path('changepassword/<token>',views.changepassword,name="changepassword") ,
    path('weightloss',views.weightloss,name="weightloss"),
    path('pcos',views.pcos,name="pcos")
]