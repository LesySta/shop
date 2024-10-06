from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.parsers import JSONParser

from product.models import Product, Cart, Order, ProductsCarts
from product.serializers import ProductSerializer, CartSerializer, OrderSerializer


def product_list(request):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

def cart_list(request):
    if request.method == 'GET':
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return JsonResponse(serializer.data, safe=False)


def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return JsonResponse(serializer.data, safe=False)

def add_product(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        carts = Cart.objects.filter(user_id=data["user_id"], is_active=True)
        user = User.objects.get(id=data["user_id"])
        if len(carts) == 0:
            new_cart = Cart.objects.create(
                user=user,
            ).save()
        else:
            new_cart = carts[0]
        product = Product.objects.get(id=data["product_id"])
        ProductsCarts.objects.create(
            cart=new_cart,
            product=product,
        ).save()



