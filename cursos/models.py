from django.db import models

from datetime import datetime


class Curso(models.Model):

    titulo_curso = models.CharField(max_length=255)
    profesor = models.CharField(max_length=255)
    temario = models.TextField()
    imagen = models.FileField(upload_to="cursos/imagenes",
                              blank=True, null=True)
    creacion_curso = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.titulo_curso


class Tema(models.Model):

    titulo_tema = models.CharField(max_length=255)
    curso_id = models.ForeignKey(Curso, on_delete=models.CASCADE,
                                 null=False, blank=False)
    imagen = models.FileField(upload_to="temas/imagenes",
                              blank=True, null=True)
    creacion_curso = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.titulo_tema


class Documento(models.Model):

    titulo_documento = models.CharField(max_length=255)
    tema_id = models.ForeignKey(Tema, on_delete=models.CASCADE,
                                null=False, blank=False)
    documento = models.FileField(upload_to='pdf/%Y/%m/',
                                 blank=True, null=True)
    created_documento = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.titulo_documento


class Video(models.Model):

    titulo_video = models.CharField(max_length=255)
    tema_id = models.ForeignKey(Tema, on_delete=models.CASCADE,
                                null=False, blank=False)
    video = models.URLField()
    created_video = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.titulo_video
