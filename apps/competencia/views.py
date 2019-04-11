from rest_framework import generics

from apps.competencia.serializers import *


class CompetenciaListView(generics.ListCreateAPIView):
    queryset = Competencia.objects.all()
    serializer_class = CompetenciaSerializer


class CompetenciaRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competencia.objects.all()
    serializer_class = CompetenciaSerializer


class CompLogradaListView(generics.ListCreateAPIView):
    queryset = CompLograda.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CompetenciaLogradaSerializer

        return CompetenciaLogradaCreateSerializer


class CompLogradaRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompLograda.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CompetenciaLogradaSerializer

        return CompetenciaLogradaCreateSerializer


class CompPlanifListCreateView(generics.ListCreateAPIView):
    queryset = CompPlanif.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CompPlanifSerializer

        return CompPlanifCreateSerializer


class CompPlanifRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompPlanif.objects.all()
    serializer_class = CompPlanifSerializer


class ReferenteListCreateView(generics.ListCreateAPIView):
    queryset = Referente.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReferenteSerializer

        return ReferenteCreateSerializer


class ReferenteRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Referente.objects.all()
    serializer_class = ReferenteSerializer
