from django.db import IntegrityError
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login , logout , authenticate

# Create your views here.


    
def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todo/signup.html' , {'form': UserCreationForm() })
    elif request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todo/signup.html' , {'form': UserCreationForm(), 'error' : 'Username already taken please select another username' })
        else:
            return render(request, 'todo/signup.html' , {'form': UserCreationForm() , 'error' : 'Password didn`t match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todo/login.html' , {'form': AuthenticationForm() })
    elif request.method == 'POST':
        user = authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request, 'todo/login.html' , {'form': AuthenticationForm()  , 'error' : 'Username and password didn`t match'})
        else:
            login(request, user)
            return redirect('currenttodos')

def currenttodos(request):
    return render(request, 'todo/currenttodos.html')

def homepage(request):
    return render(request, 'todo/home.html')

def logoutuser(req):
    if req.method == 'POST':
        logout(req)
        return redirect('homepage')