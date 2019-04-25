from django.contrib import admin

from apps.entidad.models import Entidad, Representante

admin.site.register(Entidad)
admin.site.register(Representante)