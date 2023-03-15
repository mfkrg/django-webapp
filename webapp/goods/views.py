from django.shortcuts import render, HttpResponseRedirect
from .models import Goods, Cart
from django.db import models
from django.contrib.auth.models import User

def goods_catalog(request):
    goods = Goods.objects.all()
    return render(request, 'goods/goods_catalog.html', {'goods':goods})

def cart(request):
    cart = Cart.objects.filter(user=request.user)
    return render(request, 'goods/cart.html', {'carts':cart})

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

def remove_from_cart(request, good_id):
    pass

def cart_remove(request, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

