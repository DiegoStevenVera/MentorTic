from enum import Enum

from django.db import models

from apps.users.models import User


class Mentor(models.Model):
    class Tipo(Enum):
        APRENDIZ = "Aprendiz"
        MENTOR = "Mentor"

    DNI = models.CharField('DNI', unique=True, max_length=8)
    DNIUpline = models.IntegerField('DNIUpline', null=False)
    tipo = models.CharField('Tipo', max_length=10, blank=True, null=True,
                              choices=[(item.name, item.value) for item in Tipo])
    mentor = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='Mentor')
    idUser = models.OneToOneField(User, on_delete=models.CASCADE, related_name='mentor')

    def __str__(self):
        return '{} - {}'.format(self.DNI, self.idUser.first_name)

    class Meta:
        verbose_name = 'Mentor'
        verbose_name_plural = 'Mentores'


class Mentoria(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='mentoria')
    fecha = models.DateTimeField('Fecha y hora', null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.mentor)

    class Meta:
        verbose_name = 'Mentoria'
        verbose_name_plural = 'Mentorias'