from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from apps.competencia.serializers import *


class CompetenciaListView(generics.ListCreateAPIView):
    queryset = Competencia.objects.all()
    serializer_class = CompetenciaSerializer
    #permission_classes = (IsAuthenticated,)


class CompetenciaRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompetenciaSerializer
    #permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj = get_object_or_404(Competencia, id=self.kwargs['pk'])
        return obj


class CompLogradaListView(generics.ListCreateAPIView):
    queryset = Hoja_Vida.objects.all()
    #permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CompetenciaLogradaSerializer

        return CompetenciaLogradaCreateSerializer


class CompLogradaRUDView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CompetenciaLogradaSerializer

        return CompetenciaLogradaCreateSerializer

    def get_object(self):
        obj = get_object_or_404(Hoja_Vida, id=self.kwargs['pk'])
        return obj


class CompPlanifListCreateView(generics.ListCreateAPIView):
    queryset = CompPlanif.objects.all()
    #permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CompPlanifSerializer

        return CompPlanifCreateSerializer


class CompPlanifRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompPlanifSerializer
    #permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj = get_object_or_404(CompPlanif, id=self.kwargs['pk'])
        return obj


class ReferenteListCreateView(generics.ListCreateAPIView):
    queryset = Referente.objects.all()
    serializer_class = ReferenteSerializer
    #permission_classes = (IsAuthenticated,)


class ReferenteRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReferenteRetrieveSerializer
    #permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj = get_object_or_404(Referente, id=self.kwargs['pk'])
        return obj


class CompRefLCView(generics.ListCreateAPIView):
    queryset = Competencia_Referente.objects.all()
    serializer_class = CompRefSerializer
    # permission_classes = (IsAuthenticated,)


class CompRefRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompRefSerializer
    # permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj = get_object_or_404(Competencia_Referente, id=self.kwargs['pk'])
        return obj
