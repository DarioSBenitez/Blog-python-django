
from django.contrib import admin
from django.urls import path
from .views import inicio
from .views import login
from .views import register
<<<<<<< HEAD
from django.contrib.auth import views as auth_views
=======
>>>>>>> f76ccd9637e34e328520920dbd2d8851e092f480



urlpatterns =[
    path('admin/', admin.site.urls),
<<<<<<< HEAD

    path('inicio/', inicio, name = 'inicio'),
    path('login/',auth_views.LoginView.as_view(template_name="login.html"), name ='login'),
    path('register/', register, name = 'register'),
   
      

=======
    path('inicio/', inicio),
    path('login/', login),
    path('register/', register),
>>>>>>> f76ccd9637e34e328520920dbd2d8851e092f480
]
