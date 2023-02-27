from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from Videojocs.models import Plataforma


class Videojocs(View):
    # Definim el mètode HTTP el qual s'ha d'atendre
    def get(self,data ):
        return HttpResponse(content='Això és una prova')

class AddPlataforma(View):
    # Sortirà un formulari amb Jinja on poses les dades de la plataforma i afegeix una plataforma
    def get(self, request,id):
        context = {
            'plataforma' : Plataforma.objects.get(id=id)
        }
        return render(request, 'addplataforma.html', context=context)

class PlataformaRandom(View):
    # Mostra una plataforma aleatoriament
    def get(self, data):
        return HttpResponse(content='La plataforma aleatoria és ' + str(Plataforma.nom))

class PlataformaRandomNou(View):
    # Mostra una plataforma aleatoriament pero que tenen videojocs nous
    def get(self, data):
        return HttpResponse(content='La plataforma aleatoria és ' + str(Plataforma.nom))

class AssociaPlataformaUsuari(View):
    # Associa una plataforma amb un usuari
    def get(self, data):
        return HttpResponse(content='La plataforma aleatoria és ' + str(Plataforma.nom))



