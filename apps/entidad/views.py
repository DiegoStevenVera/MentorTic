from rest_framework import generics

from apps.entidad.models import Entidad
from apps.entidad.serializers import EntidadSerializer


class EntidadListCreateView(generics.ListCreateAPIView):
    queryset = Entidad.objects.all()
    serializer_class = EntidadSerializer


class EntidadRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entidad.objects.all()
    serializer_class = EntidadSerializer