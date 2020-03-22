from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import Cursosviews, Inicioviews, Temasviews, TemasCursoviews, ClasesTemaviews

app_name = "cursos"

urlpatterns = [
    path('', Inicioviews.as_view(), name='inicio'),
    path('cursos/', login_required(Cursosviews.as_view()), name='cursos'),
    path('temas/', login_required(Temasviews.as_view()), name='temas'),
    path('<int:curso_id>/<curso_nombre>',
         login_required(TemasCursoviews.as_view()), name='temascurso'),
    path('clases/<int:tema_id>/<tema_nombre>',
         login_required(ClasesTemaviews.as_view()), name='clasestema'),
]
