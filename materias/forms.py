from django import forms
from .models import Curso


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'creditos', 'nivel', 'horas_semana', 'jornada', 'docente', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Desarrollo de Aplicaciones Web'}),
            'creditos': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'nivel': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Quinto Nivel'}),
            'horas_semana': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'jornada': forms.Select(attrs={'class': 'form-select'}),
            'docente': forms.Select(attrs={'class': 'form-select'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }