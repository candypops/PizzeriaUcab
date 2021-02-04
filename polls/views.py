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

        fact = Factura()
        fact.tamano = request.POST.get('tam_id')
        fact.save()

        for i in lista_ingredientes:
            factped = fact_ped()
            factped.fk_pedido = Pedido.objects.get(id=last_id)
            factped.fk_fac = Factura.objects.get(id=Factura.objects.last().id)
            factped.ing = i
            factped.save()

        tam = Tamano.objects.get(id=request.POST.get('tam_id'))
        ped = Pedido.objects.get(id=last_id)
        totaltodo = cont + tam.costo
        ped.total = totaltodo
        ped.save()
        request.session['total'] = totaltodo
        if 'ordenar' in request.POST:
            return HttpResponseRedirect('/promo')
        else:
            return HttpResponseRedirect('/new')

    return HttpResponse(template.render(context, request))

def factura(request):
    last_id = request.session.get('pedido_id')
    total = request.session.get('total')
    promoname = request.session.get('promo')
    pedido = Pedido.objects.get(id=last_id)
    latest_ingrediente = Ingrediente.objects.order_by('id')
    latest_tam = Tamano.objects.order_by('id')
    ped_fact = fact_ped.objects.filter(fk_pedido_id=last_id).order_by('fk_fac').distinct()
    pedidos_factura = fact_ped.objects.all()
    facturas = Factura.objects.all()
    facts = []
    for i in ped_fact.values('fk_fac'):
        facts.append(i.get('fk_fac'))

    template = loader.get_template('factura.html')
    context = {
        'lastest_ingrediente': latest_ingrediente,
        'lastest_tam': latest_tam,
        'total': total,
        'nombre': pedido.nombre,
        'cantidad': pedido.cantidad,
        'facturas': facts,
        'pedidos_factura': pedidos_factura,
        'factura_original': facturas,
        'promo': promoname
    }

    if request.method == 'POST':
        request.session.flush()
        print('post')
        return HttpResponseRedirect('/cliente')


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
    pedido = Pedido.objects.get(id=last_id)
    latest_ingrediente = Ingrediente.objects.order_by('id')
    latest_tam = Tamano.objects.order_by('id')
    template = loader.get_template('more.html')
    context = {
        'lastest_ingrediente': latest_ingrediente,
        'lastest_tam': latest_tam,
        'nombre': pedido.nombre,
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

        fact = Factura()
        fact.tamano = request.POST.get('tam_id')
        fact.save()

        for i in lista_ingredientes:
            factped = fact_ped()
            factped.fk_pedido = Pedido.objects.get(id=last_id)
            factped.fk_fac = Factura.objects.get(id=Factura.objects.last().id)
            factped.ing = i
            factped.save()

        tam = Tamano.objects.get(id=request.POST.get('tam_id'))
        ped = Pedido.objects.get(id=last_id)
        subtotal = cont + tam.costo + total
        ped.total = subtotal
        ped.cantidad += 1
        ped.save()
        request.session['total'] = subtotal
        if 'ordenar' in request.POST:
            return HttpResponseRedirect('/promo')
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
def createPedido(request):
    latest_tam = Tamano.objects.order_by('id')
    template = loader.get_template('cliente.html')
    lastest_ingrediente = Ingrediente.objects.order_by('id')
    context = {
        'lastest_tam': latest_tam,
        'lastest_ingrediente': lastest_ingrediente
    }

    if request.method == 'POST':
        pedido= Pedido_Pizza()
        pedido.tamano_pizza = request.POST.get_context_data('tam_id')
        pedido.pedido_fk = Pedido.objects.get(id = 1)
        pedido.pizza_fk = Ingrediente.objects.get(id = 3)
        pedido.save()

        return render(request, template, context)

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

def ventas_view(request):
    ventas = Pedido.objects.order_by('id')
    ventas_tamano = Tamano.objects.order_by('id')
    template = loader.get_template('admin.html')
    context = {
        'ventas':ventas,
        'ventas_tamano':ventas_tamano
    }
    return HttpResponse(template.render(context, request))

def promos(request):
    last_id = request.session.get('pedido_id')
    pedido = Pedido.objects.get(id=last_id)
    total = request.session.get('total')
    allpromos = Promo.objects.all()

    latest_promos = Promo.objects.order_by('id')
    template = loader.get_template('promos.html')
    context = {
        'promos': latest_promos,
        'nombre': pedido.nombre,
    }
    if request.method == 'POST':
        pedido.pedido_promo = Promo.objects.get(id=request.POST.get('promo.id'))
        promoid = request.POST.get('promo.id')
        promoname = Promo.objects.filter(id=promoid)
        for k in promoname.values('codigo'):
            pn = k.get('codigo')
        for i in promoname.values('descuento'):
            descuento = i.get('descuento')
        if descuento == 0.00:
            subtotal = total
        elif descuento > 1:
            subtotal = total - descuento
        else:
            porcentajeoff = float(total * descuento)
            print(porcentajeoff)
            subtotal = total - porcentajeoff
        pedido.total = subtotal
        pedido.save()
        request.session['promo'] = pn
        request.session['total'] = subtotal
        return HttpResponseRedirect('/factura')

    return HttpResponse(template.render(context, request))