from .models import Reservacion, Cuarto, Cliente
from django.contrib import admin

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'Nombre', 'Apellido', 'Dni',)
    ordering = ('id',)
    search_fields = ('nombre',)

class CuartoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'capacidad_de_personas','cantidad_de_camas','jacuzzi','precio_x_dia','ocupado',)
    ordering = ('numero',)
    search_fields = ('numero', 'capacidad_de_personas','precio_x_dia',)
    list_filter = ('capacidad_de_personas',)

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('cuarto', 'cliente','fecha_entrada','fecha_salida', 'días_de_estadia', 'metodo_de_pago', 'monto_pagado', 'estado')
    ordering = ('cuarto',)
    search_fields = ('cuarto', 'cliente', 'estado')
    list_filter = ('estado',)

admin.site.site_header = "Reservas Hotel"
admin.site.register(Reservacion, ReservaAdmin)
admin.site.register(Cuarto, CuartoAdmin)
admin.site.register(Cliente, ClienteAdmin)

