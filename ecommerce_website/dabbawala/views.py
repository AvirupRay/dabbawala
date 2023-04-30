# TODO: Imports

# from django.shortcuts import render
from django.http import *
from django.urls import reverse
from django.contrib import messages
from django.template import loader

from django.contrib.auth.models import User, auth
from django.contrib.auth import get_user_model

from .validate import unauth_user_permission


# TODO: CREATE YOUR VIEWS HERE #

User = get_user_model()

# TODO: Load the templates 
front_page = loader.get_template('frontpage.html')
home_page = loader.get_template('homepage.html')
login_page = loader.get_template('login.html')
signup_page = loader.get_template('register.html')

# TODO: creating view functions

# Front page
def index(request):
    return HttpResponse(front_page.render({}, request))

# user registration
def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        password_again = request.POST['password_again']

        # checking if both passwords are same
        if password == password_again:
            # checking if entered email is already registered
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email already registered')
                return HttpResponseRedirect(reverse('register'))
            # checking if entered email is already registered
            elif User.objects.filter(phone_number = phone_number).exists():
                messages.info(request, 'Phone already registered')
                return HttpResponseRedirect(reverse('register'))
            
            else:
                # if new email and phone number save as user in User table
                user = User.objects.create_user(email = email, name = name, phone_number = phone_number, password = password)
                user.save()
                return HttpResponseRedirect('/login/')
            
        else:
            messages.info(request, "Password does not match")
            return HttpResponseRedirect(reverse('register'))
        
    else:      
        return HttpResponse(signup_page.render({}, request))

# user login
@unauth_user_permission
def login(request):
    if request.method == 'POST':
        # getting email and password from the logiin form to valuidte authentication
        email = request.POST['email']
        password = request.POST['password']
        # authenticate from User table using given parameters
        user = auth.authenticate(email = email, password = password)

        # checking existence of user
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/homepage/')

        else:
            messages.info(request, "invalid credentials !")
            return HttpResponseRedirect(reverse('login'))
        
    else:
        return HttpResponse(login_page.render({}, request))
    

# user logout
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

# Home page
def homepage(request):
    return HttpResponse(home_page.render({}, request))