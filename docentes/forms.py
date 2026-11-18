from django import forms

from .models import Docente


class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ["nombre", "apellido", "correo", "cedula",
                  "tipo_sangre", "direccion", "imagen"]
        labels = {"tipo_sangre": "Tipo de sangre", "direccion": "Dirección",
                  "cedula": "Cédula"}
