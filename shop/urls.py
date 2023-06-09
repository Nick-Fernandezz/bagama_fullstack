from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexpage, name='indexpage'),
    path('login/', views.loginuser, name='loginuser'),
    path('singup/', views.singupuser, name='singupuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('about/', views.aboutpage, name='aboutpage'),
    path('whywe/', views.whywepage, name='whywepage'),
    path('categories/', views.categoriespage, name='categoriespage'),
    path('category/<int:category__id>', views.productspage, name='productspage'),
    path('product/<int:product__id>', views.productpage, name='productpage'),
]

