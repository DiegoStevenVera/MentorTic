from rest_framework import serializers

from apps.entidad.models import Entidad


class EntidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entidad
        fields = (
            'id','RUC', 'razon_social', 'celular', 'email'
        )
        read_only_fields = ('id',)