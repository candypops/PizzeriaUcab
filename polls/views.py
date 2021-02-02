from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *

def index(request):
 return render(request, 'cliente.html', {})

def factura(request):
    return render(request, 'factura.html', {})


def tamanos(request):
 latest_tam = Tamano.objects.order_by('id')[:4]
 template = loader.get_template('polls/index.html')
 context = {
  'lastest_tam': latest_tam
 }
 return HttpResponse(template.render(context, request))

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