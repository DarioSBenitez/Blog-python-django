from django.shortcuts import render
from django.contrib.auth.forms  import UserCreationForm

def inicio(request):
    template_name= "index.html"
    contexto={
    }
    return render(request, template_name, contexto)


def login(request):
    template_name= "login.html"
    contexto={
    }
    return render(request, template_name, contexto)

   

   


def quienes_somos(request):
    template_name= "quienes_somos.html"
    contexto={
    }
    return render(request, template_name, contexto)

def post(request):
    template_name= "post.html"
    contexto = {

    }
    return render(request, template_name,contexto)