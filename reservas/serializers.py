from rest_framework.serializers import ModelSerializer
from reservas.models import Cuarto, Reservacion, Cliente

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id','Nombre', 'Apellido','Dni',)

class CuartoSerializer(ModelSerializer):
    class Meta:
        model = Cuarto
        fields = ('numero', 'capacidad_de_personas','cantidad_de_camas','jacuzzi','precio_x_dia','ocupado',)

class ReservacionSerializer(ModelSerializer):
    class Meta:
        model = Reservacion
        fields = ('cuarto', 'cliente','fecha_entrada','fecha_salida', 'días_de_estadia', 'metodo_de_pago', 'monto_pagado', 'estado')



