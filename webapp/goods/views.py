from django.shortcuts import render

def goods_catalog(request):
    return render(request, 'main/about.html')