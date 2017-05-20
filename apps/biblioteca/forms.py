from django import forms
from apps.biblioteca.models import Libro


class LibroForm(forms.ModelForm):
    
    class Meta:
        model = Libro
        fields = [
            'nombre',
            'isbn',
        ]

class LibroSearchForm(forms.Form):
    nombre = forms.CharField(required=False, label='Filtrar')