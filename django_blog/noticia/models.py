from django.db import models

# Create your models here.
class noticia(models.Model):
    #   administrador = models.ForeignKey('auth.user',one_delete=models.CASCADE)
      titulo = models.CharField(max_length=200)
      contenido = models.TextField()
      