from django.contrib import admin

# Register your models here.

# вывод информации о клиенте
from django.contrib import admin
from .models import Client
from .models import Product
from .models import Order

"""Добавление модели Client в административную панель Django с определенными полями"""


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'address', 'reg_data')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'quantity', 'added_date')


class ProductInline(admin.TabularInline):
    model = Order.products.through
    extra = 1  # дополнительная форма для добавления продукта к заказу


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'total_amount', 'order_date')
    inlines = [ProductInline]
