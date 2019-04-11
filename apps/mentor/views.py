from rest_framework import generics

from apps.mentor.models import Mentor
from apps.mentor.serializers import *


class MentorListView(generics.ListAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer


class MentorCreateView(generics.CreateAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorCreateSerializer


class MentorRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializerRetrieve


class MentoriaListView(generics.ListCreateAPIView):
    queryset = Mentoria.objects.all()
    serializer_class = MentoriaSerializer


class MentoriaRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mentoria.objects.all()
    serializer_class = MentoriaSerializer