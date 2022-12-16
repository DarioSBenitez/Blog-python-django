from django.shortcuts import render

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


def register(request):
    template_name= "register.html"
    contexto={
    }
    return render(request, template_name, contexto)

<<<<<<< HEAD

def quienes_somos(request):
    template_name= "quienes_somos.html"
    contexto={
    }
    return render(request, template_name, contexto)
=======
>>>>>>> f76ccd9637e34e328520920dbd2d8851e092f480
