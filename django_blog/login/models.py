from django.db import models

# Create your models here.



class login(models.Model):
   
    Nombre_Usuario = models.CharField(max_length= 15, blank= False, null= False)
    Contraseña  = models.CharField(max_length= 20, blank= False, null= False)
    Tipo_Usuario = models.CharField(max_length= 20, blank= False, null= False)

    def __integer__(self):
        return self.Nombre_Usuario