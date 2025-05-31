from django.urls import path
from studentApp.views import *

urlpatterns = [
    path('',student,name="student"),
    path('userlogin',userlogin,name="userlogin"),
    path('registeruser',registeruser,name="registeruser")
]
