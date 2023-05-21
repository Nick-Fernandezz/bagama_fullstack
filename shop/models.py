from datetime import datetime

from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class UserProfils(models.Model):

    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    phone = PhoneNumberField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время регистрации')

    class Meta():

        verbose_name = 'профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return str(self.user)
    

class Categories(models.Model):
    
    title = models.CharField(verbose_name='Заголовок', max_length=100)
    image = models.ImageField(verbose_name='Картинка', upload_to='categories/avatars/')

    class Meta():

        verbose_name = 'каригорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title
    
class Products(models.Model):

    title = models.CharField(max_length=100, verbose_name='Имя товара')
    description = models.TextField('Описание товара', max_length=1000)  
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', default=0.00)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='Категория товара')
    # images = models.ForeignKey(ProductsImages, on_delete=models.CASCADE)
    preview = models.ImageField('Превью товара', upload_to='product/previews/%Y/%Y-%m-%d-%H-%M-%S/')
    top_status = models.BooleanField('Промо товар', default=False)
    created_date = models.DateTimeField(auto_now=True, verbose_name='Время создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Время последнего обновления')
    class Meta():

        verbose_name = 'продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class ProductsImages(models.Model):

    product = models.ForeignKey(Products, verbose_name='Товар', on_delete=models.CASCADE,
                                related_name="images")
    image = models.ImageField('Изображение', upload_to='product/images/%Y/%Y-%m-%d-%H-%M-%S/')

    def __str__(self):
        return str(self.product)


class Basket(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Пользователь', editable=False)
    products = models.ManyToManyField(Products, verbose_name='Продукты', blank=True)
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.user)
