from rest_framework import serializers

from apps.competencia.models import *
from apps.mentor.serializers import MentorSerializer, MentoriaSerializer


class CompetenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencia
        fields = (
            'id','nombre', 'duracion'
        )
        read_only_fields = ('id',)


class CompetenciaLogradaSerializer(serializers.ModelSerializer):
    mentor = MentorSerializer()
    competencia = CompetenciaSerializer()

    class Meta:
        model = CompLograda
        fields = (
            'id', 'mentor', 'competencia', 'entidad', 'grado', 'especialidad', 'puesto', 'periodo'
        )
        read_only_fields = ('id', 'mentor', 'competencia')


class CompetenciaLogradaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompLograda
        fields = (
            'id', 'mentor', 'competencia', 'entidad', 'grado', 'especialidad', 'puesto', 'periodo'
        )
        read_only_fields = ('id',)


class CompPlanifSerializer(serializers.ModelSerializer):
    mentoria = MentoriaSerializer(read_only=True)
    competencia = CompetenciaSerializer(read_only=True)

    class Meta:
        model = CompPlanif
        fields = (
            'id', 'mentoria', 'competencia', 'periodo', 'estado'
        )
        read_only_fields = ('id',)


class CompPlanifCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompPlanif
        fields = (
            'id', 'mentoria', 'competencia', 'periodo', 'estado'
        )
        read_only_fields = ('id',)


class ReferenteSerializer(serializers.ModelSerializer):
    competencia = CompetenciaSerializer(read_only=True)
    mentor = MentorSerializer(read_only=True)

    class Meta:
        model = Referente
        fields = (
            'id', 'competencia', 'mentor', 'puntaje'
        )
        read_only_fields = ('id',)


class ReferenteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referente
        fields = (
            'id', 'competencia', 'mentor', 'puntaje'
        )
        read_only_fields = ('id',)