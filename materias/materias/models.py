from django.db import models
from docentes.models import Docente


class Curso(models.Model):
    JORNADA_CHOICES = [
        ('Matutina', 'Matutina'),
        ('Vespertina', 'Vespertina'),
        ('Nocturna', 'Nocturna'),
    ]

    nombre = models.CharField(max_length=100, verbose_name='Nombre del curso')
    creditos = models.PositiveIntegerField(verbose_name='Número de créditos')
    nivel = models.CharField(max_length=50, verbose_name='Nivel')
    horas_semana = models.PositiveIntegerField(verbose_name='Horas de clase a la semana')
    jornada = models.CharField(max_length=20, choices=JORNADA_CHOICES, verbose_name='Jornada')
    imagen = models.ImageField(upload_to='cursos/', null=True, blank=True, verbose_name='Imagen')
    docente = models.ForeignKey(
        Docente,
        on_delete=models.CASCADE,
        related_name='cursos',
        verbose_name='Docente'
    )

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'

    def __str__(self):
        return f"{self.nombre} ({self.nivel})"