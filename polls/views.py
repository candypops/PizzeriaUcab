from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
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
        print('post')
        last_id = crearPedido(request)
        request.session['has_session'] = True
        request.session['pedido_id'] = last_id
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
        totaltodo = cont + tam.costo
        ped.total = totaltodo
        ped.save()
        request.session['total'] = totaltodo
        if 'ordenar' in request.POST:
            request.session.flush()
            print('ordenar')
            return HttpResponse(template.render(context, request))
        else:
            return HttpResponseRedirect('/new')

    return HttpResponse(template.render(context, request))

def factura(request):
    return render(request, 'factura.html', {})

def nombre(request):
    template = loader.get_template('nombre.html')
    context = { }
    if 'nombre' in request.POST:
        return HttpResponseRedirect('/cliente')
    else:
        print("No hay nombre")

    return HttpResponse(template.render(context, request))

    


def crearPedido(request):
    pedido = Pedido()
    pedido.nombre = request.POST.get('nombre')
    pedido.cantidad = 1
    pedido.total = 0.00
    pedido.fecha = datetime.now()
    pedido.save()
    last_id = Pedido.objects.last()
    return last_id.id

def newPizza(request):
    last_id = request.session.get('pedido_id')
    total = request.session.get('total')
    print(total)
    latest_ingrediente = Ingrediente.objects.order_by('id')
    latest_tam = Tamano.objects.order_by('id')
    template = loader.get_template('more.html')
    context = {
        'lastest_ingrediente': latest_ingrediente,
        'lastest_tam': latest_tam,
    }
    if request.method == 'POST':
        lista_ingredientes = (request.POST.getlist('ing.id'))
        cont = 0
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
        subtotal = cont + tam.costo + total
        ped.total = subtotal
        ped.save()
        request.session['total'] = subtotal
        if 'ordenar' in request.POST:
            request.session.flush()
            print('ordenar')
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/new')

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