from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('about/', views.about, name='about'),
    path('auth/', views.register, name='auth'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),

]