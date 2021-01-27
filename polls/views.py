from django.shortcuts import render


from django.http import HttpResponse




def index(request):
 return HttpResponse("Hola UCAB, usted está en el indice de polls")
