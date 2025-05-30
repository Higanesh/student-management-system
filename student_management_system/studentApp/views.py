from django.shortcuts import render
from studentApp.models import *

# Create your views here.
def student(request):
    return render(request,"student.html")
