from django.shortcuts import render

def goods_catalog(request):
    return render(request, 'goods/goods_catalog.html')