from django.contrib import admin
from django.urls import path

from product.views import product_list, cart_list, order_list

urlpatterns = [
    path('', product_list),
    path('cart/', cart_list),
    path('order/', order_list),

]
