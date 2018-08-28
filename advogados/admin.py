from django.contrib import admin
from .models import Usuario

# Register your models here.
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    '''Admin View for Cliente '''
    fieldsets = (
        ("Informações Pessoais", {
            'fields': ('first_name','last_name','sexo','email','password','oab_estado','oab','nacionalidade','estado_civil',),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.username = obj.email
            obj.set_password(obj.password)
            obj.is_staff = True
        super().save_model(request, obj, form, change)