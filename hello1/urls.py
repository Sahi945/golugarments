from django.contrib import admin
from django.urls import path
from hello1 import views
from django.conf.urls import url
urlpatterns = [
    path('', views.index1, name='home1'),
    path('login/', views.loginuser, name='login'),
    path('signup/',views.handleSignup,name='signup'),
    path('signuppage/',views.signupuser,name='signup'),
    path('logout/',views.logoutuser,name='logout'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='sevice'),
    path('Contact_Us/',views.Contact_Us,name='Contact'),
    path('Kids_Wear/',views.Kids_Wear,name="Kids Wear"),
    path('Ladies_Wear/',views.Ladies_Wear,name="ladies Wear"),
    
]
