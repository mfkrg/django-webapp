from django.urls import path
from . import views

urlpatterns = [
    path('', views.goods_catalog, name='goods_catalog')
]