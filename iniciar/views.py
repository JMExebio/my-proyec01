from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy

from django.contrib.auth.models import User

from datetime import datetime

from .forms import RegistroForm


class RegisterView(CreateView):
    model = User
    template_name = "iniciar/register.html"
    form_class = RegistroForm
    success_url = reverse_lazy('cursos:cursos')
