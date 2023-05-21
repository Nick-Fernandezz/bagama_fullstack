from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm
from django.db import IntegrityError
from django.contrib.auth.models import User
from .models import UserProfils, Categories, Products, ProductsImages, Basket



# Create your views here.

def indexpage(request):
    top_products = Products.objects.all().filter(top_status=True)
    print(top_products)
    return render(request, 'shop/index.html', {'top_products': top_products})


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
                basket = Basket.objects.create(user=user)
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


def productspage(request, category__id):
    # category_name = Categories.objects.get(id=category__id).title
    category_name = get_object_or_404(Categories, id = category__id).title
    # products = Products.objects.all(category=category__id)
    products = get_list_or_404(Products, category = category__id)

    data = {
        'category_name': category_name,
        'products': products
    }
    return render(request, 'shop/products.html', context=data)


def productpage(request, product__id):
    print(product__id)
    product = get_object_or_404(Products, id=product__id)
    product_photos = ProductsImages.objects.filter(product_id=product.id)
    print(product_photos)
    # product_photos = get_list_or_404(ProductsImages, product_id=product.id)

    return render(request, 'shop/productpage.html', context={'product': product, 'photos': product_photos})


def page_not_found_view(request, exception):
    return render(request, 'shop/404page.html')
