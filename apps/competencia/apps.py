from django.apps import AppConfig


class CompetenciaConfig(AppConfig):
    name = 'apps.competencia'
    verbose_name = 'Competencia'

    def ready(self):
        try:
            from . import signals
        except ImportError:
            pass
