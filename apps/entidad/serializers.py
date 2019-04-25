from rest_framework import serializers

from apps.entidad.models import Entidad, Representante


class EntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidad
        fields = '__all__'
        read_only_fields = ('id',)


class RepresentanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Representante
        fields = '__all__'
        read_only_fields = ('id',)


class EntidadRetrieveSerializer(serializers.ModelSerializer):
    representante = RepresentanteSerializer(read_only=True)

    class Meta:
        model = Entidad
        fields = '__all__'
        read_only_fields = ('id',)