from django.shortcuts import render, HttpResponseRedirect
from .models import Goods, Cart
from django.db import models
from django.contrib.auth.models import User

def goods_catalog(request):
    goods = Goods.objects.all()
    return render(request, 'goods/goods_catalog.html', {'goods':goods})

def cart(request):
    cart = Cart.objects.filter(user=request.user)
    total_sum = sum(carts.sum() for carts in cart)
    total_quantity = sum(carts.quantity for carts in cart)
    return render(request, 'goods/cart.html', {'carts':cart, 'cart':cart, 'total_sum':total_sum, 'total_quantity':total_quantity})

def add_to_cart(request, good_id):
    good = Goods.objects.get(id=good_id)
    carts = Cart.objects.filter(user=request.user, good=good)

    if not carts.exists():
        Cart.objects.create(user=request.user, good=good, quantity=1)
    else:
        cart = carts.first()
        cart.quantity += 1
        cart.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
