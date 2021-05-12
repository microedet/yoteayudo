import requests
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DetailView, DeleteView
from core.forms import ClienteSignupForm, EspecialistaSignupForm, ClienteUpdateForm, EspecialistaUpdateForm, \
    EspecialistaDeleteForm, CitaForm, CitaDetailHistorical
from django import forms
from core.models import Cliente, Especialista, Cita

# decoradores
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


class StaffRequiredMixin(object):

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


# Create your views here.


def index(request):
    return render(request, "core/index.html")


def about_us(request):
    return render(request, "core/about_us.html")


def contact_us(request):
    return render(request, "core/contact_us.html")


def gallery(request):
    return render(request, "core/gallery.html")


def services(request):
    return render(request, "core/services.html")


def blog(request):
    return render(request, "core/blog.html")


def login(request):
    return render(request, "registration/login.html")


# para registrar el cliente
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


# para registrar el especialista
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


# da la opcion de elegir el tipo de cuenta
class SignUpView(TemplateView):
    template_name = 'registration/signup.html'


# vista para el formulario del perfil de cliente
@method_decorator(login_required, name='dispatch')
class ClienteUpdate(UpdateView):
    form_class = ClienteUpdateForm
    success_url = reverse_lazy('index')
    template_name = 'cliente/update_cliente.html'

    def get_object(self):
        # recuperamos el objeto que vamos a editar

        cliente, created = Cliente.objects.get_or_create(idUsuario=self.request.user)
        return cliente


# vista para el formulario del perfil de especialista
@method_decorator(login_required, name='dispatch')
class EspecialistaUpdate(UpdateView):
    form_class = EspecialistaUpdateForm
    success_url = reverse_lazy('index')
    template_name = 'core/especialista_detail.html'

    def get_object(self):
        # recuperamos el objeto que vamos a editar

        especialista, created = Especialista.objects.get_or_create(idUsuario=self.request.user)
        return especialista


# vista para un listado de especialistas
@method_decorator(login_required(), name='dispatch')
class EspecialistasListView(ListView):
    model = Especialista
    # template_name = 'especialista/listview_especialista.html'


# no se usa, usamos el updateview
class EspecialistaDetailView(DetailView):
    model = Especialista


# desde aqui el admin puede modificar el especialista
@method_decorator(staff_member_required, name='dispatch')
class EspeUpdateView(UpdateView):
    model = Especialista
    form_class = EspecialistaUpdateForm
    success_url = reverse_lazy('especialistas')


# desde aqui el admin puede borrar el especialista
@method_decorator(staff_member_required, name='dispatch')
class EspeDelete(DeleteView):
    model = Especialista
    form_class = EspecialistaDeleteForm
    success_url = reverse_lazy('especialistas')


# vista para trabajar con citas
@method_decorator(login_required, name='dispatch')
class CitaCreateView(CreateView):
    model = Cita
    form_class = CitaForm
    success_url = reverse_lazy('index')

    # mediante esta funcion tomamos el valor de la pk, metido en la url, para saber que especialista
    # solicitamos la consulta
    def get_context_data(self, **kwargs):
        context = super(CitaCreateView, self).get_context_data(**kwargs)
        # especialista= Especialista.objects.get(idUsuario=self.model.idEspecialista)
        especialista = Especialista.objects.get(idUsuario_id=self.kwargs.get('pk'))
        cliente = Cliente.objects.get(idUsuario_id=self.request.user)
        context['idEspecialista'] = especialista.idUsuario_id
        context['idCliente'] = cliente.idUsuario_id
        context['nombre_especialista'] = especialista.nombre
        context['apellido_especialista'] = especialista.apellido

        # print(especialista)
        return context


# vista para listado de citas del cliente que no sido realizadas
@method_decorator(login_required(), name='dispatch')
class CitasListView(ListView):
    model = Cita

    # funcion que devuelve las citas que no han sido efectuados por el especialista
    def get_queryset(self):
        return Cita.objects.filter(realizada=0)


# vista para Historico de citas del cliente que ya han sido realizadas
@method_decorator(login_required(), name='dispatch')
class CitasListHistorical(ListView):
    model = Cita
    template_name = 'core/cita_list_historical.html'

    #funcion que devuelve las citas que han sido efectuados por el especialista
    def get_queryset(self):
        return Cita.objects.filter(realizada=1)


# Vista para ver el detalle de una cita historica
@method_decorator(login_required(), name='dispatch')
class CitaDetailHistorical(DetailView):
    model = Cita
    form_class= CitaDetailHistorical
    #success_url = reverse_lazy('historico_consulta_cliente')
    template_name = 'core/cita_detail_historical.html'


    # mediante esta funcion tomamos el valor de la pk, metido en la url, para saber que cita historica
    # solicitamos la consulta
    def get_context_data(self, **kwargs):
        context = super(CitaDetailHistorical, self).get_context_data(**kwargs)
        cita = Cita.objects.get(id=self.kwargs.get('pk'))
        context['fecha'] = cita.fecha
        context['idEspecialista'] = cita.idEspecialista_id
        context['idCliente'] = cita.idCliente_id
        context['informe'] = cita.informe
        context['realizada'] = cita.realizada
        context['nombre_especialista'] = cita.idEspecialista.nombre
        context['apellido_especialista'] = cita.idEspecialista.apellido

        # print(especialista)
        return context



# desde aqui el cliente puede modificar la fecha de la consulta
@method_decorator(login_required, name='dispatch')
class CitaUpdateView(UpdateView):
    model = Cita
    form_class = CitaForm
    success_url = reverse_lazy('modificar_consultar_cita_cliente')
    template_name = 'core/cita_cambio_fecha.html'

    # mediante esta funcion tomamos el valor de la pk, metido en la url, para saber que especialista
    # solicitamos la consulta
    def get_context_data(self, **kwargs):
        context = super(CitaUpdateView, self).get_context_data(**kwargs)
        cita = Cita.objects.get(id=self.kwargs.get('pk'))
        # cliente = Cliente.objects.get(idUsuario_id=self.request.user)
        context['fecha'] = cita.fecha
        context['idEspecialista'] = cita.idEspecialista_id
        context['idCliente'] = cita.idCliente_id
        context['nombre_especialista'] = cita.idEspecialista.nombre
        context['apellido_especialista'] = cita.idEspecialista.apellido

        # print(especialista)
        return context


# desde aqui se puede borrar cita
@method_decorator(login_required, name='dispatch')
class CitaDeleteView(DeleteView):
    model = Cita
    form_class = CitaForm
    success_url = reverse_lazy('modificar_consultar_cita_cliente')

