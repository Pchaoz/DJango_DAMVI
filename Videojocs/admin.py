from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from Videojocs.models import Videojoc, Plataforma


class VideojocAdmin(ModelAdmin):
    pass

class PlataformaAdmin(ModelAdmin):
    pass

admin.site.register(Videojoc, ModelAdmin)
admin.site.register(Plataforma, ModelAdmin)
