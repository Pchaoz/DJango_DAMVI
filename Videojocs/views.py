from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
class Videojocs(View):
    # Definim el mètode HTTP el qual s'ha d'atendre
    def get(self,data ):
        return HttpResponse(content='Això és una prova')
