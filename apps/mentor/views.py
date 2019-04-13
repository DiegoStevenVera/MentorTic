import geocoder
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.mentor.serializers import *


class MentorListView(generics.ListCreateAPIView):
    queryset = Mentor.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MentorSerializer

        return MentorCreateSerializer


class MentorRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializerRetrieve
    permission_classes = (IsAuthenticated,)


class MentoriaListView(generics.ListCreateAPIView):
    queryset = Mentoria.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MentoriaSerializer

        return MentoriaCreateSerializer


class MentoriaRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mentoria.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MentoriaSerializer

        return MentoriaCreateSerializer