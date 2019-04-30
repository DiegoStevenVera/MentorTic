from rest_framework import serializers

from apps.entidad.serializers import EntidadSerializer
from apps.mentor.models import Mentor, Mentoria
from apps.users.serializers import UserSerializer


class MentorSerializer(serializers.ModelSerializer):
    idUser = UserSerializer(read_only=True)
    entidad = EntidadSerializer(read_only=True)

    class Meta:
        model = Mentor
        fields = (
            'id', 'tipo', 'entidad', 'location', 'wannaBeMentor', 'mentorPadre', 'Mentores',
            'idUser', 'created_at', 'last_modified'
        )


class UserMentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = (
            'id', 'location', 'entidad', 'tipo', 'wannaBeMentor',
        )

    def update(self, instance, validated_data):
        instance.DNI = validated_data.get('DNI', instance.DNI)
        instance.location = validated_data.get('location', instance.location)
        instance.tipo = validated_data.get('tipo', instance.tipo)
        instance.wannaBeMentor = validated_data.get('wannaBeMentor', instance.wannaBeMentor)
        if instance.tipo == 'MENTOR':
            instance.wannaBeMentor = False
        instance.entidad = validated_data.get('entidad', instance.entidad)

        instance.save()
        return instance


class MentorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = (
            'id', 'tipo', 'entidad', 'location','mentorPadre', 'idUser', 'created_at','last_modified'
        )


class MentorgetSerializer(serializers.ModelSerializer):
    idUser = UserSerializer(read_only=True)

    class Meta:
        model = Mentor
        fields = (
            'id', 'tipo', 'location', 'idUser'
        )


class MentoriaSerializer(serializers.ModelSerializer):
    mentor = MentorgetSerializer()

    class Meta:
        model = Mentoria
        fields = (
            'id', 'mentor', 'fecha', 'created_at', 'last_modified'
        )
        read_only_fields = ('id',)


class MentoriaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentoria
        fields = (
            'id', 'mentor', 'fecha', 'created_at', 'last_modified'
        )
        read_only_fields = ("id",)


class MentoriaGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentoria
        fields = (
            'id', 'fecha', 'created_at', 'last_modified'
        )
        read_only_fields = ('id',)


class MentorSerializerRetrieve(serializers.ModelSerializer):
    idUser = UserSerializer(read_only=True)
    mentoria = MentoriaGetSerializer(read_only=True, many=True)
    entidad = EntidadSerializer(read_only=True)

    class Meta:
        model = Mentor
        fields = (
            'id', 'tipo', 'entidad', 'wannaBeMentor', 'location', 'mentorPadre', 'Mentores', 'idUser',
            'mentoria', 'created_at', 'last_modified'
        )
