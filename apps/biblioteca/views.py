from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
# Create your views here.

from apps.biblioteca.models import Libro
from apps.biblioteca.forms import LibroForm, LibroSearchForm

class LibroListar(ListView):
    model = Libro
    form_class = LibroSearchForm
    template_name = 'biblioteca/libro_list.html'
    paginate_by = 5
    form = None
    object_list = None
    
    def post(self, request, *args, **kwargs):
        self.show_results = False
        self.object_list = self.get_queryset()
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
            self.show_results = True
            self.object_list = Libro.objects.filter(nombre__icontains=form.cleaned_data['nombre'])
        else:
            self.object_list = Libro.objects.all()
        return  self.render_to_response(self.get_context_data(object_list=self.object_list, form=self.form))
    
    def get_context_data(self, **kwargs):
        context = super(LibroListar, self).get_context_data(**kwargs)
        if not self.form:
            self.form = LibroSearchForm()
        context.update({
            'form': self.form
        })
        return context
    
class LibroCreate(CreateView):
    model = Libro
    fields = ['nombre','isbn','autor']
    
class LibroUpdate(UpdateView):
    model = Libro
    fields = ['nombre','isbn','autor','categoria','tipomaterial','ubicacion']
    raw_id_fields = ('tipomaterial','categoria','ubicacion')
    filter_horizontal = ('autor',)
    success_url = reverse_lazy('biblioteca:libro_listar')