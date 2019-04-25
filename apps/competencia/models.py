from django.db import models

from apps.behaviors import TimesStampedModel
from apps.entidad.models import Entidad
from apps.mentor.models import Mentoria, Mentor


class Hoja_Vida(TimesStampedModel):
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, related_name='hojaVida', null=True)
    grado = models.CharField('Grado', max_length=30, null=True, blank=True)
    descripcion = models.TextField('Descripcion', null=True, blank=True)
    areasInteres = models.CharField('areas de interes', max_length=200, null=True, blank=True)
    especialidad = models.CharField('Especialidad', max_length=30, null=True, blank=True)
    puesto = models.CharField('Puesto', max_length=30, null=True, blank=True)
    periodo = models.CharField('Periodo', max_length=30, null=True, blank=True)
    mentor = models.OneToOneField(Mentor, on_delete=models.CASCADE, related_name='hojaVida', null=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.mentor)

    class Meta:
        verbose_name = 'Hoja de vida'
        verbose_name_plural = 'Hojas de vida'


class Competencia(TimesStampedModel):
    nombre = models.CharField('Nombre competencia', max_length=30, null=False, blank=False)
    duracion = models.CharField('Duracion competencia', max_length=10, null=False, blank=False)
    hojaVida = models.ForeignKey(Hoja_Vida, on_delete=True, related_name='competencias', null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.nombre)

    class Meta:
        verbose_name = 'Competencia'
        verbose_name_plural = 'Competencias'


class CompPlanif(TimesStampedModel):
    mentoria = models.ForeignKey(Mentoria, on_delete=models.CASCADE, related_name='CompPlanif')
    competencia = models.ForeignKey(Competencia, on_delete=True, related_name='CompPlanif')
    periodo = models.CharField('Periodo', max_length=30, null=False, blank=False)
    estado = models.CharField('Estado', max_length=30, null=False, blank=False)

    def __str__(self):
        return '{} - {}'.format(self.mentoria, self.competencia)

    class Meta:
        verbose_name = 'Competencia planificada'
        verbose_name_plural = 'Competencias planificadas'


class Referente(TimesStampedModel):
    nombre = models.CharField('nombre', max_length=200, null=True, blank=True)
    puntaje = models.FloatField('Puntaje', null=True, blank=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.nombre)

    class Meta:
        verbose_name = 'Referente'
        verbose_name_plural = 'Referentes'


class Competencia_Referente(TimesStampedModel):
    referente = models.ForeignKey(Referente, on_delete=True, related_name='compRef')
    competencia = models.ForeignKey(Competencia, on_delete=True, related_name='compRef')

    def __str__(self):
        return '{} - {}'.format(self.referente, self.competencia)

    class Meta:
        verbose_name = 'Competencia de un perfil'
        verbose_name_plural = 'Competencias de un perfil'
