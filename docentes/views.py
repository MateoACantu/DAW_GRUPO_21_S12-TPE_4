from django.shortcuts import get_object_or_404, redirect, render

from .forms import DocenteForm
from .models import Docente


def lista_docentes(request):
    docentes = Docente.objects.all().order_by("apellido", "nombre")
    return render(request, "docentes/lista.html", {"docentes": docentes})


def crear_docente(request):
    form = DocenteForm(request.POST or None, request.FILES or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("lista_docentes")
    return render(request, "docentes/formulario.html",
                  {"form": form, "titulo": "Agregar docente"})


def editar_docente(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    form = DocenteForm(request.POST or None, request.FILES or None, instance=docente)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("lista_docentes")
    return render(request, "docentes/formulario.html",
                  {"form": form, "titulo": "Editar docente"})


def eliminar_docente(request, pk):
    docente = get_object_or_404(Docente, pk=pk)
    if request.method == "POST":
        docente.delete()
        return redirect("lista_docentes")
    return render(request, "docentes/confirmar_eliminar.html", {"docente": docente})
