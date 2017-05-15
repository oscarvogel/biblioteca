from django.db import models
from apps.biblioteca.models import Libro

SEXO = (('M','Masculino'),('F','Femenino'))

# Create your models here.
class Estudiante(models.Model):
    nombre 	   = models.CharField(max_length = 80)
    celular    = models.CharField(max_length = 30)
    dni 	   = models.CharField(max_length = 8)
    sexo	   = models.CharField(max_length = 1, choices=SEXO)
    direccion  = models.CharField(max_length = 80)
    fecIngreso = models.DateField(blank=True)
    reservas   = models.BooleanField(default = False, help_text='Puede realizar reservas')
    prestamos  = models.BooleanField(default = False, help_text='Puede realizar prestamos')

    def __str__(self):
        return "%s" % (self.nombre)
    
    class Meta:
        verbose_name_plural = 'Estudiantes'
        
class Reserva(models.Model):
    fechaReserva = models.DateField()

    libro  = models.ForeignKey(Libro)
    estudiante = models.ForeignKey(Estudiante)

    def __str__(self):
        return self.estudiante.nombre
    
    class Meta:
        verbose_name_plural = 'Reservas'
        
class Prestamo(models.Model):
    fechaPrestamo   = models.DateField(verbose_name='Fecha prestamo')
    fechaDevolucion = models.DateField(blank = True, null = True)

    libro 	   = models.ForeignKey(Libro)
    estudiante = models.ForeignKey(Estudiante)

    def __str__(self):
        return self.estudiante.nombre                
    
    class Meta:
        verbose_name_plural = 'Prestamos'