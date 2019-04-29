from enum import Enum

from django.contrib.gis.db import models

from apps.behaviors import TimesStampedModel
from apps.entidad.models import Entidad
from apps.ubigeos.models import Distrito
from apps.users.models import User


class Mentor(TimesStampedModel):
    class Tipo(Enum):
        Aprendiz = "Aprendiz"
        Mentor = "Mentor"

    DNI = models.CharField('DNI', unique=True, max_length=8, null=True, blank=True)
    location = models.ForeignKey(Distrito, null=True, blank=True, on_delete=models.CASCADE)
    tipo = models.CharField('Tipo', max_length=10, blank=True, null=True, default='Aprendiz',
                              choices=[(item.name, item.value) for item in Tipo])
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, null=True, blank=True, related_name='Mentores')
    mentorPadre = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='Mentores')
    #estará en falso para todos pero si es aprendiz y está en verdadero entonces quiere ser mentor
    wannaBeMentor = models.BooleanField('Quiero ser mentor', null=False, blank=False, default=False)
    idUser = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mentor')

    def __str__(self):
        return '{}'.format(self.idUser.email)

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