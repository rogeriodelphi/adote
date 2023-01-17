from django.contrib import admin
from .models import Raca, Tag, Pet


@admin.register(Raca)
class RacaAdmin(admin.ModelAdmin):
    list_display = ('id', 'raca')
    search_fields = ['raca']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')
    search_fields = ['tag']
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'foto', 'cidade', 'estado', 'telefone', 'raca', 'status')
    search_fields = ('cidade', 'raca')
    list_filter = ['status', 'cidade']
