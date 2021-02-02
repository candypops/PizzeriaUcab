from django.urls import path
from . import views

urlpatterns = [
 path('', views.createPedido, name='index'),
 path('tam/', views.createPedido, name='tamanos'),
 path('ing/', views.mostrarIngredientes, name='ingredientes'),
 path(r'^factura/$', views.factura, name='factura')
]