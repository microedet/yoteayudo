import readline as readline
from django.contrib import admin

# Register your models here.
from .models import Cliente,Especialista

class ClienteAdmin(admin.ModelAdmin):
    readline
admin.site.register(Cliente,ClienteAdmin)

class EspecialistaAdmin(admin.ModelAdmin):
    readline
admin.site.register(Especialista,EspecialistaAdmin)