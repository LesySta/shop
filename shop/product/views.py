from django.http import JsonResponse
from django.shortcuts import render

from product.models import Product, Cart, Order
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

