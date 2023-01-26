from rest_framework.routers import DefaultRouter
from reservas.views import ReservacionApiViewSet, CuartoApiViewSet, ClienteApiViewSet

router = DefaultRouter()

router.register(prefix = 'Clientes', basename='Clientes', viewset=ClienteApiViewSet)   
router.register(prefix = 'Cuartos', basename='Cuartos', viewset=CuartoApiViewSet)
router.register(prefix = 'ReservasHotel', basename='ReservasHotel', viewset=ReservacionApiViewSet)


