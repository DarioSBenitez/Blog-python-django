from django.db import transaction
from django.contrib.auth.forms import UserCreationForm
from .models import register



class RegistroUsuarioForm(UserCreationForm):

    class Meta:
        model  = register
        fields = ['first_name','last_name','username','password1','password2','email']

    @transaction.atomic
    def save(self):
        user              = super().save(commit=False)
        user.is_superuser = False
        user.is_staff     = False
        user.save()
        return user

    