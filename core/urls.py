from django.urls import path,include
from . import views
from .views import SignUpView, ClienteSignUpView, EspecialistaSignUpView, ClienteUpdate, EspecialistaUpdate, \
    EspecialistaDetailView, EspecialistasListView


urlpatterns = [
    path('', views.index,name = "index"),
    path('about_us/',views.about_us,name='about_us'),
    path("blog/",views.blog,name='blog'),
    path("contact_us/",views.contact_us,name="contact_us"),
    path("gallery/",views.gallery,name="gallery"),
    path("services/",views.services,name="services"),
    path("login/",views.login,name="login"),

    #urls para hacer los registros
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', SignUpView.as_view(), name='signup'),
    path('accounts/signup/cliente/', ClienteSignUpView.as_view(), name='cliente_signup'),
    path('accounts/signup/especialista/', EspecialistaSignUpView.as_view(), name='especialista_signup'),

    #urls para hacer update cliente
    path('updatecliente/',ClienteUpdate.as_view(),name='updatecliente'),

    #urls para hacer update cliente
    #path('updateespecialista/<int:pk>',EspecialistaUpdate.as_view(),name='updateespecialista'),

    #url para listview de especialista
    path('especialistas/',EspecialistasListView.as_view(),name='especialistas'),

    #url para detailview de especialista
    path('especialista/',views.EspecialistaUpdate.as_view(),name='especialista'),

    # url  para update especialista
    path('updateespecialista/<int:pk>', views.EspeUpdateView.as_view(), name='espeupdate'),

    # url  para delete especialista
    path('deleteespecialista/<int:pk>', views.EspeDelete.as_view(), name='espedelete'),

    #url para solicitar cita
    path('solicitarcita/<int:pk>', views.CitaCreateView.as_view(), name='solicitarcita'),

    #url para listado de citas del cliente
    path('modificar_consultar_cita_cliente/', views.CitasListView.as_view(), name='modificar_consultar_cita_cliente'),

    #url para modificar la fecha de la consulta del especialista
    path('cambio_fecha_cita_cliente/<int:pk>', views.CitaUpdateView.as_view(), name='cambio_fecha_cita_cliente'),

    #url para borrar la consulta del especialista
    path('borrar_cita_cliente/<int:pk>', views.CitaDeleteView.as_view(), name='borrar_cita_cliente'),

    #url para consultar historico de citas
    path('historico_consulta_cliente', views.CitasListHistorical.as_view(), name='historico_consulta_cliente'),

    #url para consultar detalles de cita historica
    path('consulta_historica/<int:pk>', views.CitaDetailHistorical.as_view(), name='consulta_historica'),

    #url para que el especialista consulte los pacientes
    path('especialista_consulta_cliente', views.EspecialistaConsultaClientes.as_view(), name='especialista_consulta_cliente'),

    #url para que el especialista vea los detalles de una consulta no realizada y la modifica
    path('especialista_edita_consulta/<int:pk>', views.EspecialistaEditaConsulta.as_view(),
         name='especialista_edita_consulta'),

    # url para que el especialista vea el historial de cada cliente
    path('especialista_consulta_historico_cliente/<int:pk>', views.EspecialistaConsultaHistoricoClientes.as_view(),
         name='especialista_consulta_historico_cliente'),

    # url para que el especialista consulte las citas del dia presente
    path('especialista_consulta_citas_del_dia/', views.EspecialistaConsultaCitasDelDia.as_view(),
         name='especialista_consulta_citas_del_dia'),

    #url para consultar mensajes recibidos
    path('mensaje_list/', views.MensajeListView.as_view(),
         name='mensaje_list'),

    #url para hacer mensajes
    path('enviar_mensaje/', views.MensajeUpdateView.as_view(),name='enviar_mensaje'),

]

