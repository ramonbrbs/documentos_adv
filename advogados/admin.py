from django.contrib import admin
from .models import Usuario

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    '''Admin View for Cliente '''
    fieldsets = (
        (None, {
            'fields': ('username','first_name','last_name','sexo','email','password','oab_estado','oab','nacionalidade','estado_civil',),
        }),
    )