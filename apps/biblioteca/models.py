from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return '%s' % (self.nombre)
    
    class Meta:
        verbose_name_plural = 'Autores'
        
class Libro(models.Model):
    nombre = models.CharField(max_length=80)
    isbn = models.CharField(max_length=13)
    precio = models.DecimalField(max_digits=14,decimal_places=4,blank=True,default=0)
    detalle = models.TextField(blank=True)
    autor = models.ManyToManyField(Autor, blank=True)
    imagen = models.ImageField(upload_to = 'libro', blank=True)
    stock = models.IntegerField(default=1)
    
    def __str__(self):
        return '%s' % (self.nombre)
    
    class Meta:
        verbose_name_plural = 'Libros'