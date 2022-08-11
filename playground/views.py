from itertools import product
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from store.models import Product, Customer, Collection, Order, OrderItem

def say_hello(request):
    #queryset = Customer.objects.filter(email__icontains='.com')
    #queryset = Collection.objects.filter(featured_product__isnull=True)
    #queryset = Product.objects.filter(inventory__lt=10) 
    #queryset = Order.objects.filter(customer__id=1)
    #queryset = OrderItem.objects.filter(product__collection__id=3)
    #queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id')).distinct().order_by('title')
    #queryset = Product.objects.prefetch_related('promotions')
    #queryset = Order.objects.filter('id__in=')
    queryset = Order.objects.select_related('customer').prefetch_related('orderitem_set__product')[:5]
    return render(request, 'hello.html', {'name': 'Mosh', 'orders': list(queryset)})
