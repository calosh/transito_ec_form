# -*- encoding: utf-8 -*-
from django import forms
from autos.models import Tipovehiculo
from autos.models import Provincias, Combustibles

class TipoVehiculoForm(forms.Form):
    tipos = forms.ModelChoiceField(queryset=Tipovehiculo.objects.all(), label="", initial='', widget=forms.Select(), required=True)




class CombustiblesProvinciaForm(forms.Form):
    provincia = forms.ModelChoiceField(queryset=Provincias.objects.all(), label="", initial='', widget=forms.Select(), required=True)
    combustible = forms.ModelChoiceField(queryset=Combustibles.objects.all(), label="", initial='', widget=forms.Select(), required=True)
