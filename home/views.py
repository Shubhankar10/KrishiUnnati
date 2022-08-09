from django.shortcuts import render
from django.http import HttpResponse
from chatBackend.chat import chat
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import NewUser


# Create your views here.

class mainpage(TemplateView):
    Template_view = "index.html"

    def get(self, request):
        return render(request, self.Template_view)

    def post(self, request):
        if request.method == 'POST':
            user = request.POST.get('input', False)
            context = {"user": user, "bot": chat(request)}

        return render(request, self.Template_view, context)


# Register/Login function se redirect hona hai main page pe.
def index(request):
    return render(request, 'index.html')


def detail(request):
    return render(request, 'details.html')


def map(request):
    return render(request, 'map.html')


'''
def detail(request):
		return render(request,'details.html')
'''


# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # username = request.POST['username']
        email = request.POST['email']
        # dob = request.POST['dob']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if NewUser.objects.filter(email=email).exists(): #Same Email so again redirect to signup page
                messages.info(request, 'email already exists')
                return redirect(register)
            else:
                user = NewUser.objects.create_user(email=email, first_name=first_name, password=password)
                user.set_password(password)
                user.save()
                print("success")
                auth.login(request, user)
                # return redirect(home)
                return redirect(index)
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
    else:
        print("no post method")
        return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        email = request.POST['email']
        print(email)
        password = request.POST['password']
        print(password)
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect(index)
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login_user')
    else:
        return render(request, 'login.html')


def logout_user(request):
    auth.logout(request)
    return redirect(index)
    # return render(request, 'index.html')
