from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from django.db import IntegrityError
from django.contrib.auth.models import User
from .models import UserProfils, Categories



# Create your views here.

def indexpage(request):
    return render(request, 'shop/index.html')


def loginuser(request):

    if request.method == 'GET':

        return render(request, "shop/loginuser.html", {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, "shop/loginuser.html", {'form': AuthenticationForm(), 'error': 'Логин или пароль введены неверно'})
        else:
            login(request, user)
            return redirect('indexpage')
    

def singupuser(request):
    if request.method == 'GET':
        return render(request, 'shop/singupuser.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password1'])
                user.save()
                login(request, user)
                user_profile = UserProfils.objects.create(user=user, phone=request.POST['phonenumber'])
                
                user_profile.save()
                return redirect('indexpage')
            except IntegrityError:
                return render(request, 'shop/singupuser.html', {'error': 'Пользователь с таким логином существует'})
        else:
            return render(request, 'shop/singupuser.html', {'error': 'Пароли не совпадают'})

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('indexpage')


def aboutpage(request):
    return render(request, 'shop/about.html')


def whywepage(request):
    return render(request, 'shop/whywe.html')


def categoriespage(request):

    categories = Categories.objects.all()

    return render(request, 'shop/categories.html', {'categories': categories})