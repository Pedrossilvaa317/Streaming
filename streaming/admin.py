from django.contrib import admin
from .models import Filmes, Generos, Plataformas

@admin.register(Filmes)
class FilmesAdmin(admin.ModelAdmin):
    list_display = ('filme', 'genero', 'ano_lancamento')
    search_fields = ('filme',)
    list_filter = ('genero', 'plataformas')

@admin.register(Generos)
class GenerosAdmin(admin.ModelAdmin):
    list_display = ('genero',)

@admin.register(Plataformas)
class PlataformasAdmin(admin.ModelAdmin):
    list_display = ('nome', 'site')
