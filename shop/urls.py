from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexpage, name='indexpage'),
    path('login/', views.loginuser, name='loginuser'),
<<<<<<< HEAD
=======
    path('singup/', views.singupuser, name='singupuser')
>>>>>>> a0358f2 (process creating loging sys)
]

