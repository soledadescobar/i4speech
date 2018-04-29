# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Textos, Autores, Cr, Fh, Gu, Mu, Sp, Ocasiones, Indices, Ejes
from django.views import generic
from django.forms import ModelForm
from .forms import NuevoTextoForm
from .forms import NuevoAutorForm
from .forms import AnalizaTextoForm
from django.core.files.storage import default_storage

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.fields.files import FieldFile
from django.views.generic import FormView
from django.views.generic.base import TemplateView
from django.contrib import messages
from django.db.models import Avg
from django import forms
from .chartdata import ChartData
import django_filters
from .cargacsv import CargaCSV
from django.core.files.storage import FileSystemStorage
from io import TextIOWrapper
from .analizador import Analizador
from django.utils import encoding

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_textos = Textos.objects.all().count()
    num_autores = Autores.objects.all().count()
    #   c = CargaCSV.cargacsv()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'i4speech_app/index.html',
        context={'num_textos': num_textos, 'num_autores': num_autores,},
    )

class TextosListView(generic.ListView):
    model = Textos


class AutoresListView(generic.ListView):
    model = Autores
    num_textos = Textos.objects.all().count()
    prom_cr = Cr.objects.values('idtexto__idautor__nombre').annotate(prom_cr=Avg('resultado')).order_by('idtexto__idautor__nombre')

class TextoDetailView(generic.DetailView):
    model = Textos


def TextoNuevoView(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = NuevoTextoForm(request.POST or None)
        # Check if the form is valid:
        if form.is_valid():
            form.save()
            form = NuevoTextoForm()
    # If this is a GET (or any other method) create the default form.

    else:
        form = NuevoTextoForm()
    return render(request, 'i4speech_app/nuevo_texto.html', {'form': form})


def AutorNuevoView(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = NuevoAutorForm(request.POST)
        # Check if the form is valid:
        if form.is_valid():
            form.save()
            form = NuevoAutorForm()
    # If this is a GET (or any other method) create the default form.
    else:
        form = NuevoAutorForm()
    return render(request, 'i4speech_app/nuevo_autor.html', {'form': form})


def ResultadosView (request):
    return render(request, 'i4speech_app/resultados.html')


def ResultadoasoView (request):
    return render(request, 'i4speech_app/resultadoaso.html')


def DashboardView(request, chartID='chart_ID', chart_type='column', chart_height=500):
    filterindice=  IndiceFilter(request.GET, queryset=Indices.objects.values('indice'))
    filterautor = AutorFilter(request.GET, queryset=Autores)
    filterocasion = OcasionFilter(request.GET, queryset=Ocasiones)
    filtereje = EjeFilter(request.GET, queryset=Ejes)
    dataraw = ChartData.chart_data(filterindice, filterautor, filterocasion, filtereje)
    drilldown = ChartData.drilldowns (dataraw, filterindice, filterocasion, filtereje)

    chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    title = {"text": 'Promedio por Autor e Indice'.__str__()}
    xAxis = {"type": 'category', 'labels': {
            'rotation': -45,
            'style': {
                'fontSize': '9px',
                'fontFamily': 'Verdana, sans-serif'
            },
            "scrollbar":  {'enabled': 'true'},
    'min': 0,
            'max': 3
        }}
    yAxis = {"title": {"text": 'Valor'}}
    series = {'name':[],'data':[]}
    for  index, autor in enumerate(dataraw['autor']):
        if 'indice' not in filterindice.data:
            data = {'name': dataraw['autor'][index],'drilldown': dataraw['autor'][index], 'y':dataraw['fh'][index], 'color': dataraw['color'][index]}
            indice = 'FH'
        else:
            if 'cr' in dataraw:
                data = {'name': dataraw['autor'][index],'drilldown': dataraw['autor'][index], 'y':dataraw['cr'][index], 'color': dataraw['color'][index]}
                indice = 'CR'
            if 'gu' in dataraw:
                data = {'name': dataraw['autor'][index],'drilldown': dataraw['autor'][index], 'y':dataraw['gu'][index], 'color': dataraw['color'][index]}
                indice = 'GU'
            if 'fh' in dataraw:
                data = {'name': dataraw['autor'][index],'drilldown': dataraw['autor'][index], 'y':dataraw['fh'][index], 'color': dataraw['color'][index]}
                indice = 'FH'
            if 'mu' in dataraw:
                data = {'name': dataraw['autor'][index],'drilldown': dataraw['autor'][index], 'y':dataraw['mu'][index], 'color': dataraw['color'][index]}
                indice = 'MU'
            if 'sp' in dataraw:
                data = {'name': dataraw['autor'][index],'drilldown': dataraw['autor'][index], 'y':dataraw['sp'][index], 'color': dataraw['color'][index]}
                indice = 'SP'
        series['data'].append(data)
    series['name']=indice

    return render(request, 'i4speech_app/dashboard.html', {'chartID': chartID, 'chart': chart,
                                                    'series': [series], 'title': title,
                                                    'xAxis': xAxis, 'yAxis': yAxis, 'filterindice':filterindice,
                                                    'filterautor': filterautor, 'filtereje': filtereje, 'filterocasion': filterocasion,
                                                    'drilldown': drilldown})


class IndiceFilter(django_filters.FilterSet):
    indice = django_filters.ModelMultipleChoiceFilter(queryset=Indices.objects.all(), label="Indice",
                                                      widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    class Meta:
        model = Indices
        fields = ['indice']


class AutorFilter(django_filters.FilterSet):
    nombre = django_filters.ModelMultipleChoiceFilter(queryset=Autores.objects.all(), label='Autor',
                                                      widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    class Meta:
        model = Autores
        fields = ['nombre']


class OcasionFilter(django_filters.FilterSet):
    ocasion = django_filters.ModelMultipleChoiceFilter(queryset=Ocasiones.objects.all(), label ='Ocasión',
                                                       widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    class Meta:
        model = Ocasiones
        fields = ['ocasion']


class EjeFilter(django_filters.FilterSet):
    eje = django_filters.ModelMultipleChoiceFilter(queryset=Ejes.objects.all(), label = 'Eje Temático',
                                                   widget=forms.SelectMultiple(attrs={'class': 'form-control'}))

    class Meta:
        model = Ejes
        fields = ['eje']


def CargaCSVView(request):
    if request.method == 'POST' and request.FILES['myfile']:
        #myfile = request.FILES['myfile']
        myfile = TextIOWrapper(request.FILES['myfile'].file, encoding=request.encoding)
        res = CargaCSV.cargacsv(myfile)
        return render(request, 'i4speech_app/cargacsv.html')
    return render(request, 'i4speech_app/cargacsv.html')


def AnalizaTextoView(request):
    # If this is a POST request then process the Form data
    resultado = []
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
            form = AnalizaTextoForm(request.POST)
            if form.is_valid():
                texto=encoding.smart_text(form.data.get('textoparaanalizar'))
                resultado = Analizador.analizatexto(texto)
    # If this is a GET (or any other method) create the default form.
    else:
        form = AnalizaTextoForm(request.GET)
    return render(request, 'i4speech_app/analizatexto.html', {'form': form, 'resultado': resultado})