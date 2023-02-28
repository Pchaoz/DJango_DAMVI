from random import random, randint

from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Videojocs.api.serializers import PlataformaSerializer
from Videojocs.models import Plataforma


class PlataformaRandom(APIView):
    # Mostra una plataforma aleatoriament
    def get(self, request):
        if request.user.is_authenticated:
            Plataformes = Plataforma.objects.all()
            NumeroAleatori = randint(0, len(Plataformes)-1)
            PlataformaEscollida = PlataformaSerializer(Plataformes[NumeroAleatori])
            return Response(data=PlataformaEscollida.data, status=status.HTTP_200_OK)
        else:
            return redirect('login')

class PlataformaRandomNou(APIView):
    # Mostra una plataforma aleatoriament pero que tenen videojocs nous
    def get(self, request):
        if request.user.is_authenticated:
            Plataformes = Plataforma.objects.all().filter(videojoc__nou = True)
            NumeroAleatori = randint(0, len(Plataformes) - 1)
            PlataformaEscollida = PlataformaSerializer(Plataformes[NumeroAleatori])
            return Response(data=PlataformaEscollida.data, status=status.HTTP_200_OK)
        else:
            return redirect('login')

class PlataformaRandomUsuari(APIView):
    # Mostra una plataforma random d' un usuari
    def get(self, request, nom):
        if request.user.is_authenticated:
            Plataformes = Plataforma.objects.all().filter(usuaris__username=nom)
            NumeroAleatori = randint(0, len(Plataformes) - 1)
            PlataformaEscollida = PlataformaSerializer(Plataformes[NumeroAleatori])
            return Response(data=PlataformaEscollida.data, status=status.HTTP_200_OK)
        else:
            return redirect('login')