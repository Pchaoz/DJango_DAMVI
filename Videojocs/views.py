from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View

from Videojocs.models import Plataforma, Videojoc


class Videojocs(View):
    # Definim el mètode HTTP el qual s'ha d'atendre
    def get(self,data ):
        return HttpResponse(content='Això és una prova')

class AfegirDades(View):
    def get(self, data):
        # Usuaris creats
        Usuari1 = User.objects.create_user(username="exemple", password="exemple", email="exemple@test.com")
        # Per crear superusuari: python manage.py createsuperuser

        # Plataformes creades
        Plataforma1 = Plataforma.objects.create(nom="Gameflix")
        Plataforma1.usuaris.add(Usuari1)
        Plataforma2 = Plataforma.objects.create(nom="Steam")
        Plataforma2.usuaris.add(Usuari1)
        Plataforma3 = Plataforma.objects.create(nom="Epic")
        Plataforma3.usuaris.add(Usuari1)

        # Videojocs creats
        Videojoc1 = Videojoc.objects.create(nom="Crash Bandicoot", preu=33, nou=False, plataforma=Plataforma2)
        Videojoc2 = Videojoc.objects.create(nom="Valorant", preu=10, nou=True, plataforma=Plataforma3)
        Videojoc3 = Videojoc.objects.create(nom="Sanic", preu=20, nou=False, plataforma=Plataforma1)

        return HttpResponse("Creant les dades. Comprova la bbdd.")

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

class PlataformesUsuari(View):
    # Mostra les plataformes d' un usuari concret en una vista Jinja
    def get(self, data):
        return HttpResponse(content='La plataforma aleatoria és ' + str(Plataforma.nom))

class PlataformaRandomUsuari(View):
    # Mostra una plataforma random d' un usuari
    def get(self, data):
        return HttpResponse(content='La plataforma aleatoria és ' + str(Plataforma.nom))

class AfegirJocPlataforma(View):
    # Afegeix un joc a una plataforma especifica en una vista amb Jinja mitjançant un formulari
    def get(self, request, id):
        context = {
            'plataforma': Plataforma.objects.get(id=id)
        }
        return render(request, 'addplataforma.html', context=context)

class AssociarVideojocUsuari(View):
    #Associa un videojoc amb un usuari
    def get(self, data):
        return HttpResponse(content='La plataforma aleatoria és ' + str(Plataforma.nom))

class EliminaVideojoc(View):
    # Treu un videojoc proporcionat a un usuari proporcionat
    def get(self, data):
        return HttpResponse(content='La plataforma aleatoria és ' + str(Plataforma.nom))

# No hi ha class per afegir videojoc per que els videojocs s' afegeixen desde /Admin
