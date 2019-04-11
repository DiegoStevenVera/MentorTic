from rest_framework import serializers

from apps.mentor.models import Mentor, Mentoria
from apps.users.serializers import RetrieveUserSerializer


class MentorSerializer(serializers.ModelSerializer):
    idUser = RetrieveUserSerializer(read_only=True)

    class Meta:
        model = Mentor
        fields = (
            'id','DNI', 'DNIUpline', 'tipo', 'Mentor', 'idUser'
        )


class MentorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = (
            'id','DNI', 'DNIUpline', 'tipo', 'Mentor', 'idUser'
        )


class MentoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentoria
        fields = (
            'id', 'mentor', 'fecha'
        )
        read_only_fields = ('id',)


class MentoriaGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentoria
        fields = (
            'id', 'fecha'
        )
        read_only_fields = ('id',)


class MentorSerializerRetrieve(serializers.ModelSerializer):
    idUser = RetrieveUserSerializer(read_only=True)
    mentoria = MentoriaGetSerializer(read_only=True, many=True)

    class Meta:
        model = Mentor
        fields = (
            'id', 'DNI', 'DNIUpline', 'tipo', 'Mentor', 'idUser', 'mentoria'
        )