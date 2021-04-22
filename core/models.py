from django.db import models

# Create your models here.

class Usuario(models.Model):
    id=models.AutoField(verbose_name="idUsuario",primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = 'usuarios'
       # ordering = ['id']

    def __str__(self):
        return  self.username + " " + self.password


class Cliente (models.Model):
    #id=models.AutoField(verbose_name="idCLiente",primary_key=True)
    dni=models.CharField(max_length=10)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    fechaNacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    foto = models.ImageField(upload_to='core', verbose_name="Foto")
    idUsuario= models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name="ClienteidUsuario")


    class Meta:
        verbose_name= "cliente"
        verbose_name_plural='clientes'
        ordering= ['id']

    def __str__(self):
        return self.dni + " " + self.nombre + " " + self.apellido


class Especialista(models.Model):
    #id = models.AutoField(verbose_name="idEspecialista", primary_key=True)
    dni = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    fechaNacimiento = models.DateField(verbose_name="Fecha de Nacimiento")
    foto = models.ImageField(upload_to='core', verbose_name="Foto")
    biografia= models.CharField(max_length=255,verbose_name="biografia")
    idUsuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name="EspecialistaidUsuario")


    class Meta:
        verbose_name = "especialista"
        verbose_name_plural = 'especialistas'
        ordering = ['id']

    def __str__(self):
        return self.dni + " " + self.nombre + " " + self.apellido


class Cita(models.Model):
    #id = models.AutoField(verbose_name="idCita",primary_key=True)
    fechaAlta = models.DateTimeField(verbose_name="Fecha de Alta",auto_now_add=True)
    idCliente= models.ForeignKey(Cliente,on_delete=models.CASCADE,related_name="CitaidCliente")
    idEspecialista= models.ForeignKey(Especialista,on_delete=models.CASCADE,related_name="CitaidEspecialista")
    informe= models.TextField(verbose_name="Cita Texto Informe")
    realizada= models.BooleanField(verbose_name="Cita realizada", default=False)


    class Meta:
        verbose_name = "cita"
        verbose_name_plural = 'citas'
        #ordering = ['id']

    def __str__(self):
        return str(self.id) + " " + str(self.idCliente) + " " + str(self.idEspecialista)





class Mensaje(models.Model):
    #id = models.AutoField(verbose_name="idMensaje",primary_key=True)
    idEmisor=models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name="MensajeidEmisor")
    idReceptor=models.ForeignKey(Usuario,on_delete=models.CASCADE,related_name="MensajeidReceptor")
    fecha = models.DateTimeField(verbose_name="Fecha de Mensaje", auto_now=True)
    asunto = models.CharField(verbose_name="asunto Mensaje",max_length=50)
    texto= models.TextField(verbose_name="texto Mensaje")
    leido= models.BooleanField(verbose_name="Mensaje leido", default=False)


    class Meta:
        verbose_name = "mensaje"
        verbose_name_plural = 'mensajes'
        ordering = ['id']

    def __str__(self):
        return str(self.idEmisor) + " "  + str(self.idReceptor) + " "+ self.asunto + " "
        + self.texto + " "


