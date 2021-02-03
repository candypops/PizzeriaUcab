from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *
from datetime import datetime

def index(request):
    latest_ingrediente = Ingrediente.objects.order_by('id')
    latest_tam = Tamano.objects.order_by('id')
    template = loader.get_template('cliente.html')
    context = {
        'lastest_ingrediente': latest_ingrediente,
        'lastest_tam': latest_tam,
    }
    cont = 0
    if request.method == 'POST':
        last_id = crearPedido(request)
        lista_ingredientes = (request.POST.getlist('ing.id'))
        for ing in lista_ingredientes:
            pedido = Pedido_Pizza()
            pedido.tamano_pizza = Tamano.objects.get(id=request.POST.get('tam_id'))
            pedido.pedido_fk = Pedido.objects.get(id=last_id)
            pedido.pizza_fk = Ingrediente.objects.get(id=ing)
            pedido.save()
            ingrediente = Ingrediente.objects.get(id=ing)
            cont += ingrediente.costo
        tam = Tamano.objects.get(id=request.POST.get('tam_id'))
        ped = Pedido.objects.get(id=last_id)
        ped.total = cont + tam.costo
        ped.save()

    return HttpResponse(template.render(context, request))

def factura(request):
    return render(request, 'factura.html', {})


def crearPedido(request):
    pedido = Pedido()
    pedido.nombre = request.POST.get('nombre')
    pedido.cantidad = 1
    pedido.total = 0.00
    pedido.fecha = datetime.now()
    pedido.save()
    last_id = Pedido.objects.last()
    return last_id.id


def createPedido(request):
 latest_tam = Tamano.objects.order_by('id')[:4]
 template = loader.get_template('polls/index.html')
 context = {
  'lastest_tam': latest_tam
 }
 if request.method == 'POST':
  pedido= Pedido_Pizza()
  pedido.tamano_pizza = Tamano.objects.get(id = request.POST.get('tam_id'))
  pedido.pedido_fk = Pedido.objects.get(id = 1)
  pedido.pizza_fk = Ingrediente.objects.get(id = 3)
  pedido.save()
  return render(request, 'polls/index.html')

 return HttpResponse(template.render(context, request))

def mostrarIngredientes(request):
    lastest_ingrediente = Ingrediente.objects.order_by('id')
    template = loader.get_template('polls/ingredientes.html')
    context = {
        'lastest_ingrediente': lastest_ingrediente
    }
    print(request.POST)
    lista_ingredientes = (request.POST.getlist('ing.id'))
    print(lista_ingredientes)

    return HttpResponse(template.render(context, request))