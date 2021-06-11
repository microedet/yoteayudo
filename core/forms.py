from datetime import datetime, date

from django.contrib.auth.forms import UserCreationForm
from django import forms

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
        fields = ['fecha', 'idCliente', 'idEspecialista']

        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control mt-3', 'placeholder': 'DD/MM/AAAA'}),
            'idCliente': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'idCliente'}),
            'idEspecialista': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'idEspecialista'}),


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

        widgets = {
            'fecha': forms.DateInput(attrs={'class': 'form-control mt-3', 'placeholder': 'DD/MM/AAAA'}),
            'idCliente': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'idCliente'}),
            'idEspecialista': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'idEspecialista'}),
            'informe': forms.TextInput(
                attrs={'class': 'form-control mt-3', 'placeholder': 'informe', 'required': 'False', 'value': ' '}),
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


# formulario para crear mensajes
class MensajeCreateForm(forms.ModelForm):
    class Meta:
        model = Mensaje

        fields = ['idEmisor', 'idReceptor', 'asunto', 'texto']
        #idReceptor = forms.ModelChoiceField.filter(queryset= Usuario.objects.get(is_especialista=True))
        #especialista = forms.ModelChoiceField(queryset= Especialista.objects.order_by('nombre','apellido'))


        widgets = {
            'especialista':forms.Select(attrs={'class': 'form-control mt-3', 'placeholder': 'especialista'}),
            'idEmisor': forms.Select(attrs={'class': 'form-control mt-3', 'placeholder': 'idEmisor'}),
            'idReceptor': forms.Select(attrs={'class': 'form-control mt-3', 'placeholder': 'idReceptor'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'asunto'}),
            'texto': forms.Textarea(attrs={'class': 'form-control mt-3', 'placeholder': 'texto'}),

        }

# formulario para leer mensajes
class MensajeUpdateForm(forms.ModelForm):
    class Meta:
        model = Mensaje

        fields = ['idEmisor', 'idReceptor','asunto','texto','leido']

        widgets = {

            'idEmisor': forms.TextInput(attrs={'readonly':'readonly'}),
            'idReceptor': forms.Select(attrs={'readonly':'readonly'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control mt-3', 'readonly':'readonly'}),
            'texto': forms.Textarea(attrs={'class': 'form-control mt-3', 'readonly':'readonly'}),
            'leido': forms.NullBooleanSelect(attrs={'class': 'form-control mt-3', 'placeholder': 'leido'})

        }

#formulario para filtrado consultas por fechas
class FiltradoConsultaFechas(forms.Form):

    fechaInicio=forms.DateField(label="Fecha Inicial:",required=True,widget=forms.DateInput(attrs={'class':'form-control mt-3','placeholder':'YYYY-MM-DD'}))
    fechaFinal=forms.DateField(label="Fecha Final:",required=True,widget=forms.DateInput(attrs={'class':'form-control mt-3','placeholder':'YYYY-MM-DD'}))





