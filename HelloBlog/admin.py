from django.contrib import admin
from .models import Publicacao, Perfil

# admin.site.register(Publicacao)

@admin.register(Publicacao)
class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor']


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    pass
