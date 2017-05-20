from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return '%s' % (self.nombre)
    
    class Meta:
        verbose_name_plural = 'Autores'

class TipoMaterial(models.Model):
    detalle = models.CharField(max_length=80)

    def __str__(self):
        return self.detalle

    class Meta:
        verbose_name_plural = 'Tipo de Materiales'

class Categorias(models.Model):
    detalle = models.CharField(max_length=80)

    def __str__(self):
        return self.detalle

    class Meta:
        verbose_name_plural = 'Categoria de libro'

class Ubicacion(models.Model):
    detalle = models.CharField(max_length=80)

    def __str__(self):
        return self.detalle

    class Meta:
        verbose_name_plural = 'Ubicacion de libro'

class Libro(models.Model):
    nombre = models.CharField(max_length=80)
    isbn = models.CharField(max_length=13, blank=True)
    precio = models.DecimalField(max_digits=14,decimal_places=4,blank=True,default=0)
    detalle = models.TextField(blank=True)
    autor = models.ManyToManyField(Autor, blank=True)
    imagen = models.ImageField(upload_to = 'libro', blank=True)
    stock = models.IntegerField(default=1)
    tipomaterial = models.ForeignKey(TipoMaterial,default=1,verbose_name='Tipo de material')
    categoria = models.ForeignKey(Categorias,default=1,verbose_name='Categoria')
    ubicacion = models.ForeignKey(Ubicacion,default=1,verbose_name='Ubicacion')

    def __str__(self):
        return '%s' % (self.nombre)
    
    class Meta:
        verbose_name_plural = 'Libros'