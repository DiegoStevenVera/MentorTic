from enum import Enum

from django.contrib.gis.db import models

from apps.behaviors import TimesStampedModel
from apps.users.models import User


class Mentor(TimesStampedModel):
    class Tipo(Enum):
        APRENDIZ = "Aprendiz"
        MENTOR = "Mentor"

    DNI = models.CharField('DNI', unique=True, max_length=8)
    DNIUpline = models.IntegerField('DNIUpline', null=False)
    location = models.PointField('Location', null=True, blank=True)
    tipo = models.CharField('Tipo', max_length=10, blank=True, null=True,
                              choices=[(item.name, item.value) for item in Tipo])
    mentorPadre = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='Mentores')
    idUser = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mentor')

    def __str__(self):
        return '{} - {}'.format(self.DNI, self.idUser.first_name)

    class Meta:
        verbose_name = 'Mentor'
        verbose_name_plural = 'Mentores'


class Mentoria(TimesStampedModel):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='mentoria')
    fecha = models.DateTimeField('Fecha y hora', null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.mentor)

    class Meta:
        verbose_name = 'Mentoria'
        verbose_name_plural = 'Mentorias'