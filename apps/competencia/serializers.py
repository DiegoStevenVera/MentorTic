from rest_framework import serializers

from apps.competencia.models import *


class CompetenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencia
        fields = (
            'id','nombre', 'duracion'
        )
        read_only_fields = ('id',)