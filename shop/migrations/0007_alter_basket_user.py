# Generated by Django 4.2 on 2023-05-21 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0006_alter_productsimages_options_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='user',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
