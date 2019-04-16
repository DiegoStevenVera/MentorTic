from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.mentor import models
from apps.users.models import User


@receiver(post_save, sender=User)
def create_mentor(sender, instance, created, **kwargs):
    if not created:
        return
    mentor = models.Mentor(idUser=instance)
    mentor.save()