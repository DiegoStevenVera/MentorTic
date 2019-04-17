from rest_framework import serializers

from apps.mentor.models import Mentor, Mentoria
from apps.users.serializers import UserSerializer


class MentorSerializer(serializers.ModelSerializer):
    idUser = UserSerializer(read_only=True)

    class Meta:
        model = Mentor
        fields = (
            'id','DNI', 'tipo', 'location','mentorPadre', 'Mentores',
            'idUser', 'created_at', 'last_modified'
        )


class UserMentorSerializer(serializers.ModelSerializer):
    idUser = UserSerializer()

    class Meta:
        model = Mentor
        fields = (
            'id', 'DNI', 'location', 'tipo', 'wannaBeMentor', 'idUser', 'created_at', 'last_modified'
        )

    def update(self, instance, validated_data):
        instance.DNI = validated_data.get('DNI', instance.DNI)
        instance.location = validated_data.get('location', instance.location)
        instance.tipo = validated_data.get('tipo', instance.tipo)
        instance.wannaBeMentor = validated_data.get('wannaBeMentor', instance.wannaBeMentor)
        if instance.tipo == 'MENTOR':
            instance.wannaBeMentor = False

        user_data = validated_data.pop('idUser')
        user = instance.idUser
        user.first_name = user_data.get('first_name', user.first_name)
        user.last_name = user_data.get('last_name', user.last_name)
        user.phone = user_data.get('phone', user.phone)
        user.gender = user_data.get('gender', user.gender)
        user.photo = user_data.get('photo', user.photo)
        user.save()
        instance.created_at = validated_data.get('created_at', instance.created_at)

        instance.save()
        return instance


class MentorCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = (
            'id','DNI', 'tipo', 'location','mentorPadre', 'idUser', 'created_at','last_modified'
        )


class MentorgetSerializer(serializers.ModelSerializer):
    idUser = UserSerializer(read_only=True)

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
    idUser = UserSerializer(read_only=True)
    mentoria = MentoriaGetSerializer(read_only=True, many=True)

    class Meta:
        model = Mentor
        fields = (
            'id', 'DNI', 'tipo','wannaBeMentor', 'location','mentorPadre', 'Mentores', 'idUser',
            'mentoria', 'created_at', 'last_modified'
        )