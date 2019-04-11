from django.shortcuts import render

from rest_framework import generics

from apps.competencia.serializers import *


class CompetenciaListView(generics.ListCreateAPIView):
    queryset = Competencia.objects.all()
    serializer_class = CompetenciaSerializer


class CompetenciaRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competencia.objects.all()
    serializer_class = CompetenciaSerializer