import geocoder
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from apps.mentor.serializers import *


class MentorListView(generics.ListCreateAPIView):
    queryset = Mentor.objects.all()
    #permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MentorSerializer

        return MentorCreateSerializer


class MentorRUDView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj = get_object_or_404(Mentor, id=self.kwargs['pk'])
        return obj

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MentorSerializer

        return UserMentorSerializer


class MentoriaListView(generics.ListCreateAPIView):
    queryset = Mentoria.objects.all()
    #permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MentoriaSerializer

        return MentoriaCreateSerializer


class MentoriaRUDView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MentoriaSerializer

        return MentoriaCreateSerializer

    def get_object(self):
        obj = get_object_or_404(Mentoria, id=self.kwargs['pk'])
        return obj


class MentorByUserRUD(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MentorSerializer

        return UserMentorSerializer

    def get_object(self):
        try:
            mentor = Mentor.objects.get(idUser=self.request.user.id)
        except Mentor.DoesNotExist:
            mentor = None
        return mentor
