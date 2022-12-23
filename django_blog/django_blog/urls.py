
from django.contrib import admin
from django.urls import path, include
from django_blog.views import inicio
from django_blog.views import post,mision,qsomos, contacto,descarga


from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', inicio, name='inicio'),
    path('login/',auth_views.LoginView.as_view(template_name="login.html"), name ='login'),
    path('logout/',auth_views.LogoutView.as_view(),name ='logout'),
    path('post/', post, name='post'),
    path('mision/', mision, name='mision'),
    path('Quienes_Somos/', qsomos, name='qsomos'),
    path('Contacto/', contacto, name='contacto'),
    path('descarga/', descarga, name='descarga'),
    
    
    
    path('register/', include ('register.urls'))
    # path('noticia/', include('noticia.urls')),
    # path('comentario/', include('comentario.urls')),
]
