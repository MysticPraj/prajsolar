#Createdd by Praj 
# --21:11 23-02-2021 Tuesday
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    return render(request,'contact.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')