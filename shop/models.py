from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class UserProfils(models.Model):

    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    phone = PhoneNumberField(blank=True)

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
    
