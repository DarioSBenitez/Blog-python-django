
from django.contrib import admin
from django.urls import path, include
from django_blog.views import inicio


from django.contrib.auth import views as auth_views



urlpatterns =[
    path('admin/', admin.site.urls),

    path('inicio/', inicio, name='inicio'),
    path('login/',auth_views.LoginView.as_view(template_name="login.html"), name ='login'),
    path('logout/',auth_views.LogoutView.as_view(),name ='logout'),


    
    
    path('register/', include ('register.urls'))
   
      


]
