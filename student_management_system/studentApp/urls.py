from django.urls import path
from studentApp.views import *

urlpatterns = [
    path('',student,name="student")
]
