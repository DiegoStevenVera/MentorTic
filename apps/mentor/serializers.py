from rest_framework import serializers

from apps.mentor.models import Mentor, Mentoria
from apps.users.serializers import RetrieveUserSerializer


class MentorSerializer(serializers.ModelSerializer):
    idUser = RetrieveUserSerializer(read_only=True)

    class Meta:
        model = Mentor
        fields = (
            'id','DNI', 'tipo', 'location','mentorPadre', 'Mentores',
            'idUser', 'created_at', 'last_modified'
        )


class UserMentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = (
            'id', 'DNI', 'location', 'tipo'
        )


class MentorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = (
            'id','DNI', 'tipo', 'location','mentorPadre', 'idUser', 'created_at','last_modified'
        )


class MentorgetSerializer(serializers.ModelSerializer):
    idUser = RetrieveUserSerializer(read_only=True)

    class Meta:
        model = Mentor
        fields = (
            'id', 'DNI', 'tipo','location', 'idUser'
        )


class MentoriaSerializer(serializers.ModelSerializer):
    mentor = MentorgetSerializer()

    class Meta:
        model = Mentoria
        fields = (
            'id', 'mentor', 'fecha', 'created_at','last_modified'
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
            'id', 'fecha', 'created_at','last_modified'
        )
        read_only_fields = ('id',)


class MentorSerializerRetrieve(serializers.ModelSerializer):
    idUser = RetrieveUserSerializer(read_only=True)
    mentoria = MentoriaGetSerializer(read_only=True, many=True)

    class Meta:
        model = Mentor
        fields = (
            'id', 'DNI', 'tipo', 'location','mentorPadre', 'Mentores', 'idUser',
            'mentoria', 'created_at', 'last_modified'
        )