import datetime

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Plataforma(models.Model):
    nom = models.CharField(max_lenght=30, null=False, default="")
    afegit=models.DateField(default=datetime.date.now())
    usuaris = models.ManyToManyField(User)

class Videojoc(models.Model):
    nom = models.CharField(max_lenght=30,null=False,default="")
    preu=models.FloatField(null=False, default=0)
    nou=models.BooleanField(null=False,default=False)
    plataforma= models.ForeignKey(Plataforma, on_delete=models.CASCADE)









