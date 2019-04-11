from django.db import models


class Entidad(models.Model):
    RUC = models.CharField('RUC', unique=True, max_length=11)
    razon_social = models.CharField('Razon social', max_length=30, unique=True, blank=False, null=False)
    celular = models.IntegerField('Celular', null=False, blank=False)
    email = models.EmailField('Correo electronico', null=False, blank=False)

    def __str__(self):
        return '{}'.format(self.RUC)

    class Meta:
        verbose_name = 'Entidad'
        verbose_name_plural = 'Entidades'