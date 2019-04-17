from django.contrib import admin
from mapwidgets.widgets import GooglePointFieldWidget

from apps.mentor.models import *


class MentorAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #    models.PointField: {"widget": GooglePointFieldWidget}
    # }
    list_display = ('id', 'DNI', 'tipo', 'wannaBeMentor', 'idUser',)
    list_filter = ('wannaBeMentor',)


admin.site.register(Mentor, MentorAdmin)
admin.site.register(Mentoria)
