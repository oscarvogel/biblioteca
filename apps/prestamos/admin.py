from django.contrib import admin

# Register your models here.

from apps.prestamos.models import Estudiante, Reserva, Prestamo

class EstudianteAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)
    list_filter = ('fecIngreso',)

class ReservaAdmin(admin.ModelAdmin):
    search_fields = ('estudiante__nombre',)
    list_filter = ('fechaReserva',)
    raw_id_fields = ('libro', 'estudiante',)

class PrestamoAdmin(admin.ModelAdmin):
    search_fields = ('estudiante__nombre','libro__nombre',)
    list_filter = ('fechaPrestamo','estudiante','libro',)
    raw_id_fields = ('libro', 'estudiante',)
    
admin.site.register(Estudiante, EstudianteAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(Prestamo, PrestamoAdmin)