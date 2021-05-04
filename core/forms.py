from django.contrib.auth.forms import UserCreationForm

from core.models import Usuario,Cliente,Especialista

class ClienteSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.is_cliente = True
        usuario.is_active= False
        if commit:
            usuario.save()
        return usuario

class EspecialistaSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.is_especialista = True
        usuario.is_active= False
        if commit:
            usuario.save()
        return usuario