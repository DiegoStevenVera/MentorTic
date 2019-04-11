from rest_framework import generics

from apps.mentor.serializers import *


class MentorListView(generics.ListCreateAPIView):
    queryset = Mentor.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return MentorSerializer

        return MentorCreateSerializer


class MentorRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializerRetrieve


class MentoriaListView(generics.ListCreateAPIView):
    queryset = Mentoria.objects.all()
    serializer_class = MentoriaSerializer


class MentoriaRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mentoria.objects.all()
    serializer_class = MentoriaSerializer