from django.contrib import admin

from apps.entidad.models import Entidad, Representante


class EntidadAdmin(admin.ModelAdmin):
    list_display = ('RUC', 'razon_social', 'esFicticia')
    list_filter = ('Mentores',)


admin.site.register(Entidad, EntidadAdmin)
admin.site.register(Representante)