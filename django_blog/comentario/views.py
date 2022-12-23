from django.shortcuts import render
from .models import Comentarios
from .forms import  ComentarioForm
from django.views.generic import DeleteView
from register.models import register
from django.urls import reverse_lazy



def AddComentario(request):
	usuario= register(usuario=request.user)
	form = ComentarioForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ComentarioForm()
	
	
	context={
		'form': form,
		'usuario': usuario,
	}
	return render(request,'comentario/addcomentario.html', context)

class DeleteComentario(DeleteView):
	model 		  = Comentarios
	template_name = 'comentario/comentario_delete.html'
	success_url   = reverse_lazy('apps.noticia:listarNoticia2')

def Comentarioss(request):
	comentarios = Comentarios.objects.all()
	usuario = request.user.id

	context={
		'comentarios' : comentarios,
		'usuario': usuario,
	}
	return render(request,'comentario/listarcomentario.html', context)
