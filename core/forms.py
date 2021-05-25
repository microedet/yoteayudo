from datetime import datetime, date

from django.contrib.auth.forms import UserCreationForm
from django import forms
from sqlalchemy.sql.functions import now

from core.models import Usuario, Cliente, Especialista, Cita, Mensaje


class ClienteSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.is_cliente = True
        usuario.is_active = False
        if commit:
            usuario.save()
        return usuario


class EspecialistaSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Usuario

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.is_especialista = True
        usuario.is_active = False
        if commit:
            usuario.save()
        return usuario


# Formulario para updatecliente
class ClienteUpdateForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['foto', 'dni', 'nombre', 'apellido', 'direccion', 'fechaNacimiento']
        # fields = ['foto','dni','nombre','apellido','direccion']

        widgets = {
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'dni': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'DNI'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'NOMBRE'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'APELLIDO'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'DIRECCION'}),
            'fechaNacimiento': forms.DateInput(attrs={'class': 'form-control mt-3', 'placeholder': 'DD/MM/AAAA'})
        }


# Formulario para updateespecialista
class EspecialistaUpdateForm(forms.ModelForm):
    class Meta:
        model = Especialista
        fields = ['foto', 'dni', 'nombre', 'apellido', 'direccion', 'fechaNacimiento', 'biografia']

        widgets = {
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'dni': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'DNI'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'NOMBRE'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'APELLIDO'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'DIRECCION'}),
            'fechaNacimiento': forms.DateInput(attrs={'class': 'form-control mt-3', 'placeholder': 'DD/MM/AAAA'}),
            'biografia': forms.Textarea(attrs={'class': 'form-control mt-3', 'rows': '3', 'placeholder': 'BIOGRAFIA'})
        }


# Formulario para Deleteespecialista
class EspecialistaDeleteForm(forms.ModelForm):
    class Meta:
        model = Especialista
        fields = ['foto', 'dni', 'nombre', 'apellido']

        widgets = {
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'dni': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'DNI'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'NOMBRE'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'APELLIDO'})
        }


# formulario para crear la cita
class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        # fields = ['fecha','idCliente','idEspecialista','informe','realizada']
        fields = ['fecha', 'idCliente', 'idEspecialista']

        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control mt-3', 'placeholder': 'DD/MM/AAAA'}),
            'idCliente': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'idCliente'}),
            'idEspecialista': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'idEspecialista'}),
            # 'informe':forms.TextInput(attrs={'class':'form-control mt-3', 'placeholder':'informe'}),
            # 'realizada':forms.NullBooleanSelect(attrs={'class':'form-control mt-3', 'placeholder':'realizada'})

        }

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha', None)
        if fecha < date.today():
            raise forms.ValidationError('fecha ya pasada , no puede pedir cita')

        return fecha


# formulario para domificar la cita por el especialista
class CitaFormModificaEspe(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['fecha', 'idCliente', 'idEspecialista', 'informe', 'realizada']
        informe = forms.CharField(required=False)
        # fields = ['fecha','idCliente','idEspecialista'

        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control mt-3', 'placeholder': 'DD/MM/AAAA'}),
            'idCliente': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'idCliente'}),
            'idEspecialista': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'idEspecialista'}),
            'informe': forms.TextInput(
                attrs={'class': 'form-control mt-3', 'placeholder': 'informe', 'required': 'False' , 'value':' '}),
            'realizada': forms.NullBooleanSelect(attrs={'class': 'form-control mt-3', 'placeholder': 'realizada'})

        }


# formulario para ver los detalles de una cita historica
class CitaDetailHistorical(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['fecha', 'idCliente', 'idEspecialista', 'informe', 'realizada']

        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control mt-3', 'placeholder': 'DD/MM/AAAA'}),
            'idCliente': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'idCliente'}),
            'idEspecialista': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'idEspecialista'}),
            'informe': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'informe'}),
            'realizada': forms.NullBooleanSelect(attrs={'class': 'form-control mt-3', 'placeholder': 'realizada'})

        }

# formulario para mensajes
class MensajeUpdateForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['idEmisor', 'idReceptor',  'asunto', 'texto','leido']

        widgets = {
            'idEmisor': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'idEmisor'}),
            'idReceptor': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'idReceptor'}),
            #'fecha': forms.DateField(attrs={'class': 'form-control mt-3', 'placeholder': 'DD/MM/AAAA'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'asunto'}),
            'texto': forms.Textarea(attrs={'class': 'form-control mt-3', 'placeholder': 'texto'}),
            'leido': forms.NullBooleanSelect(attrs={'class': 'form-control mt-3', 'placeholder': 'realizada'})

        }

