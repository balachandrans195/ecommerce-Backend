from django.contrib import admin

from .models import Customer, Product, Rating, Category, Cart

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Rating)
admin.site.register(Category)
admin.site.register(Cart)