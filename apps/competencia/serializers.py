from rest_framework import serializers

from apps.competencia.models import *
from apps.entidad.serializers import EntidadSerializer
from apps.mentor.serializers import MentorSerializer, MentoriaSerializer


class CompetenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencia
        fields = '__all__'
        read_only_fields = ('id',)


class CompetenciaLogradaSerializer(serializers.ModelSerializer):
    mentor = MentorSerializer()
    entidad = EntidadSerializer()

    class Meta:
        model = Hoja_Vida
        fields = '__all__'
        read_only_fields = ('id', 'mentor', 'entidad')


class CompetenciaLogradaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hoja_Vida
        fields = '__all__'
        read_only_fields = ('id',)


class CompPlanifSerializer(serializers.ModelSerializer):
    mentoria = MentoriaSerializer(read_only=True)
    competencia = CompetenciaSerializer(read_only=True)

    class Meta:
        model = CompPlanif
        fields = '__all__'
        read_only_fields = ('id',)


class CompPlanifCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompPlanif
        fields = '__all__'
        read_only_fields = ('id',)


class CompRefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competencia_Referente
        fields = '__all__'
        read_only_fields = ('id',)


class CompRefRetrieveSerializer(serializers.ModelSerializer):
    competencia = CompetenciaSerializer(read_only=True)

    class Meta:
        model = Competencia_Referente
        fields = '__all__'
        read_only_fields = ('id',)


class ReferenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Referente
        fields = '__all__'
        read_only_fields = ('id',)


class ReferenteRetrieveSerializer(serializers.ModelSerializer):
    compRef = CompRefRetrieveSerializer(many=True, read_only=True)

    class Meta:
        model = Referente
        fields = '__all__'
        read_only_fields = ('id',)
