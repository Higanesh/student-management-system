from django.urls import path
from studentApp.views import *

urlpatterns = [
    path('',loginpage,name="loginpage"),
    path('registerpage',registerpage,name="registerpage"),
    path('userlogin',userlogin,name="userlogin"),
    path('registeruser',registeruser,name="registeruser"),
    path('home',home,name="home"),
    path('userlogout',userlogout,name="userlogout"),
    path('add_studentclass',add_studentclass,name="add_studentclass"),
    path('update_studentclass/<id>',update_studentclass,name="update_studentclass"),
    path('delete_studentclass/<id>',delete_studentclass,name="delete_studentclass"),
    path('add_student',add_student,name="add_student"),
    path('update_student/<id>',update_student,name="update_student"),
    path('delete_student/<id>',delete_student,name="delete_student"),
    path('studentclass_data',studentclass_data,name="studentclass_data"),
    path('student_data',student_data,name="student_data")
]
