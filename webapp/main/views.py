from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'main/index.html')

def cart(request):
    return HttpResponse("<h4>Проверка корзины</h4>")

def catalog(request):
    return HttpResponse("<h4>Проверка каталога</h4>")

def about(request):
    return HttpResponse("<h4>Проверка страницы о нас</h4>")