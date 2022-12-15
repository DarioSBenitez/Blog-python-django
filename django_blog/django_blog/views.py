

from django.shortcuts import render

def inicio(request):
    template_name= "index.html"
    contexto={

    }
    return render(request, template_name, contexto)
   

    


def login(request):
     
    contexto={

    }
    return render(request, "login.html", {})

from django.shortcuts import render
def noticia(request):
        contexto={}
        return render(request, "noticia.html", contexto)