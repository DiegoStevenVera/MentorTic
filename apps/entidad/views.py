from docutils.parsers import null
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from apps.entidad.models import Entidad, Representante
from apps.entidad.serializers import EntidadSerializer, RepresentanteSerializer, EntidadRetrieveSerializer


class EntidadListCreateView(generics.ListCreateAPIView):
    queryset = Entidad.objects.all()
    #permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EntidadRetrieveSerializer

        return EntidadSerializer


class EntidadRUDView(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj = get_object_or_404(Entidad, id=self.kwargs['pk'])
        return obj

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return EntidadRetrieveSerializer

        return EntidadSerializer


class EntidadAPrendices(generics.ListAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = EntidadRetrieveSerializer

    def get_queryset(self):
        objs = Entidad.objects.filter(Mentores__isnull=False, Mentores__tipo="Aprendiz")
        return objs


class RepresentanteListCreateView(generics.ListCreateAPIView):
    queryset = Representante.objects.all()
    serializer_class = RepresentanteSerializer
    #permission_classes = (IsAuthenticated,)


class RepresentanteRUDView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RepresentanteSerializer
    #permission_classes = (IsAuthenticated,)

    def get_object(self):
        obj = get_object_or_404(Representante, id=self.kwargs['pk'])
        return obj
