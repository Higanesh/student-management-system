from django.shortcuts import render,redirect,HttpResponse
from studentApp.models import *
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def loginpage(request):
    return render(request,"userlogin.html")

def registerpage(request):
    return render(request,"registeruser.html")

@login_required(login_url="/")
def home(request):
    return render(request,"home.html")

# def home(request):
#     if not request.user.is_authenticated:
#         return redirect('/')  # Go to login page at "/"
#     return render(request, "home.html")

def registeruser(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR, "Username already Exists !!!")
            return render(request,'registeruser.html')
        
        user = User(username=username,email=email)
        user.set_password(password)
        user.save()
        messages.add_message(request, messages.SUCCESS, "Registration successFully !!!!")
        return render(request,'registeruser.html')
    return render(request,'registeruser.html')

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR, "invalid credentials!!!")
            return render(request,"userlogin.html")
        
        user = authenticate(username=username,password=password)

        if user == None:
            messages.add_message(request, messages.ERROR, "invalid credentials!!!")
            return render(request,"userlogin.html")
        else:
            login(request,user)
            return redirect('home')
    return render(request,"userlogin.html")

def userlogout(request):
    logout(request)
    return redirect('loginpage')

@login_required(login_url="/")
def add_studentclass(request):
    if request.method == "POST":
        id = request.POST.get("id")
        name = request.POST.get("name")
        section = request.POST.get("section")
        class_teacher = request.POST.get("class_teacher")
        academic_year = request.POST.get("academic_year")

        if id:
            currentStudentClass = StudentClass.objects.get(pk=id)
            currentStudentClass.name = name
            currentStudentClass.section = section
            currentStudentClass.class_teacher = class_teacher
            currentStudentClass.academic_year = academic_year
            currentStudentClass.save()
        else:
            StudentClass.objects.create(name=name, section=section, class_teacher=class_teacher, academic_year=academic_year)
    return render(request,"studentclass_form.html")

def update_studentclass(request,id):
    get_class = StudentClass.objects.get(pk=id)
    update_class = StudentClass.objects.all()
    return render(request,"studentclass_form.html",{"get_class":get_class,"update_class":update_class})

def delete_studentclass(request,id):
    get_class = StudentClass.objects.get(pk=id)
    get_class.delete()
    return render(request,"studentclass_data.html")

@login_required(login_url="/")
def add_student(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        age = request.POST.get("age")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        address = request.POST.get("address")
        roll_number = request.POST.get("roll_number")
        class_name = request.POST.get("class_name")
        admission_date = request.POST.get("admission_date")
        profile_pic = request.FILES.get("profile_pic")
        is_active = request.POST.get("is_active") == 'on'

        class_obj = StudentClass.objects.get(id=class_name)

        Student.objects.create(
            firstname=firstname,
            lastname=lastname,
            age=age,
            email=email,
            phone=phone,
            dob=dob,
            gender=gender,
            address=address,
            roll_number=roll_number,
            class_name=class_obj,
            admission_date=admission_date,
            profile_pic=profile_pic,
            is_active=is_active
        )

    classes = StudentClass.objects.all()
    return render(request,"student_form.html",{"classes":classes})

def update_student(request,id):
    get_student = Student.objects.get(pk=id)
    update_student = Student.objects.all()
    return render(request,"student_form.html",{"get_student":get_student,"update_student":update_student})

def delete_student(request,id):
    get_student = Student.objects.get(pk=id)
    get_student.delete()
    return render(request,"student_data.html")

def studentclass_data(request):
    all_class_data = StudentClass.objects.all()
    return render(request,"studentclass_data.html",{"all_class":all_class_data})

def student_data(request):
    all_students_data = Student.objects.all()
    return render(request,"student_data.html",{"all_student":all_students_data})
    


