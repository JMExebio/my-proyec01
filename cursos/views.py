from django.shortcuts import render
from django.views.generic import TemplateView

from datetime import datetime

from .models import Curso


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
