from django.urls import path

from  .import views


app_name = 'register'

urlpatterns = [
     path('register/',views.Register.as_view(), name ='registro')
]
