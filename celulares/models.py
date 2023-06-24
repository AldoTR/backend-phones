from django.db import models
from django.conf import settings

# Create your models here.

class Celular(models.Model):
     version = models.TextField(default='', blank = False)
     descripcion = models.TextField(default='', blank = False)
     marca = models.TextField(default='', blank = False)
     precio = models.DecimalField(default=0, max_digits=5, decimal_places=2, blank = False)
     tamano = models.TextField(default = 'xy pulgadas', blank = False)
     sistema = models.TextField(default = 'SO', blank = False)
     fecha = models.TextField(default = 'Año', blank = False)
     color = models.TextField(default = 'Color', blank = False)
     cpu = models.TextField(default = '- GB', blank = False)
     memoria = models.TextField(default = '- GB', blank = False)
     posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
     
class Vote(models.Model):
     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
     celular = models.ForeignKey('celulares.Celular', related_name='votes', on_delete=models.CASCADE)
