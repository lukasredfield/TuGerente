"""ReservasHotel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from reservas.router import router
from django.urls import path
from reservas.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('clientes/', ClienteCreateView.as_view(), name='cliente-create'),
    path('clientes/update/<int:pk>', ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/delete/<int:pk>', ClienteDeleteView.as_view(), name='cliente-delete'),
    path('cuartos/', CuartoCreateView.as_view(), name='cuarto-create'),
    path('cuartos/<int:numero>', CuartoApiViewSet.as_view({"get": "retrieve"}), name='cuarto-ver'),
    path('cuartos/update/<int:numero>', CuartoUpdateView.as_view(), name='cuarto-update'),
    path('cuartos/delete/<int:numero>', CuartoDeleteView.as_view(), name='cuarto-delete'),
    path('reservaciones/', ReservacionCreateView.as_view(), name='reservacion-create'),
    path('reservaciones/<int:cliente>', ReservacionApiViewSet.as_view({"get": "retrieve"}), name='reservacion-ver'),
    path('reservaciones/update/<int:cliente>', ReservacionUpdateView.as_view(), name='reservacion-update'),
    path('reservaciones/delete/<int:cliente>', ReservacionDeleteView.as_view(), name='reservacion-delete'),
]
