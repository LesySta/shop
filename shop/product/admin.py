from django.contrib import admin
from django.contrib import admin
from .models import Product, Cart, Order, ProductsCarts

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'count', 'is_active', 'created_at')
    search_fields = ('name', 'description')
    list_filter = ('is_active', 'created_at')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_active', 'created_at')
    search_fields = ('user__username',)
    list_filter = ('is_active', 'created_at')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'created_at')
    search_fields = ('cart__user__username',)
    list_filter = ('created_at',)

@admin.register(ProductsCarts)
class ProductsCartsAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product')
    search_fields = ('cart__user__username', 'product__name')
    list_filter = ('cart', 'product')

# Register your models here.
