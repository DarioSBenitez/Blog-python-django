
from django.contrib import admin
from django.urls import path
from .views import inicio
from .views import login
from .views import register
from django.contrib.auth import views as auth_views



urlpatterns =[
    path('admin/', admin.site.urls),

    path('inicio/', inicio, name = 'inicio'),
    path('login/',auth_views.LoginView.as_view(template_name="login.html"), name ='login'),
    path('register/', register, name = 'register'),
   
      

]
