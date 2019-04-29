from django.urls import path
from .views import *

app_name = "Entidad"
urlpatterns = [
    path(
        "",
        view=EntidadListCreateView.as_view(),
        name="listar y crear entidad"
    ),
    path(
        "<int:pk>/",
        view=EntidadRUDView.as_view(),
        name="obtener editar y eliminar entidad"
    ),
    path(
        "representantes/",
        view=RepresentanteListCreateView.as_view(),
        name="listar y crear representante"
    ),
    path(
        "representantes/<int:pk>/",
        view=RepresentanteRUDView.as_view(),
        name="obtener editar y eliminar representante"
    ),
    path(
        "aprendiz/",
        view=EntidadAPrendices.as_view(),
        name="obtener entidades con aprendices"
    )
]