from django import forms
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class ListarPrestamosForm(forms.Form):
    desde_fecha = forms.DateField(label='Desde Fecha', widget=DateInput())
    hasta_fecha = forms.DateField(label='Hasta Fecha', widget=DateInput())
    
