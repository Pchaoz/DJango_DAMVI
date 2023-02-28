from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View
from pymysql import IntegrityError

#from pymongo.auth import authenticate

from Videojocs.models import Plataforma, Videojoc


class Videojocs(View):
    # Definim el mètode HTTP el qual s'ha d'atendre
    def get(self,data ):
        return redirect('login')

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
        Videojoc1.usuaris.add(Usuari1)
        Videojoc2 = Videojoc.objects.create(nom="Valorant", preu=10, nou=True, plataforma=Plataforma3)
        Videojoc2.usuaris.add(Usuari1)
        Videojoc3 = Videojoc.objects.create(nom="Sanic", preu=20, nou=False, plataforma=Plataforma1)
        Videojoc3.usuaris.add(Usuari1)

        return HttpResponse("Creant les dades. Comprova la bbdd.")

#FET
class LoginView(View):
    # un login
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        # Treiem les dades d' autenticacio del formulari i les passem a una variable. El password l' encripta automaticament per l' authenticate
        usuari = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        # Comprovem si existeix l' usuari
        if usuari is not None:
            # Login ens obre directament una sessió amb aquest usuari
            login(request, usuari)
            return HttpResponse(content='Sessió iniciada correctament.')
        return self.get(request)

#FET
class LogoutView(View):
    # Si el usuari es troba logat el desloga amb logout i et torna a la web de login
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('login')


#FET
class AddPlataforma(View):
    # Sortirà un formulari amb Jinja on poses les dades de la plataforma i afegeix una plataforma
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'addplataforma.html')
        else:
            return redirect('login')
    def post(self, request):
        try:
            PlataformaCreada, ComprovarPlataforma = Plataforma.objects.get_or_create(nom=request.POST.get('nom'))
            if ComprovarPlataforma:
                PlataformaCreada.save()
                return HttpResponse(content='Plataforma creada correctament')
            else:
                return HttpResponse(content='Ja existeix aquesta plataforma')
        except IntegrityError:
            raise Http404("Hi ha hagut un error al crear la plataforma.")

#FET
class AssociaPlataformaUsuari(View):
    # Associa una plataforma amb un usuari
    def get(self, request, idplataforma, idusuari):
        if request.user.is_authenticated:
            try:
                PlataformaAssociar = Plataforma.objects.get(id=idplataforma)
                UsuariAssociar = User.objects.get(id=idusuari)
                if PlataformaAssociar is not None and UsuariAssociar is not None:
                    PlataformaAssociar.usuaris.add(UsuariAssociar)
                    return HttpResponse(content='Usuari afegit a la plataforma.')
                else:
                    return HttpResponse(content='El usuari o la plataforma no existeixen.')
            except Plataforma.DoesNotExist or User.DoesNotExist:
                raise Http404("El usuari o la plataforma no existeixen.")
        else:
            return redirect('login')

#FET
class PlataformesUsuari(View):
    # Mostra les plataformes d' un usuari concret en una vista Jinja
    def get(self, request, nom):
        if request.user.is_authenticated:
            context = {
                    'plataformes': list(Plataforma.objects.all().filter(usuaris__username__contains = nom))
            }
            return render(request, 'plataformesde.html', context=context)
        else:
            return redirect('login')



#FET
class AfegirJocPlataforma(View):
    # Afegeix un joc a una plataforma especifica en una vista amb Jinja mitjançant un formulari
    def get(self, request, idplataforma):
        if request.user.is_authenticated:
            context = {
                'plataforma': Plataforma.objects.get(id=idplataforma)
            }
            return render(request, 'addvideojocplataforma.html', context=context)
        else:
            return redirect('login')
    def post(self, request, idplataforma):
        try:
            VideojocAfegir = Videojoc.objects.get(nom=request.POST.get('videojoc'))
            PlataformaAfegir = Plataforma.objects.get(id=idplataforma)
            if VideojocAfegir is not None and PlataformaAfegir is not None:
                VideojocAfegir.plataforma = PlataformaAfegir
                VideojocAfegir.save()
                return HttpResponse(content='Videojoc afegit a la plataforma')
            else:
                return HttpResponse(content='La plataforma o el Videojoc no existeixen.')
        except IntegrityError:
            raise Http404("Hi ha hagut un error al crear la plataforma.")
#FET
class AssociarVideojocUsuari(View):
    #Associa un videojoc amb un usuari
    def get(self, request, idvideojoc, idusuari):
        if request.user.is_authenticated:
            try:
                VideojocAssociar = Videojoc.objects.get(id=idvideojoc)
                UsuariAssociar = User.objects.get(id=idusuari)
                if VideojocAssociar is not None and UsuariAssociar is not None:
                    VideojocAssociar.usuaris.add(UsuariAssociar)
                    return HttpResponse(content='Usuari ara té el videojoc indicat.')
                else:
                    return HttpResponse(content='El usuari o el videojoc no existeixen.')
            except Plataforma.DoesNotExist or User.DoesNotExist:
                raise Http404("El usuari o el videojoc no existeixen.")
        else:
            return redirect('login')
#FET
class EliminaVideojoc(View):
    # Treu un videojoc proporcionat a un usuari proporcionat
    def get(self, request, idvideojoc, idusuari):
        if request.user.is_authenticated:
            try:
                VideojocEliminar = Videojoc.objects.get(id=idvideojoc)
                Usuari = User.objects.get(id=idusuari)
                if VideojocEliminar is not None and Usuari is not None:
                    VideojocEliminar.usuaris.remove(Usuari)
                    return HttpResponse(content='El usuari ja no té el videojoc indicat.')
                else:
                    return HttpResponse(content='El usuari o el videojoc no existeixen.')
            except Plataforma.DoesNotExist or User.DoesNotExist:
                raise Http404("El usuari o el videojoc no existeixen.")
        else:
            return redirect('login')

# No hi ha class per afegir videojoc per que els videojocs s' afegeixen desde /Admin




