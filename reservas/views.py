from rest_framework.viewsets import ModelViewSet
from reservas.models import Cuarto, Reservacion, Cliente
from reservas.serializers import ReservacionSerializer, CuartoSerializer, ClienteSerializer
from rest_framework import filters, generics

"""Views de Cliente"""
class ClienteApiViewSet(ModelViewSet):
    serializer_class = ClienteSerializer
    queryset = Cliente.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre']

class ClienteCreateView(generics.CreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteUpdateView(generics.UpdateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteDeleteView(generics.DestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

"""Views de Reservación"""
class ReservacionApiViewSet(ModelViewSet):
    serializer_class = ReservacionSerializer
    queryset = Reservacion.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['cliente']

class ReservacionCreateView(generics.CreateAPIView):
    queryset = Reservacion.objects.all()
    serializer_class = ReservacionSerializer

class ReservacionUpdateView(generics.UpdateAPIView):
    queryset = Reservacion.objects.all()
    lookup_field = 'cliente'
    serializer_class = ReservacionSerializer

class ReservacionDeleteView(generics.DestroyAPIView):
    queryset = Reservacion.objects.all()
    lookup_field = 'cliente'
    serializer_class = ReservacionSerializer


"""Views de cuarto"""
class CuartoApiViewSet(ModelViewSet):
    serializer_class = CuartoSerializer
    queryset = Cuarto.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['numero']

class CuartoCreateView(generics.CreateAPIView):
    queryset = Cuarto.objects.all()
    serializer_class = CuartoSerializer

class CuartoUpdateView(generics.UpdateAPIView):
    queryset = Cuarto.objects.all()
    lookup_field = 'numero'
    serializer_class = CuartoSerializer

class CuartoDeleteView(generics.DestroyAPIView):
    queryset = Cuarto.objects.all()
    lookup_field = 'numero'
    serializer_class = CuartoSerializer



