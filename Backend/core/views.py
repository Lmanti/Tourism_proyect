from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from core.models import User, Hosting, Ofert, Municipality, Tourist, Activity, Restaurant, Discovery, Reservation
from core.serializers import (UserSerializer, HostingSerializer, OfertSerializer, MunicipalitySerializer, 
TouristSerializer, ActivitySerializer, RestaurantSerializer, DiscoverySerializer, ReservationSerializer)

from django.core.files.storage import default_storage


def CreateUser(request, id = 0):

    if request.method == "GET":
        pass


# Create your views here.
