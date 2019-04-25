from enum import Enum
from django.db import models

from apps.behaviors import TimesStampedModel


class Representante(TimesStampedModel):
    class Gender(Enum):
        HOMBRE = "hombre"
        MUJER = "mujer"

    DNI = models.CharField('DNI', unique=True, max_length=8, null=True, blank=True)
    email = models.EmailField('correo electronico', unique=True)
    first_name = models.CharField('nombres', max_length=100)
    last_name = models.CharField('apellidos', max_length=100)
    photo = models.ImageField('foto', upload_to='user', blank=True, null=True)
    gender = models.CharField('genero', max_length=20, blank=True, null=True,
                              choices=[(item.name, item.value) for item in Gender])
    phone = models.CharField('celular', max_length=30, blank=True, null=True)

    def __str__(self):
        return '{} - {}'.format(self.first_name, self.last_name)

    class Meta:
        verbose_name = 'Representante'
        verbose_name_plural = 'Representantes'


class Entidad(TimesStampedModel):
    RUC = models.CharField('RUC', unique=True, max_length=11)
    razon_social = models.CharField('Razon social', max_length=30, unique=True, blank=False, null=False)
    email = models.EmailField('Correo electronico', null=False, blank=False)
    esFicticia = models.BooleanField('Es ficticia?', default=False)
    representante = models.ForeignKey(Representante, on_delete=models.SET_NULL, null=True, blank=True,
                                      related_name='entidad')

    def __str__(self):
        return '{}'.format(self.razon_social)

    class Meta:
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'
