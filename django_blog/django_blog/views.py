from django.shortcuts import render

def inicio(request):
    template_name= "index.html"
    contexto={
    }
    return render(request, template_name, contexto)

def login1(request):
    template_name= "login1.html"
    contexto={
    }
    return render(request, template_name, contexto)

def register(request):
    template_name= "register.html"
    contexto={
    }
    return render(request, template_name, contexto)
