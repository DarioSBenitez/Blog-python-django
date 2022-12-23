from django.shortcuts import render
from django.contrib.auth.forms  import UserCreationForm

def inicio(request):
    template_name= "index.html"
    contexto={
    }
    return render(request, template_name, contexto)


def descarga(request):
    template_name= "descarga.html"
    contexto={
    }
    return render(request, template_name, contexto)

   

   


def mision(request):
    template_name= "mision.html"
    contexto={
    }
    return render(request, template_name, contexto)

def post(request):
    template_name= "post.html"
    contexto = {

    }
    return render(request, template_name,contexto)


def qsomos(request):
    template_name= "qsomos.html"
    contexto = {

    }
    return render(request, template_name,contexto)


def contacto(request):
    template_name= "qsomos.html"
    contexto = {

    }
    return render(request, template_name,contexto)