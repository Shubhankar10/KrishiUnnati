from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'index.html')

def detail(request):
    return render(request,'details.html')

def login(request):
    return render(request,'login.html')

def signup(request):
    return render(request,'signup.html')

def map(request):
    return render(request,'map.html')
'''
def detail(request):
    return render(request,'details.html')
'''