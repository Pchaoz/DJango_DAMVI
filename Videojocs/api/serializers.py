from rest_framework import serializers
from Videojocs.models import Plataforma

class PlataformaSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    class Meta:
        model = Plataforma
        fields = '__all__'