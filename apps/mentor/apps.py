from django.apps import AppConfig


class MentorConfig(AppConfig):
    name = 'apps.mentor'
    verbose_name = 'Mentor'

    def ready(self):
        try:
            from . import signals
        except ImportError:
            pass
