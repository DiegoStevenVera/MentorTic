from django.contrib import admin
from mapwidgets.widgets import GooglePointFieldWidget

from apps.mentor.models import *


class MentorAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.PointField: {"widget": GooglePointFieldWidget}
    }


#admin.site.register(Mentor, MentorAdmin)
admin.site.register(Mentor)
admin.site.register(Mentoria)