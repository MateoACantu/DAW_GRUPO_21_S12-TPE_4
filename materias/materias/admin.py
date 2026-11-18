from django.contrib import admin
from .models import Curso


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'docente', 'nivel', 'creditos', 'horas_semana', 'jornada')
    list_filter = ('jornada', 'nivel', 'docente')
    search_fields = ('nombre',)