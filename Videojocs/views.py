from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
class Videojocs(View):
    # Definim el mètode HTTP el qual s'ha d'atendre
    def get(self,data ):
        return HttpResponse(content='Això és una prova')


class getUser(View):
    def get(self, request, id):
        context = {
            'Usuari' : User.objects.get(id=id)
        }
        return HttpResponse (context);

class allUsers(View):
    def get(self, request):
        context = {
            'Usuari' : list(User.objects.all())
        }
        return render(request, 'test.html', context=context)

