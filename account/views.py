from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login,logout

def register(request):
    if request.method =='POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        username= request.POST['username']
        email= request.POST['email']
        password1= request.POST['password1']
        password2= request.POST['password2']

        user = User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
        user.save
        messages.info(request,'Saved user')
        return redirect('/')
    else:
        return render(request,'register.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password= request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            auth_login(request,user)
            return redirect('/')
        else:
            messages.error(request,"Invalid Credential")
            return render(request,'login.html')
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')