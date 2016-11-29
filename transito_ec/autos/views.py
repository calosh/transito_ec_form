# -*- encoding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.http import JsonResponse
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect

from autos.models import *
from autos.forms import *
import json

# Create your views here.

def index(request):
    
    diccionario = {'saludo': "Hola Mundo"}
    return render(request, 'index.html', diccionario, 
        context_instance=RequestContext(request))

def listado_vehiculos(request):
    
    # obtengo las provincias
    vehiculos = Vehiculos.objects.all()
    diccionario = {'vehiculos': vehiculos, 'mensaje': 'Mensaje de la pantalla'}
    return render(request, 'listado_vehiculos.html', diccionario, 
        context_instance=RequestContext(request))


def buscador_placas(request):
    abecedario = [
            ('-', '-'),
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
            ('E', 'E'),
            ('F', 'F'),
            ('G', 'G'),
            ('H', 'H'),
            ('I', 'I'),
            ('J', 'J'),
            ('K', 'K'),
            ('M', 'M'),
            ('N', 'N'),
            ('O', 'O'),
            ('P', 'P'),
            ('Q', 'Q'),
            ('R', 'R'),
            ('S', 'S'),
            ('T', 'T'),
            ('W', 'W'),
            ('X', 'X'),
            ('Y', 'Y'),
            ('Z', 'Z'),
            ]
    context = {'abecedario': abecedario}
    
    return render(request, 'buscador_placas.html', context)


@csrf_exempt
def funcion_ajax(request):
    """
    """
    # print request
    # print request.POST.getlist('valor')
    if request.is_ajax() == True:
        req = {}
        letra = request.POST.getlist('valor')[0]
        vehiculos = serializers.serialize('json', Vehiculos.objects.filter(placa__startswith = letra ))
        req['mensaje'] = 'Correcto .... cargando datos '
        req['vehiculos'] = vehiculos 
        return JsonResponse(req, safe=False)


def buscador_placas_dos(request):
    abecedario = [
            ('-', '-'),
            ('A', 'A'),
            ('B', 'B'),
            ('C', 'C'),
            ('D', 'D'),
            ('E', 'E'),
            ('F', 'F'),
            ('G', 'G'),
            ('H', 'H'),
            ('I', 'I'),
            ('J', 'J'),
            ('K', 'K'),
            ('M', 'M'),
            ('N', 'N'),
            ('O', 'O'),
            ('P', 'P'),
            ('Q', 'Q'),
            ('R', 'R'),
            ('S', 'S'),
            ('T', 'T'),
            ('W', 'W'),
            ('X', 'X'),
            ('Y', 'Y'),
            ('Z', 'Z'),
            ]
    context = {'abecedario': abecedario}
    
    return render(request, 'buscador_placas_dos.html', context)


@csrf_exempt
def funcion_ajax_dos(request):
    """
    """
    if request.is_ajax() == True:
        req = {}
        letra = request.POST.getlist('valor')[0]
        vehiculos = Vehiculos.objects.filter(placa__startswith=letra).all()
        vehiculos2 = json.dumps( [{'placa': o.placa, 'provincia': o.idprov.nombreprov} for o in vehiculos] )
        req['mensaje'] = 'Correcto .... cargando datos '
        req['vehiculos'] = vehiculos2 
        return JsonResponse(req, safe=False)


def listado_vehiculos_tipo(request):
    # if this is a POST request we need to process the form data
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TipoVehiculoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL (opcional)
            id_tipo_vehiculo = request.POST['tipos']
            print id_tipo_vehiculo
            tipo_vehiculo = Tipovehiculo.objects.get(pk=id_tipo_vehiculo)
            vehiculos = Vehiculos.objects.filter(idtipov=tipo_vehiculo)
    # if a GET (or any other method) we'll create a blank form
    else:
        vehiculos = Vehiculos.objects.all()
        form = TipoVehiculoForm()
        
    return render(request, 'listado_vehiculos_tipo.html', {'form': form, 'vehiculos': vehiculos})




def listado_combustibles_provincia(request):
    # if this is a POST request we need to process the form data
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CombustiblesProvinciaForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL (opcional)
            id_provincia = request.POST['provincia']
            id_combustible = request.POST['combustible']
            print id_provincia
            print id_combustible
            provincia = Provincias.objects.get(pk=id_provincia)
            combustible = Combustibles.objects.get(idcomb=id_combustible)
            vehiculos = Vehiculos.objects.filter(idcomb=combustible, idprov=provincia)
            #vehiculos = Vehiculos.objects.all()
    # if a GET (or any other method) we'll create a blank form
    else:
        vehiculos = Vehiculos.objects.all()
        provincia = Provincias.objects.all()
        combustible = Combustibles.objects.all()
        form = CombustiblesProvinciaForm()
        
    return render(request, 'listado_vehiculos_tipo2.html', {'form': form, 'vehiculos': vehiculos,'provincia': provincia,'combustible':combustible})


