import readline as readline
from django.contrib import admin

# Register your models here.
from .models import Cliente,Especialista,Usuario,Mensaje,Cita

'''class ClienteAdmin(admin.ModelAdmin):
    readline
admin.site.register(Cliente,ClienteAdmin)

class EspecialistaAdmin(admin.ModelAdmin):
    readline
admin.site.register(Especialista,EspecialistaAdmin)'''


admin.site.register(Cliente)
admin.site.register(Especialista)
admin.site.register(Usuario)
admin.site.register(Mensaje)
admin.site.register(Cita)