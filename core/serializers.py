from rest_framework import  serializers
from core.models import Cita, Especialista


class EspecialistaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Especialista
        fields = ['dni','nombre','apellido','direccion','fechaNacimiento','foto','biografia','idUsuario']



class CitaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = ['fecha','idCliente','idEspecialista','informe','realizada']
        depth = 5

'''
class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['is_cliente','is_especialista']

class ClienteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['dni','nombre','apellido','direccion','fechaNacimiento','foto','idUsuario']




class MensajeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = ['idEmisor','idReceptor','fecha','asunto','texto','leido']

'''


