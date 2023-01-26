from rest_framework.viewsets import ModelViewSet
from reservas.models import Cuarto, Reservacion, Cliente
from reservas.serializers import ReservacionSerializer, CuartoSerializer, ClienteSerializer
from rest_framework import filters, generics


class ReservacionApiViewSet(ModelViewSet):
    serializer_class = ReservacionSerializer
    queryset = Reservacion.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['cliente']

class CuartoApiViewSet(ModelViewSet):
    serializer_class = CuartoSerializer
    queryset = Cuarto.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['numero']

class ClienteApiViewSet(ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre']


class ClienteCreateView(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ReservacionCreateView(generics.CreateAPIView):
    queryset = Reservacion.objects.all()
    serializer_class = ReservacionSerializer