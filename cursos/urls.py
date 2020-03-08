from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import Cursosviews, Inicioviews

app_name = "cursos"

urlpatterns = [
    path('', Inicioviews.as_view(), name='inicio'),
    path('cursos/', login_required(Cursosviews.as_view()), name='cursos'),
]
