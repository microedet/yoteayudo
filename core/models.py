from django.db import models

# Create your models here.

class Cliente (models.Model):
    id=models.AutoField(verbose_name="idCLiente",primary_key=True)
    dni=models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    fechaNacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    foto = models.ImageField(upload_to='core', verbose_name="Foto")
    idUsuario=models.IntegerField(unique=True)

    class Meta:
        verbose_name= "cliente"
        verbose_name_plural='clientes'
        ordering= ['id']

    def __str__(self):
        return self.dni + " " + self.nombre + " " + self.apellido

class Usuario(models.Model):
    idUsuario=models.OneToOneField(Cliente,on_delete=models.CASCADE,related_name="Usuario")
    username = models.CharField(max_length=30)
    password = models.IntegerField

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = 'usuarios'
        ordering = ['id']

    def __str__(self):
        return self.id + " " + self.username + " " + self.password

class Especialista(models.Model):
    id = models.AutoField(verbose_name="idEspecialista", primary_key=True)
    dni = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    fechaNacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    foto = models.ImageField(upload_to='core', verbose_name="Foto")
    biografia= models.CharField(max_length=255,verbose_name="biografia")
    idUsuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name="Especialista")


    class Meta:
        verbose_name = "especialista"
        verbose_name_plural = 'especialistas'
        ordering = ['id']

    def __str__(self):
        return self.dni + " " + self.nombre + " " + self.apellido


class Cita(models.Model):
    id = models.AutoField(verbose_name="idCita",primary_key=True)
    fechaAlta = models.DateTimeField(verbose_name="Fecha de Alta",auto_now_add=True)
    idCliente= models.ForeignKey(Cliente,on_delete=models.CASCADE,related_name="Cita_idCliente")
    idEspecialista= models.ForeignKey(Especialista,on_delete=models.CASCADE,related_name="Cita_idCliente")
    informe= models.TextField(verbose_name="texto Informe")
    realizada= models.BooleanField(verbose_name="cita realizada", default=False)


    class Meta:
        verbose_name = "cita"
        verbose_name_plural = 'citas'
        ordering = ['id']

    def __str__(self):
        return self.id + " " + self.username + " " + self.password





class Mensaje(models.Model):
    id = models.AutoField(verbose_name="idMensaje",primary_key=True)
    idEmisor=models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name="Mensaje_id_Emisor")
    idReceptor=models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name="Mensaje_id_Receptor")
    fecha = models.DateTimeField(verbose_name="Fecha de Mensaje", auto_now=True)
    asunto = models.CharField(verbose_name="asunto Mensaje",max_length=50)
    texto= models.TextField(verbose_name="texto Mensaje")
    leido= models.BooleanField(verbose_name="Mensaje leido", default=False)


    class Meta:
        verbose_name = "mensaje"
        verbose_name_plural = 'mensajes'
        ordering = ['id']

    def __str__(self):
        return self.id + " " + self.idEmisor + " "  + self.idReceptor + " "+ self.fecha + " "
        + self.asunto + " "


