from django.db import models

from apps.behaviors import TimesStampedModel
from apps.entidad.models import Entidad
from apps.mentor.models import Mentor, Mentoria


class Competencia(TimesStampedModel):
    nombre = models.CharField('Nombre competencia', max_length=30, null=False, blank=False)
    duracion = models.CharField('Duracion competencia', max_length=10, null=False, blank=False)

    def __str__(self):
        return '{} - {}'.format(self.id, self.nombre)

    class Meta:
        verbose_name = 'Competencia'
        verbose_name_plural = 'Competencias'


class CompLograda(TimesStampedModel):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='CompLograda')
    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE, related_name='CompLograda')
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE, related_name='CompLograda')
    grado = models.CharField('Grado', max_length=30, null=False, blank=False)
    especialidad = models.CharField('Especialidad', max_length=30, null=False, blank=False)
    puesto = models.CharField('Puesto', max_length=30, null=False, blank=False)
    periodo = models.CharField('Periodo', max_length=30, null=False, blank=False)

    def __str__(self):
        return '{} - {}'.format(self.mentor, self.competencia)

    class Meta:
        verbose_name = 'Competencia lograda'
        verbose_name_plural = 'Competencias logradas'


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
    competencia = models.ForeignKey(Competencia, on_delete=models.CASCADE, related_name='Referente')
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='Referente')
    puntaje = models.FloatField('Puntaje', null=False, blank=False)

    def __str__(self):
        return '{} - {}'.format(self.mentor, self.competencia)

    class Meta:
        verbose_name = 'Referente'
        verbose_name_plural = 'Referentes'