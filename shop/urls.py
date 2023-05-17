from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexpage, name='indexpage'),
    path('login/', views.loginuser, name='loginuser'),
    path('singup/', views.singupuser, name='singupuser'),
    path('logout/', views.logoutuser, name='logoutuser')
]

