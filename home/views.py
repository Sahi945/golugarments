from django.shortcuts import render,HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout,login

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'index.html')
    



    
def about(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'about.html')
   
def service(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'services.html')
def Kids_Wear(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,'kidswear.html')


def Contact_Us(request):
    if request.user.is_anonymous:
        return redirect("/login")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, phone = phone , desc = desc , date = datetime.today())
        contact.save()
        messages.success(request, 'Your Message Has been Sent!')
    return render(request, 'contact.html')
def Ladies_Wear(request):
    if request.user.is_anonymous:
        return redirect("/login")        
    return render(request, 'ladies.html')