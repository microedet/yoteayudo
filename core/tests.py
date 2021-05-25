from django.test import TestCase
from django.contrib.auth.models import AbstractUser
from django.db import models
from .models import Thread, Cita, Usuario, Mensaje


# Create your tests here.
class ThreadTestCase(TestCase):
    def setUp(self):
        self.cliente1 = Usuario.objects.create_user('cliente1',None,'password123')
        self.especialista1 = Usuario.objects.create_user('especialista1',None,'password123')

        self.thread = Thread.objects.create()

    def test_add_usuarios_to_thread(self):
        self.thread.usuarios.add(self.cliente1,self.especialista1)
        self.assertEqual(len(self.thread.usuarios.all()),2)

    def test_filter_thread_by_users(self):
        self.thread.usuarios.add(self.cliente1, self.especialista1)
        threads = Thread.objects.filter(usuarios=self.cliente1).filter(usuarios=self.especialista1)
        self.assertEqual(self.thread, threads[0])

    def test_filter_non_existent_thread(self):
        threads = Thread.objects.filter(usuarios=self.cliente1).filter(usuarios=self.especialista1)
        self.assertEqual(len(threads),0)




    def test_add_messages_to_thread(self):
        self.thread.usuarios.add(self.cliente1, self.especialista1)
        mensaje1= Mensaje.objects.create(usuarios=self.cliente1, content="hola son cliente1")
        mensaje2= Mensaje.objects.create(usuarios=self.especialista1, content="hola yo soy especialista1")
        self.thread.mensajes.add(mensaje1,mensaje2)
        self.assertEqual(len(self.thread.mensajes.all()), 2)

        for menssage in  self.thread.mensajes.all():
            print("({}): {}".format(menssage.user,menssage.content))

