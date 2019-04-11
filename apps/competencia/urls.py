from django.urls import path
from .views import *

app_name = "Competencia"
urlpatterns = [
    path("", view=CompetenciaListView.as_view(), name="listar competencias"),
    path("<int:pk>/", view=CompetenciaRUDView.as_view(), name="obtener editar y eliminar competencia"),
]