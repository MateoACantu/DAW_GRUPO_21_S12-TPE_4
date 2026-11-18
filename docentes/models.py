from django.core.validators import RegexValidator
from django.db import models


class Docente(models.Model):
    TIPOS_SANGRE = [
        ("O+", "O+"), ("O-", "O-"),
        ("A+", "A+"), ("A-", "A-"),
        ("B+", "B+"), ("B-", "B-"),
        ("AB+", "AB+"), ("AB-", "AB-"),
    ]

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    cedula = models.CharField(
        max_length=10,
        unique=True,
        validators=[RegexValidator(r"^\d{10}$", "La cédula debe tener 10 dígitos.")],
    )
    tipo_sangre = models.CharField(max_length=3, choices=TIPOS_SANGRE)
    direccion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to="docentes/")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
