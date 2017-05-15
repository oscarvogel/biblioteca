from django.conf.urls import url

from apps.prestamos.views import PrestamoList

urlpatterns = [
    url(r'^listar$', PrestamoList, name='prestamo_listar'),
]
