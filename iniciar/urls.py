from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from datetime import datetime

from iniciar import models
from .views import RegisterView

app_name = "iniciar"

urlpatterns = [

    path('login/', LoginView.as_view(template_name='iniciar/login.html',
                                     authentication_form=models.BootstrapAuthenticationForm,
                                     extra_context={'title': 'Iniciar seción', 'year': datetime.now().year
                                                    }), name='login'
         ),

    path('logout/', LogoutView.as_view(next_page='/'), name='logout'
         ),

    path('register/', RegisterView.as_view(extra_context={'title': 'Registro',
                                                          'year': datetime.now().year,
                                                          }), name='register'
         ),
]
