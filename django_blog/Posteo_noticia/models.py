from django.db import models
from ckeditor.fields import RichTextField

class modelo_Principal (models.model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField('Estado', default= True)
    fecha_creacion = models.DateField('Fecha de creacion',auto_now= False, auto_now_add= True)
    fecha_Modificacion = models.DateField('Fecha de Modificacion',auto_now= True, auto_now_add= False)
    fecha_eliminacion = models.DateField('Fecha de creacion',auto_now= False, auto_now_add= True)

class Meta:
     abstract : True

class categoria(modelo_Principal):
    nombre = models.CharField('Nombre de categoria',max_length=100, unique=True)
    imagen = models.ImageField('imagen', upload_to= 'categoria/')

class Meta:
     verbose_name ='Categoria'
     verbose_name_plural = 'Categorias'

def __str__(self):
         return self.nombre

class Autor(modelo_Principal):    
    nombre = models.CharField('Nombre',max_length=100)
    apellidos = models.CharField('Apellido',max_length=120)
    email=models.EmailField('Correo Electronico', max_length=200)
    descripcion= models.TextField('Descripcion')
    
    class Meta:
        verbose_name='Autor'
        verbose_name_plural="Autores"

    def __str__ (self):
        return '{0}, {1}'.format (self. apellidos, self.nombre)

    class Post (modelo_Principal):
        titulo=models.CharField ('Titulo del Post',max_length=150, unique=True)
        slug=models.CharField('slug', max_length=150, unique=True)
        descripcion =models.TextField('Descripcion')
        autor=models.Foreignkey('Autor', on_delete=models.CASCADE)
        categoria=models.Foreignkey ('Categoria', on_delete=models.CASCADE)
        contenido=RichTextField()
        imagen=models.ImageField ('Imagen', upload_to= 'categoria/')
        fecha_publicación=models.DateField('Fecha de publicacion')

        
    class Meta:
        verbose_name='Post'
        verbose_name_plural="Posts"

    def __str__ (self):
        return self.titulo

    class Contacto (modelo_Principal):
        nombre=models.CharField('Nombre', max_lenght=100)
        apellidos=models.CharField('Apellidos', max_lenght=150)
        correo=models.CharField('Correo Electrónico', max_lenght=200)
        asunto=models.CharField('Asunto', max_lenght=100)
        mensaje=models.TextField('Mensaje')

        class Meta:
            verbose_name='Contacto'
            verbose_name_plural='Contactos'

        def __Str__(self):
            return self.asunto