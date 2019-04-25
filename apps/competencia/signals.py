from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.competencia import models
from apps.mentor.models import Mentor


@receiver(post_save, sender=Mentor)
def create_hv(sender, instance, created, **kwargs):
    if not created:
        return
    hv = models.Hoja_Vida(mentor=instance)
    hv.save()
