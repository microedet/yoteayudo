from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name = "index"),
    path('about_us/',views.about_us,name='about_us'),
    path("blog/",views.blog,name='blog'),
    path("contact_us/",views.contact_us,name="contact_us"),
    path("gallery/",views.gallery,name="gallery"),
    path("services/",views.services,name="blog"),

]