from django.contrib import admin

# Register your models here.
from .models import modelo_Principal
from .models import categoria
from .models import Autor


admin.site.register(Autor)
admin.site.register(categoria)
admin.site.register(modelo_Principal)