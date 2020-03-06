from django.db import models

from datetime import datetime


class Curso(models.Model):
    titulo = models.CharField(
        max_length=255
    )
    profesor = models.CharField(
        max_length=255,
    )
    temario = models.TextField(
    )
    imagen = models.FileField(
        upload_to="cursos/imagenes",
        blank=True,
        null=True
    )
    creacion_curso = models.DateTimeField(
        default=datetime.now
    )

    def __str__(self):
        return self.titulo
