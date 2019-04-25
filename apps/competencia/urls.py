from django.urls import path
from .views import *

app_name = "Competencia"
urlpatterns = [
    path("",
         view=CompetenciaListView.as_view(),
         name="listar competencias"
         ),
    path("<int:pk>/",
         view=CompetenciaRUDView.as_view(),
         name="obtener editar y eliminar competencia"
         ),
    path(
        "hoja_vida/",
        view=CompLogradaListView.as_view(),
        name="listar y crear competencias logradas"
    ),
    path(
        "hoja_vida/<int:pk>/",
        view=CompLogradaRUDView.as_view(),
        name="obtener editar y eliminar competencia ligrada"
    ),
    path(
        "compplanif/",
        view=CompPlanifListCreateView.as_view(),
        name="listar y crear competencia planificada"
    ),
    path(
        "compplanif/<int:pk>/",
        view=CompPlanifRUDView.as_view(),
        name="obtener editar y eliminar competencia planificada"
    ),
    path(
        "referente/",
        view=ReferenteListCreateView.as_view(),
        name="listar y crear referente"
    ),
    path(
        "referente/<int:pk>",
        view=ReferenteRUDView.as_view(),
        name="obtener editar y eliminar referente"
    ),
    path(
        "competencia_referente/",
        view=CompRefLCView.as_view(),
        name="listar y crear"
    ),
    path(
        "competencia_referente/<int:pk>/",
        view=CompRefRUDView.as_view(),
        name="RUD"
    )
]