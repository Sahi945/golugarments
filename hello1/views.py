from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout,login
# Create your views here.
def index1(request):
    
    return render(request, 'index1.html')
def loginuser(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("/home")
        else:
            messages.error(request, 'Invalid Login please enter the correct credentials!')
            return redirect('/')
            
    return render(request, 'login.html')
def handleSignup(request):
    if request.method=="POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password = request.POST['confirmpassword']
        user = User.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        messages.success(request, 'your account have been successfully created!')

        return redirect("/")

    else:
        return HttpResponse("error 404 not found")
def signupuser(request):
    return render(request, 'signup.html')
def logoutuser(request):
    logout(request)
    messages.success(request, 'Thanks For Visiting Our Website!!!')
    return redirect("/")



def about(request):
    if request.user.is_anonymous:
        return redirect("/login")        
    return render(request, 'about.html')
def Ladies_Wear(request):
    if request.user.is_anonymous:
        return redirect("/login")        
    return render(request, 'ladies.html')
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