from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView
from core.forms import ClienteSignupForm, EspecialistaSignupForm, ClienteUpdateForm, EspecialistaUpdateForm
from django import forms
from core.models import Cliente, Especialista

#decoradores
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# Create your views here.


def index(request):
    return render(request,"core/index.html")

def about_us(request):
    return render(request,"core/about_us.html")

def contact_us(request):
    return render(request,"core/contact_us.html")

def gallery(request):
    return render(request,"core/gallery.html")

def services(request):
    return render(request,"core/services.html")

def blog(request):
    return render(request,"core/blog.html")

def login(request):
    return render(request,"registration/login.html")

#para registrar el cliente
class ClienteSignUpView(CreateView):
    success_url = reverse_lazy('login')
    template_name = 'registration/signup_cliente.html'
    form_class = ClienteSignupForm

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(ClienteSignUpView, self).get_form()
        # modifico los campos en tiempo real
        form.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre de Usuario'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Confirmar Contraseña'})
        return form

#para registrar el especialista
class EspecialistaSignUpView(CreateView):
    success_url = reverse_lazy('login')
    template_name = 'registration/signup_especialista.html'
    form_class = EspecialistaSignupForm

    def get_success_url(self):
        return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(EspecialistaSignUpView, self).get_form()
        # modifico los campos en tiempo real
        form.fields['username'].widget = forms.TextInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Nombre de Usuario'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class': 'form-control mb-2', 'placeholder': 'Confirmar Contraseña'})
        return form


#da la opcion de elegir el tipo de cuenta
class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

#vista para el formulario del perfil de cliente
@method_decorator(login_required, name='dispatch')
class ClienteUpdate(UpdateView):
    form_class = ClienteUpdateForm
    success_url = reverse_lazy('index')
    template_name = 'cliente/update_cliente.html'

    def get_object(self):
        #recuperamos el objeto que vamos a editar

        cliente , created = Cliente.objects.get_or_create(idUsuario=self.request.user)
        return cliente

#vista para el formulario del perfil de especialista
@method_decorator(login_required, name='dispatch')
class EspecialistaUpdate(UpdateView):
    form_class = EspecialistaUpdateForm
    success_url = reverse_lazy('index')
    template_name = 'especialista/update_especialista.html'

    def get_object(self):
        #recuperamos el objeto que vamos a editar

        especialista , created = Especialista.objects.get_or_create(idUsuario=self.request.user)
        return especialista