from django.contrib import admin

from .models import PedidoAdocao

@admin.register(PedidoAdocao)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pet', 'usuario', 'data', 'status')
    search_fields = ['usuario', 'status']
    list_filter = ['status']