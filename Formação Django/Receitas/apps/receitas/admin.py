from re import T
from tkinter import N
from django.contrib import admin
from .models import Receita


class ListandoReceitas(admin.ModelAdmin):

    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'publicada')
    list_display_links = ('id', 'nome_receita')
    search_fields = ('nome_receita',)
    list_filter = ('categoria','publicada')
    list_editable =  ('publicada',)
    list_per_page = 20


admin.site.register(Receita, ListandoReceitas)

