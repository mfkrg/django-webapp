from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('cart/', views.cart, name='cart'),
    path('catalog/', views.catalog, name='catalog'),
    path('about/', views.about, name='about'),
    path('auth/', views.register, name='auth'),
    # path('register/', views.register, name='register')
]