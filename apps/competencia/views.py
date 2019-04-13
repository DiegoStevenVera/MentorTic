from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from apps.competencia.serializers import *


class CompetenciaListView(generics.ListCreateAPIView):
    queryset = Competencia.objects.all()
    serializer_class = CompetenciaSerializer
    permission_classes = (IsAuthenticated,)


class CompetenciaRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competencia.objects.all()
    serializer_class = CompetenciaSerializer
    permission_classes = (IsAuthenticated,)


class CompLogradaListView(generics.ListCreateAPIView):
    queryset = CompLograda.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CompetenciaLogradaSerializer

        return CompetenciaLogradaCreateSerializer


class CompLogradaRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompLograda.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CompetenciaLogradaSerializer

        return CompetenciaLogradaCreateSerializer


class CompPlanifListCreateView(generics.ListCreateAPIView):
    queryset = CompPlanif.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CompPlanifSerializer

        return CompPlanifCreateSerializer


class CompPlanifRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompPlanif.objects.all()
    serializer_class = CompPlanifSerializer
    permission_classes = (IsAuthenticated,)


class ReferenteListCreateView(generics.ListCreateAPIView):
    queryset = Referente.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReferenteSerializer

        return ReferenteCreateSerializer


class ReferenteRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Referente.objects.all()
    serializer_class = ReferenteSerializer
    permission_classes = (IsAuthenticated,)
