from django.db import models
from rest_framework import status
from rest_framework.response import Response

class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    Dni = models.IntegerField()
    class Meta:
        verbose_name='Cliente'
        verbose_name_plural='Clientes'

    def __str__(self):
        return self.Nombre


class Cuarto(models.Model):
    class disponibilidad(models.TextChoices):
        SI = 'si'
        NO = 'No'
        
    numero = models.IntegerField()
    capacidad_de_personas = models.IntegerField()
    cantidad_de_camas = models.IntegerField()
    jacuzzi = models.CharField(choices=disponibilidad.choices, max_length=2)
    precio_x_dia = models.IntegerField()
    ocupado = models.CharField(choices=disponibilidad.choices, max_length=2, default=disponibilidad.NO)
    
    class Meta:
        verbose_name='Cuarto'
        verbose_name_plural='Cuartos'

    def __str__(self):
        return str(self.numero)


class Reservacion(models.Model):
    class Status(models.TextChoices):
        PENDIENTE = 'Pendiente'
        PAGADO = 'Pagado'
        ELIMINADO = 'Eliminado'
   
    cuarto = models.ForeignKey(Cuarto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_entrada = models.DateField()
    fecha_salida = models.DateField()
    metodo_de_pago = models.CharField(max_length=20)
    monto_pagado = models.IntegerField(editable=False)
    días_de_estadia = models.IntegerField(editable=False, default=0)
    estado = models.CharField(choices=Status.choices, max_length=20)

    def save(self, *args, **kwargs):
        try:
            reserva_anterior = Reservacion.objects.filter(cuarto=self.cuarto).exclude(id=self.id)
            for reserva in reserva_anterior:
                if (self.fecha_entrada <= reserva.fecha_salida and self.fecha_salida >= reserva.fecha_entrada):
                    raise ValueError("Cuarto no disponible para reservar")
            self.monto_pagado = (self.fecha_salida - self.fecha_entrada).days * self.cuarto.precio_x_dia
            self.días_de_estadia = (self.fecha_salida - self.fecha_entrada).days
            super(Reservacion, self).save(*args, **kwargs)
            self.cuarto.ocupado = "si"
            self.cuarto.save()
        except ValueError as e:
            print(e)
            return Response({"error": "No se pudo reservar, cuarto ocupado."}, status=status.HTTP_400_BAD_REQUEST)


    class Meta:
        verbose_name='Reserva'
        verbose_name_plural='Reservas'

    def __str__(self):
        return str(self.cuarto)


 