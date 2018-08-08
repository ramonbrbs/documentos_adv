from django.contrib import admin
from .models import Cliente

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    '''Admin View for Cliente '''
    readonly_fields = ('advogado',)
    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.advogado = request.user
        super().save_model(request, obj, form, change) 