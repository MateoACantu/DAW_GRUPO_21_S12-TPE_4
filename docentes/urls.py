from django.urls import path

from . import views

urlpatterns = [
    path("", views.lista_docentes, name="lista_docentes"),
    path("nuevo/", views.crear_docente, name="crear_docente"),
    path("<int:pk>/editar/", views.editar_docente, name="editar_docente"),
    path("<int:pk>/eliminar/", views.eliminar_docente, name="eliminar_docente"),
]
