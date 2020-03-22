from django.shortcuts import render
from django.views.generic import TemplateView

from datetime import datetime

from .models import Curso, Tema, Video, Documento


class Inicioviews(TemplateView):
    template_name = "cursos/index.html"

    def get_context_data(self):
        cursos = Curso.objects.all()
        return {
            'title': 'Inicio',
            'year': datetime.now().year,
            'cursos': cursos,
        }


class Cursosviews(TemplateView):
    template_name = 'cursos/courses.html'

    def get_context_data(self):
        cursos = Curso.objects.all()
        return {
            'title': 'Cursos',
            'year': datetime.now().year,
            'cursos': cursos,
        }


class Temasviews(TemplateView):
    template_name = "cursos/themes.html"

    def get_context_data(self, **kwargs):
        temas = Tema.objects.all()
        return {'temas': temas}


class TemasCursoviews(TemplateView):
    template_name = "cursos/themes.html"

    def get_context_data(self, **kwargs):
        curso_id = kwargs['curso_id']
        curso_titulo = kwargs['curso_nombre']
        temas = Tema.objects.filter(curso_id=curso_id)

        return {'temas': temas, 'curso_titulo': curso_titulo}


class ClasesTemaviews(TemplateView):
    template_name = "cursos/class.html"

    def get_context_data(self, **kwargs):
        tema_id = kwargs['tema_id']
        tema_titulo = kwargs['tema_nombre']

        videos = Video.objects.filter(tema_id=tema_id)
        documentos = Documento.objects.filter(tema_id=tema_id)

        return {'tema_titulo': tema_titulo, 'videos': videos, 'documentos': documentos}
