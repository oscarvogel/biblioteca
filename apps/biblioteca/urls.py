from django.conf.urls import url
from apps.biblioteca.views import LibroCreate, LibroListar, LibroUpdate

urlpatterns = [
    url(r'^listar$', LibroListar.as_view(), name='libro_listar'),
    url(r'^nuevo$', LibroCreate.as_view(), name='libro_crear'),
    url(r'^editar/(?P<pk>\d+)/$', LibroUpdate.as_view(), name='libro_editar'),
]
