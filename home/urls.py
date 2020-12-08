from django.contrib import admin
from django.urls import path
from home import views
from django.conf.urls import url


urlpatterns = [
    
    path('', views.index, name='home'),
    path('about/',views.about,name='about'),
    path('service/',views.service,name='sevice'),
    path('Contact_Us/',views.Contact_Us,name='Contact'),
    path('Kids_Wear/',views.Kids_Wear,name="Kids Wear"),
    
    
]