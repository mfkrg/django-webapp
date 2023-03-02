from django.shortcuts import render
from .models import Goods

def goods_catalog(request):
    goods = Goods.objects.all()
    return render(request, 'goods/goods_catalog.html', {'goods':goods})