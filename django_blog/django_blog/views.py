from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):

    nombre = "juan"

    doc_externo = open('C:/Users/Dario/Desktop/PROYECTO_FINAL/Blog-python-django/django_blog/templates/index.html')

    objetotipotemplate = Template(doc_externo.read())

    doc_externo.close()

    ctx = Context({"nombre_persona":nombre})

    documento = objetotipotemplate.render(ctx)

    return HttpResponse(documento)
