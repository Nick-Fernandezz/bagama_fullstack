from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def indexpage(request):
    return render(request, 'shop/index.html')


def loginuser(request):

    if request.method == 'GET':

        return render(request, 'shop/loginuser.html', {'form': AuthenticationForm()}) # если метод запроса ГЕТ, то возвращаем страницу входа с созданной формой
