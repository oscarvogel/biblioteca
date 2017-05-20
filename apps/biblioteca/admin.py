from django.contrib import admin

# Register your models here.
from apps.biblioteca.models import Autor, Libro, TipoMaterial, Categorias, Ubicacion

class AutorAdmin(admin.ModelAdmin):
    search_fields = ('nombre',)

class LibroAdmin(admin.ModelAdmin):
    list_filter = ('categoria__detalle',)
    search_fields = ('nombre',)
    filter_horizontal = ('autor',)
    raw_id_fields = ('tipomaterial','categoria','ubicacion')

class TipoMaterialAdmin(admin.ModelAdmin):
    search_fields = ('detalle',)

class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ('detalle',)

class UbicacionAdmin(admin.ModelAdmin):
    search_fields = ('detalle',)

admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(TipoMaterial, TipoMaterialAdmin)
admin.site.register(Categorias, CategoriaAdmin)
admin.site.register(Ubicacion, UbicacionAdmin)