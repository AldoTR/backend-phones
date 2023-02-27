from django.db import models
from django.conf import settings

class Celular(models.Model)

     version = models.TextField(default='', blank = False)
     descripcion = models.TextField(default='', blank = False)
     marca = models.TextField(Default='', blank = False)
     precio = models.DecimalField(default=0, max_digits=5, decimal_places=2, blank = False)
     tamaño = models.TextField(default = 'xy pulgadas', blank = False)
     sistema = models.TextField(default = 'SO', blank = False)
     fecha = models.TextField(default = 'Año', blank = False)
     color = models.TextField(default = 'Color', blank = False)
     cpu = models.TextField(default = '- GB', blank = False)
     memoria = models.TextField(default = '- GB', blank = False)

