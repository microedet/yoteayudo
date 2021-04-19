import readline as readline
from django.contrib import admin

# Register your models here.
from .models import Cliente,Especialista,Usuario,Mensaje,Cita

class ClienteAdmin(admin.ModelAdmin):
    #readline
    list_display = ('dni','nombre','apellido')
    ordering = ('apellido',)
    search_fields = ('nombre','dni')



class EspecialistaAdmin(admin.ModelAdmin):
    #readline
    list_display = ('dni','nombre','apellido')
    ordering = ('apellido',)
    search_fields = ('nombre','dni')
    #list_filter



admin.site.register(Especialista,EspecialistaAdmin)
admin.site.register(Cliente,ClienteAdmin)


#admin.site.register(Cliente)
#admin.site.register(Especialista)
admin.site.register(Usuario)
admin.site.register(Mensaje)
admin.site.register(Cita)