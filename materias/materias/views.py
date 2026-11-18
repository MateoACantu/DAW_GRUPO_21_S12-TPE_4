from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Curso
from .forms import CursoForm


def listar_cursos(request):
    cursos = Curso.objects.select_related('docente').all()
    return render(request, 'materias/listar_cursos.html', {'cursos': cursos})


def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso agregado exitosamente.')
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'materias/form_curso.html', {'form': form, 'titulo': 'Agregar curso'})


def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Curso actualizado correctamente.')
            return redirect('listar_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'materias/form_curso.html', {'form': form, 'titulo': 'Editar curso'})


def eliminar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    if request.method == 'POST':
        curso.delete()
        messages.success(request, 'Curso eliminado correctamente.')
        return redirect('listar_cursos')
    return render(request, 'materias/eliminar_curso.html', {'curso': curso})