from django.contrib import admin
from apps.personas.models import Persona

# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    # readonly_fields = ('correoCliente',) #No permite edicion de create y update
    # readonly_fields = ('created', 'updated') #No permite edicion de create y update
    list_display = ()
    ordering = ()  # En caso que sea una sola ordering('column',)
    #form de busqueda
    search_fields = ('nombrePersona','correoPersona') #Campo relacionado

    list_filter = ('cedulaPersona','nombrePersona','apellidoPersona','direccionPersona','telefonoPersona') # Campos relacionados


admin.site.register(Persona, PersonaAdmin)