from django import forms
from django.contrib.admin.widgets import AdminDateWidget 


class ListarPrestamosForm(forms.Form):
    desde_fecha = forms.DateField(label='Desde Fecha',widget=forms.TextInput(attrs={'class':'datepicker'}))
    hasta_fecha = forms.DateField(label='Hasta Fecha')