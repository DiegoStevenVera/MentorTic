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
    )
]