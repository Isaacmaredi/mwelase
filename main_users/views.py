from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth import authenticate, login
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import User
from .forms import UserRegistrationForm


# User Registration 
def register(request):
    form = UserRegistrationForm()
    
    if request.method == 'POST': #if the form has been submitted
        form = UserRegistrationForm(request.POST) #form bound with post data
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('main_users:login')
    else:
        form = UserRegistrationForm()
    return render(request, 'main_users/register.html', {'form':form})


# User Login  
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request,username=username, password=password)

        if user is not None:
            login(request)
            context= {
                username:"username"
            }
            messages.success(request, f'You are now logged in as {username}')
            return redirect('main_web:team')
            
        else:
            msg = messages.error(request, 'Invalid credentials')
            return redirect(request, 'main_users:login')
    else:
        return render(request, 'main_users/login.html')


    
# def profile_create(request):
#     return render(request, 'main_users/projects.html')