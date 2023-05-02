from django.contrib import admin
from .models import User, Product, Category


# Configuring admin model view
class AdminUser(admin.ModelAdmin):
    list_display = ['email', 'name']

class AdminProduct(admin.ModelAdmin):
    list_display = ['title', 'price', 'descrption']


# Register your models here.

admin.site.register(User, AdminUser)
admin.site.register(Product, AdminProduct)
admin.site.register(Category)