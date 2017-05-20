from django.contrib import admin

# Register your models here.
from apps.biblioteca.models import Autor, Libro

class AutorAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)

class LibroAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)
    filter_horizontal = ('autor',)
    
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
