from django.urls import path
from .views import *

app_name = "Mentor"
urlpatterns = [
    path("", view=MentorListView.as_view(), name="listar mentores"),
    path("create/", view=MentorCreateView.as_view(), name="Crear mentor"),
    path("<int:pk>/", view=MentorRUDView.as_view(), name="Obtener, actualizar y eliminar mentor"),
    path("mentoria/", view=MentoriaListView.as_view(), name="listar y crear mentorias"),
    path("mentoria/<int:pk>/", view=MentoriaRUDView.as_view(), name="Obtener, actualizar y eliminar mentoria")
]