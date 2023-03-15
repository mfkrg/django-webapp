from django.urls import path
from . import views

urlpatterns = [
    path('', views.goods_catalog, name='goods_catalog'),
    path('cart/add/<int:good_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:cart_id>/', views.cart_remove, name='cart_remove'),
    path('cart/', views.cart, name='cart'),
]