# Generated by Django 4.2 on 2023-05-17 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_categories_options_userprofils_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofils',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
