from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 path('ing/', views.mostrarIngredientes, name='ingredientes'),
 path('factura/', views.factura, name='factura'),
 path('new/', views.newPizza, name='nueva'),
 path('promo/', views.promos, name='promos'),
]