# from django.db import models

# # Create your models here.
# class modelo(models.model):
#     id = models.AutoField(primary_key=True)
#     estado = models.BooleanField('Estado', default= True)
#     fecha_creacion = models.DateField('Fecha de creacion',auto_now= False, auto_now_add= True)
#     fecha_Modificacion = models.DateField('Fecha de Modificacion',auto_now= True, auto_now_add= False)
#     fecha_eliminacion = models.DateField('Fecha de creacion',auto_now= False, auto_now_add= True)

# class Meta:
#     abstract : True

# class categoria(modelo):
#     nombre = models.CharField('Nombre de categoria',max_length=100, unique=True)
#     imagen = models.ImageField('imagen', upload_to= 'categoria/')

# class Meta:
#     verbose_name ='Categoria'
#     verbose_name_plural = 'Categorias'

#     def __str__(self):
#         return self.nombre

# class Autor(modelo):
#      nombre = models.CharField('Nombre',max_length=100)
#      Apellido = models.CharField('Apellido',max_length=100)




