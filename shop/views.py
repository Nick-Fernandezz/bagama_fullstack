from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm

# Create your views here.

def indexpage(request):
    return render(request, 'shop/index.html')


def loginuser(request):

    if request.method.GET:
        return ''
