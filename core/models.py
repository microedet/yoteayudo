from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class Usuario(AbstractUser):
    is_cliente = models.BooleanField(default=False)
    is_especialista = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = 'Usuarios'
        ordering = ['id']

    def __str__(self):
        return str(self.id) + " " + self.username


class Cliente(models.Model):
    dni = models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    fechaNacimiento = models.DateField(null=True, verbose_name="Fecha de Nacimiento")
    foto = models.ImageField(upload_to='core', verbose_name="Foto")
    idUsuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True,
                                     related_name="ClienteidUsuario")

    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = 'clientes'
        #ordering = ['idUsuario']

    def __str__(self):
        return str(self.idUsuario)+" "+self.dni + " " + self.nombre + " " + self.apellido


class Especialista(models.Model):
    dni = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    fechaNacimiento = models.DateField(null=True,verbose_name="Fecha de Nacimiento")
    foto = models.ImageField(upload_to='core', verbose_name="Foto")
    biografia = models.CharField(max_length=255, verbose_name="biografia")
    idUsuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True,
                                     related_name="EspecialistaidUsuario")

    class Meta:
        verbose_name = "especialista"
        verbose_name_plural = 'especialistas'
        ordering = ['idUsuario']

    def __str__(self):
        return str(self.idUsuario) + " " + self.dni + " " + self.nombre + " " + self.apellido


class Cita(models.Model):
    fecha = models.DateField(verbose_name="Fecha")
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="CitaidCliente")
    idEspecialista = models.ForeignKey(Especialista, on_delete=models.CASCADE, related_name="CitaidEspecialista")
    informe = models.TextField(verbose_name="Cita Texto Informe")
    realizada = models.BooleanField(verbose_name="Cita realizada", default=False)

    class Meta:
        verbose_name = "cita"
        verbose_name_plural = 'citas'
        ordering = ['id']

    def __str__(self):
        return str(self.id) + " " + str(self.idCliente) + " " + str(self.idEspecialista)


class Mensaje(models.Model):
    idEmisor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="MensajeidEmisor")
    idReceptor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="MensajeidReceptor")
    fecha = models.DateTimeField(verbose_name="Fecha de Mensaje", auto_now=True)
    asunto = models.CharField(verbose_name="asunto Mensaje", max_length=50)
    texto = models.TextField(verbose_name="texto Mensaje")
    leido = models.BooleanField(verbose_name="Mensaje leido", default=False)

    class Meta:
        verbose_name = "mensaje"
        verbose_name_plural = 'mensajes'
        # ordering = ['id']

    def __str__(self):
        return str(self.idEmisor) + " " + str(self.idReceptor) + " " + self.asunto + " "
        + self.texto + " "
