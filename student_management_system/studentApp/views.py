from django.shortcuts import render,redirect,HttpResponse
from studentApp.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def student(request):
    return render(request,"student.html")

def registeruser(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR, "Username already Exists !!!")
            return render(request,"auth.html")
        
        user = User(username=username,email=email)
        user.set_password(password)
        user.save()
        messages.add_message(request, messages.SUCCESS, "Registration successFully !!!!")
        return render(request,'auth.html')
    return render(request,"auth.html")

def userlogin(request):
    # if request.method == 'POST':
    #     form = AuthenticationForm(request,data=request.POST)
    #     if form.is_valid():
    #         user = form.get_user()
    #         login(request,user)
    #         return redirect('student')
    #     else:
    #         messages.error(request, "Invalid username or password.")
    # else:
    #     form = AuthenticationForm()
    return redirect('student')


