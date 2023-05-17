from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_title = 'Админ система Багама'
admin.site.site_header = 'Админ система Багама'

class ChangeUserProfild(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone')
    list_display_links = ('id', 'user', 'phone')
    search_fields = ('id', 'user', 'phone')


class ChangeCategories(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


admin.site.register(UserProfils, ChangeUserProfild)
admin.site.register(Categories, ChangeCategories)
