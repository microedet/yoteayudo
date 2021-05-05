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

    #url  para update especialista
    path('updateespecialista/<int:pk>', views.EspeUpdateView.as_view(), name='espeupdate'),

    # url  para delete especialista
    path('deleteespecialista/<int:pk>', views.EspeDelete.as_view(), name='espedelete'),

]