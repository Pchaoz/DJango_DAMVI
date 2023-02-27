"""DJango_DAMVI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Videojocs.views import Videojocs, AddPlataforma, PlataformaRandom, PlataformaRandomNou, AssociaPlataformaUsuari, \
    PlataformesUsuari, PlataformaRandomUsuari, AfegirJocPlataforma, AssociarVideojocUsuari, EliminaVideojoc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Videojocs.as_view()),
    path('addPlataforma/', AddPlataforma.as_view()),
    path('plataformaRandom/', PlataformaRandom.as_view()),
    path('plataformaRandomNou/', PlataformaRandomNou.as_view()),
    path('plataforma/<int:idplataforma>/<int:idusuari>/', AssociaPlataformaUsuari.as_view()),
    path('PlataformesDe/<Nom>/', PlataformesUsuari.as_view()),
    path('PlataformaDe/<Nom>/', PlataformaRandomUsuari.as_view()),
    path('addVideojoc/<int:idplataforma>/', AfegirJocPlataforma.as_view()),
    path('videojoc/<int:idvideojoc>/<int:idusuari>/', AssociarVideojocUsuari.as_view()),
    path('removeVideojoc/<int:idvideojoc>/<int:idusuari>/', EliminaVideojoc.as_view())
]
