from django.contrib import admin

from django.urls import path,include

import core.views
from . import views

urlpatterns = [
    path('', views.index,name = "index"),
    path('about_us/',views.about_us,name='about_us'),
    path("blog/",views.blog,name='blog'),
    path("contact_us/",views.contact_us,name="contact_us"),
    path("gallery/",views.gallery,name="gallery"),
    path("services/",views.services,name="services"),
    path("login/",views.login,name="login"),

    #ampliacion
    path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/', include('registration.urls')),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/signup/cliente/', views.ClienteSignUpView.as_view(), name='cliente_signup'),
    path('accounts/signup/especialista/', views.EspecialistaSignUpView.as_view(), name='especialista_signup'),

]