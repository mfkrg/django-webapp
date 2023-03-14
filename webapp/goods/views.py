from django.shortcuts import render, HttpResponseRedirect
from .models import Goods, Cart
from django.contrib.auth.models import User

def goods_catalog(request):
    goods = Goods.objects.all()
    return render(request, 'goods/goods_catalog.html', {'goods':goods})

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