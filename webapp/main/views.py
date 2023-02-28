from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("<h4>Проверка работы</h4>")

def cart(request):
    return HttpResponse("<h4>Проверка корзины</h4>")

def catalog(request):
    return HttpResponse("<h4>Проверка каталога</h4>")