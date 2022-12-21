from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import register
from .forms import RegistroUsuarioForm

# Create your views here.
# def register(request):
   
#     contexto_name ={

#     }
#     return render(request, "usuario/register.html",contexto_name )

class Register(CreateView):
	model         = register
	form_class    = RegistroUsuarioForm
	template_name = 'usuario/register.html'
	success_url   = reverse_lazy('inicio')
