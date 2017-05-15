from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from apps.prestamos.models import Prestamo
from apps.prestamos.forms import ListarPrestamosForm
from django.shortcuts import render

    
def PrestamoList(request):
    prestamos = None
    if request.method == 'POST':
        form = ListarPrestamosForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            prestamos = Prestamo.objects.filter(fechaPrestamo__range=(data['desde_fecha'],data['hasta_fecha']))
    else:
        form = ListarPrestamosForm()
        
    return render(request, 'prestamos/prestamos_list.html', {'form': form,'prestamos':prestamos})