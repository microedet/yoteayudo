import dateutil.utils
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.urls import reverse_lazy, Resolver404
from django.views.generic import CreateView, TemplateView, UpdateView, ListView, DetailView, DeleteView

from core.decorators import especialista_required, cliente_required
from core.forms import ClienteSignupForm, EspecialistaSignupForm, ClienteUpdateForm, EspecialistaUpdateForm, \
    EspecialistaDeleteForm, CitaForm, CitaDetailHistorical, CitaFormModificaEspe, MensajeCreateForm, MensajeUpdateForm
from django import forms
from core.models import Cliente, Especialista, Cita, Mensaje

# decoradores
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


class StaffRequiredMixin(object):

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


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
@method_decorator(cliente_required, name='dispatch')
class ClienteUpdate(UpdateView):
    form_class = ClienteUpdateForm
    success_url = reverse_lazy('index')
    template_name = 'cliente/update_cliente.html'

    def get_object(self):
        # recuperamos el objeto que vamos a editar

        cliente, created = Cliente.objects.get_or_create(idUsuario=self.request.user)
        return cliente


# vista para el formulario del perfil de especialista
@method_decorator(especialista_required, name='dispatch')
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
@method_decorator(cliente_required, name='dispatch')
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
@method_decorator(cliente_required, name='dispatch')
class CitasListView(ListView):
    model = Cita

    # funcion que devuelve las citas que no han sido efectuados por el especialista
    # y que son del cliente
    def get_queryset(self):
        return Cita.objects.filter(realizada=0).filter(idCliente=self.request.user.id).order_by('fecha')


# vista para Historico de citas del cliente que ya han sido realizadas
@method_decorator(cliente_required(), name='dispatch')
class CitasListHistorical(ListView):
    model = Cita
    template_name = 'core/cita_list_historical.html'
    ordering = ['-fecha']
    # funcion que devuelve las citas que han sido efectuados por el especialista y son del cliente
    def get_queryset(self):
        return Cita.objects.filter(realizada=1).filter(idCliente=self.request.user.id).order_by('-fecha')


# Vista para ver el detalle de una cita historica
@method_decorator(login_required(), name='dispatch')
class CitaDetailHistorical(DetailView):
    model = Cita
    form_class = CitaDetailHistorical
    success_url = reverse_lazy('index')
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
@method_decorator(cliente_required, name='dispatch')
class CitaUpdateView(UpdateView):
    model = Cita
    form_class = CitaForm
    success_url = reverse_lazy('modificar_consultar_cita_cliente')
    template_name = 'core/cita_cambio_fecha.html'

    # mediante esta funcion tomamos el valor de la pk, metido en la url, para saber que especialista
    # solicitamos la consulta
    def get_context_data(self, **kwargs):
        context = super(CitaUpdateView, self).get_context_data(**kwargs)

        #al hacer el filtrado por id con la pk y idcliente resulta que si no corresponde a idCLiente logeado da error
        cita = Cita.objects.get(id=self.kwargs.get('pk'),idCliente=self.request.user.id)
        #if cita.DoesNotExist:
            #template_name = 'core/index.html'

        # cliente = Cliente.objects.get(idUsuario_id=self.request.user)
        context['fecha'] = cita.fecha
        context['idEspecialista'] = cita.idEspecialista_id
        context['idCliente'] = cita.idCliente_id
        context['nombre_especialista'] = cita.idEspecialista.nombre
        context['apellido_especialista'] = cita.idEspecialista.apellido

        print(cita)
        return context



# desde aqui se puede borrar cita
@method_decorator(cliente_required, name='dispatch')
class CitaDeleteView(DeleteView):
    model = Cita
    form_class = CitaForm
    success_url = reverse_lazy('modificar_consultar_cita_cliente')


# desde aqui el especialista puede listar los clientes que tienen cita con el
@method_decorator(especialista_required, name='dispatch')
class EspecialistaConsultaClientes(ListView):
    model = Cita
    template_name = 'core/especialista_consulta_cliente.html'

    # funcion que devuelve las citas que no han sido efectuados por el especialista
    def get_queryset(self):
        return Cita.objects.filter(realizada=0).filter(idEspecialista=self.request.user.id).order_by('fecha')


# desde aqui el especialista tiene acceso a una cita pedida por el cliente y le cambia los parametros para
# poner el documento y poner que ha sido realizada
@method_decorator(especialista_required, name='dispatch')
class EspecialistaEditaConsulta(UpdateView):
    model = Cita
    form_class = CitaFormModificaEspe
    success_url = reverse_lazy('especialista_consulta_cliente')
    template_name = 'core/especialista_edita_consulta.html'

    # mediante esta funcion tomamos el valor de la pk, metido en la url, para saber que especialista
    # solicitamos la consulta
    def get_context_data(self, **kwargs):

        try:
            context = super(EspecialistaEditaConsulta, self).get_context_data(**kwargs)
            # especialista= Especialista.objects.get(idUsuario=self.model.idEspecialista)
            #especialista = Especialista.objects.get(idUsuario_id=self.kwargs.get('pk'))
            cita = Cita.objects.get(id=self.kwargs.get('pk'),idEspecialista_id=self.request.user.id)
            context['id'] = cita.id
            context['fecha'] = cita.fecha
            context['idEspecialista'] = cita.idEspecialista_id
            context['idCliente'] = cita.idCliente_id
            context['informe'] = cita.informe
            context['realizada'] = cita.realizada
            return context


        except ObjectDoesNotExist:
            print("Error no puedes ver una consulta que no es tuya ")


# desde aqui el especialista puede listar los historicos de un cliene los clientes que tienen cita con el
@method_decorator(especialista_required, name='dispatch')
class EspecialistaConsultaHistoricoClientes(ListView):
    model = Cita
    template_name = 'core/especialista_consulta_historico_cliente.html'

    # funcion que devuelve las citas que no han sido efectuados por el especialista
    def get_queryset(self,**kwargs):
        # return Cita.objects.filter(realizada=1).filter(idEspecialista=self.request.user.id)
        try:
            return Cita.objects.filter(realizada=1).filter(idCliente=self.kwargs.get('pk')).filter(idEspecialista=self.request.user.id).order_by('-fecha')
        except ObjectDoesNotExist:
            print("No es una consulta suya")


    # mediante esta funcion tomamos el valor de la pk, metido en la url, para saber que especialista
    # solicitamos la consulta
    def get_context_data(self, **kwargs):
        context = super(EspecialistaConsultaHistoricoClientes, self).get_context_data(**kwargs)
        cita = Cita.objects.get(id=self.kwargs.get('pk'))
        especialista=Especialista.objects.get(idUsuario_id=self.request.user)
        context['id'] = cita.id
        context['fecha'] = cita.fecha
        context['idEspecialista'] = especialista.idUsuario_id
        context['idCliente'] = cita.idCliente_id
        context['informe'] = cita.informe
        context['realizada'] = cita.realizada

        return context





# desde aqui el especialista puede listar las citas del especialista en el dia corriente
@method_decorator(especialista_required, name='dispatch')
class EspecialistaConsultaCitasDelDia(ListView):
    model = Cita
    template_name = 'core/especialista_consulta_citas_del_dia.html'

    # funcion que devuelve las citas que no han sido efectuados por el especialista
    def get_queryset(self):
        return Cita.objects.filter(realizada=0).filter(idEspecialista=self.request.user.id).filter(fecha=dateutil.utils.today())


# vista para listado de mensajes recibidos
@method_decorator(login_required, name='dispatch')
class MensajeListView(ListView):
    model = Mensaje
    #template_name = 'core/mensaje_list.html'

    def get_queryset(self):
        return Mensaje.objects.filter(idReceptor=self.request.user.id)
        #return Mensaje.objects.get(leido=1,idReceptor=self.request.user.id).order_by('-fecha')
        #return Mensaje.objects.filter(leido=0,idReceptor=self.request.user).order_by('-fecha')
        print("el idReceptor loqueado es " + Mensaje.idReceptor)



#vista para crear mensaje y enviarlo
@method_decorator(login_required, name='dispatch')
class MensajeCreateView(CreateView):
    model = Mensaje
    form_class = MensajeCreateForm
    success_url = reverse_lazy('index')


#vista para leer los mensajes y ponerlos como leidos
@method_decorator(login_required, name='dispatch')
class MensajeUpdateView(UpdateView):
    model = Mensaje
    template_name = 'core/mensaje_leer.html'
    form_class = MensajeUpdateForm
    success_url = reverse_lazy('mensaje_list')

    # mediante esta funcion tomamos el valor de la pk, metido en la url, para saber que mensaje se quiere leer
    # y se comprueba que el idReceptor sea el que este logeado
    def get_context_data(self, **kwargs):
        try:
            context = super(MensajeUpdateView, self).get_context_data(**kwargs)
            mensaje = Mensaje.objects.get(id=self.kwargs.get('pk'),idReceptor=self.request.user)
            #cliente = Cliente.objects.get(idUsuario_id=self.request.user)
            context['idReceptor'] = mensaje.idReceptor
            context['idEmisor'] = mensaje.idEmisor
            context['fecha'] = mensaje.fecha
            context['asunto'] = mensaje.asunto
            context['texto'] = mensaje.texto
            context['leido'] = mensaje.leido
            return  context
        except ObjectDoesNotExist:
            print("Either the blog or entry doesn't exist.")
            template_name = 'core/index.html'
        except:
          return render('core/404.html')




#vista para borrar mensaje
@method_decorator(login_required, name='dispatch')
class MensajeDeleteView(DeleteView):
    model = Mensaje
    form_class = MensajeUpdateForm
    success_url = reverse_lazy('mensaje_list')

    #para comprobar que el mensaje es tiene como receptor a la persona logeada
    def get_queryset(self):
        try:
         return Mensaje.objects.filter(idReceptor=self.request.user.id)
        except ObjectDoesNotExist:
            print("ERROR ESE MENSAJE NO ES SUYO NO LO PUEDE BORAR")

##VISTAS PARA ERRORES
#404: página no encontrada
def render_to_response(param):
    pass


def pag_404_not_found(request, exception, template_name="error/404.html"):
    response = render_to_response("core/404.html")
    response.status_code=404
    return response


#500: error en el servidor
def pag_500_error_server(request, exception,template_name="error/500.html"):
    response = render_to_response("core/500.html")
    response.status_code=500
    return response


