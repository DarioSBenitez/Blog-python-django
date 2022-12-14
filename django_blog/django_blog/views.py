<<<<<<< HEAD


from django.shortcuts import render

def inicio(request):
    template_name= "index.html"
    contexto={

    }
    return render(request, template_name, contexto)
   

    
=======
from django.shortcuts import render
def inicio (request):
    template_name= "index.html"
    contexto={

    }
    return render(request, template_name, contexto)
>>>>>>> 98e87059cf302a8e6eb9fa9ee68fe4ef6e4a73d8
