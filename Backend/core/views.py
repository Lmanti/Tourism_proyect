from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from core.models import User, Hosting, Ofert, Municipality, Tourist, Activity, Restaurant, Discovery, Reservation
from core.serializers import (UserSerializer, HostingSerializer, OfertSerializer, MunicipalitySerializer, 
TouristSerializer, ActivitySerializer, RestaurantSerializer, DiscoverySerializer, ReservationSerializer)

from django.core.files.storage import default_storage

@csrf_exempt
def CrudUser(request, id = 0):

    if request.method == "GET":
        user = User.objects.all()
        user_serializer = UserSerializer(user, many = True)
        return JsonResponse(user_serializer.data, safe = False)

    elif request.method == "POST":
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data = user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added sucessfully.", safe=False)
        return JsonResponse("Failed to Add.", safe = False)

    elif request.method == "PUT":
        user_data = JSONParser().parse(request)
        user = User.objects.get(id_user = user_data['id_user'])
        user_serializer = UserSerializer(user ,data = user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Updated sucessfully.", safe=False)
        return JsonResponse("Failed to update.", safe = False)

    elif request.method == "DELETE":
        user = User.objects.get(id_user = id)
        user.delete()
        return JsonResponse("Delete sucessfully", safe=False)

@csrf_exempt
def CrudHosting(request, id = 0):

    if request.method == "GET":
        hosting = Hosting.objects.all()
        hosting_serializer = HostingSerializer(hosting, many = True)
        return JsonResponse(hosting_serializer.data, safe = False)

    elif request.method == "POST":
        hosting_data = JSONParser().parse(request)
        hosting_serializer = HostingSerializer(data = hosting_data)
        if hosting_serializer.is_valid():
            hosting_serializer.save()
            return JsonResponse("Added sucessfully.", safe=False)
        return JsonResponse("Failed to Add.", safe = False)

    elif request.method == "PUT":
        hosting_data = JSONParser().parse(request)
        hosting = Hosting.objects.get(id_hosting = hosting_data['id_hosting'])
        hosting_serializer = HostingSerializer(hosting ,data = hosting_data)
        if hosting_serializer.is_valid():
            hosting_serializer.save()
            return JsonResponse("Updated sucessfully.", safe=False)
        return JsonResponse("Failed to update.", safe = False)

    elif request.method == "DELETE":
        hosting = Hosting.objects.get(id_hosting = id)
        hosting.delete()
        return JsonResponse("Delete sucessfully", safe=False)

@csrf_exempt
def CrudOfert(request, id = 0):

    if request.method == "GET":
        ofert = Ofert.objects.all()
        ofert_serializer = OfertSerializer(ofert, many = True)
        return JsonResponse(ofert_serializer.data, safe = False)

    elif request.method == "POST":
        ofert_data = JSONParser().parse(request)
        ofert_serializer = OfertSerializer(data = ofert_data)
        if ofert_serializer.is_valid():
            ofert_serializer.save()
            return JsonResponse("Added sucessfully.", safe=False)
        return JsonResponse("Failed to Add.", safe = False)

    elif request.method == "PUT":
        ofert_data = JSONParser().parse(request)
        ofert = Ofert.objects.get(id_ofert= ofert_data['id_ofert'])
        ofert_serializer = HostingSerializer(ofert ,data = ofert_data)
        if ofert_serializer.is_valid():
            ofert_serializer.save()
            return JsonResponse("Updated sucessfully.", safe=False)
        return JsonResponse("Failed to update.", safe = False)

    elif request.method == "DELETE":
        ofert = Ofert.objects.get(id_ofert = id)
        ofert.delete()
        return JsonResponse("Delete sucessfully", safe=False)

@csrf_exempt
def CrudMunicipality(request, id = 0):

    if request.method == "GET":
        municipality = Municipality.objects.all()
        municipality_serializer = MunicipalitySerializer(municipality, many = True)
        return JsonResponse(municipality_serializer.data, safe = False)

    elif request.method == "POST":
        municipality_data = JSONParser().parse(request)
        municipality_serializer = MunicipalitySerializer(data=municipality_data)
        if municipality_serializer.is_valid():
            municipality_serializer.save()
            return JsonResponse("Added sucessfully.", safe=False)
        return JsonResponse("Failed to Add.", safe = False)

    elif request.method == "PUT":
        municipality_data = JSONParser().parse(request)
        municipality = Municipality.objects.get(id_municipality = municipality_data['id_municipality'])
        municipality_serializer = MunicipalitySerializer(municipality ,data = municipality_data)
        if municipality_serializer.is_valid():
            municipality_serializer.save()
            return JsonResponse("Updated sucessfully.", safe=False)
        return JsonResponse("Failed to update.", safe = False)

    elif request.method == "DELETE":
        municipality = Municipality.objects.get(id_municipality = id)
        municipality.delete()
        return JsonResponse("Delete sucessfully", safe=False)

@csrf_exempt
def CrudTourist(request, id = 0):

    if request.method == "GET":
        tourist = Tourist.objects.all()
        tourist_serializer = TouristSerializer(tourist, many = True)
        return JsonResponse(tourist_serializer.data, safe = False)

    elif request.method == "POST":
        tourist_data = JSONParser().parse(request)
        tourist_serializer = TouristSerializer(data = tourist_data)
        if tourist_serializer.is_valid():
            tourist_serializer.save()
            return JsonResponse("Added sucessfully.", safe=False)
        return JsonResponse("Failed to Add.", safe = False)

    elif request.method == "PUT":
        tourist_data = JSONParser().parse(request)
        tourist = Tourist.objects.get(id_tourist = tourist_data['id_tourist'])
        tourist_serializer = TouristSerializer(tourist ,data = tourist_data)
        if tourist_serializer.is_valid():
            tourist_serializer.save()
            return JsonResponse("Updated sucessfully.", safe=False)
        return JsonResponse("Failed to update.", safe = False)

    elif request.method == "DELETE":
        tourist = Tourist.objects.get(id_tourist = id)
        tourist.delete()
        return JsonResponse("Delete sucessfully", safe=False)

@csrf_exempt
def CrudActivity(request, id = 0):

    if request.method == "GET":
        activity = Activity.objects.all()
        activity_serializer = ActivitySerializer(activity, many = True)
        return JsonResponse(activity_serializer.data, safe = False)

    elif request.method == "POST":
        activity_data = JSONParser().parse(request)
        activity_serializer = ActivitySerializer(data = activity_data)
        if activity_serializer.is_valid():
            activity_serializer.save()
            return JsonResponse("Added sucessfully.", safe=False)
        return JsonResponse("Failed to Add.", safe = False)

    elif request.method == "PUT":
        activity_data = JSONParser().parse(request)
        activity = Activity.objects.get(id_activity = activity_data['id_activity'])
        activity_serializer = ActivitySerializer(activity ,data = activity_data)
        if activity_serializer.is_valid():
            activity_serializer.save()
            return JsonResponse("Updated sucessfully.", safe=False)
        return JsonResponse("Failed to update.", safe = False)

    elif request.method == "DELETE":
        activity = Activity.objects.get(id_activity = id)
        activity.delete()
        return JsonResponse("Delete sucessfully", safe=False)

@csrf_exempt
def CrudRestaurant(request, id = 0):

    if request.method == "GET":
        restaurant = Restaurant.objects.all()
        restaurant_serializer = RestaurantSerializer(restaurant, many = True)
        return JsonResponse(restaurant_serializer.data, safe = False)

    elif request.method == "POST":
        restaurant_data = JSONParser().parse(request)
        restaurant_serializer = RestaurantSerializer(data = restaurant_data)
        if restaurant_serializer.is_valid():
            restaurant_serializer.save()
            return JsonResponse("Added sucessfully.", safe=False)
        return JsonResponse("Failed to Add.", safe = False)

    elif request.method == "PUT":
        restaurant_data = JSONParser().parse(request)
        restaurant = Restaurant.objects.get(id_restaurant = restaurant_data['id_restaurant'])
        restaurant_serializer = RestaurantSerializer(restaurant ,data = restaurant_data)
        if restaurant_serializer.is_valid():
            restaurant_serializer.save()
            return JsonResponse("Updated sucessfully.", safe=False)
        return JsonResponse("Failed to update.", safe = False)

    elif request.method == "DELETE":
        restaurant = Restaurant.objects.get(id_restaurant = id)
        restaurant.delete()
        return JsonResponse("Delete sucessfully", safe=False)

@csrf_exempt
def CrudDiscovery(request, id = 0):

    if request.method == "GET":
        discovery = Discovery.objects.all()
        discovery_serializer = DiscoverySerializer(discovery, many = True)
        return JsonResponse(discovery_serializer.data, safe = False)

    elif request.method == "POST":
        discovery_data = JSONParser().parse(request)
        discovery_serializer = DiscoverySerializer(data = discovery_data)
        if discovery_serializer.is_valid():
            discovery_serializer.save()
            return JsonResponse("Added sucessfully.", safe=False)
        return JsonResponse("Failed to Add.", safe = False)

    elif request.method == "PUT":
        discovery_data = JSONParser().parse(request)
        discovery = Discovery.objects.get(id_discovery = discovery_data['id_discovery'])
        discovery_serializer = DiscoverySerializer(discovery ,data = discovery_data)
        if discovery_serializer.is_valid():
            discovery_serializer.save()
            return JsonResponse("Updated sucessfully.", safe=False)
        return JsonResponse("Failed to update.", safe = False)

    elif request.method == "DELETE":
        discovery = Discovery.objects.get(id_discovery = id)
        discovery.delete()
        return JsonResponse("Delete sucessfully", safe=False)

@csrf_exempt
def CrudReservation(request, id = 0):

    if request.method == "GET":
        reservation = Reservation.objects.all()
        reservation_serializer = ReservationSerializer(reservation, many = True)
        return JsonResponse(reservation_serializer.data, safe = False)

    elif request.method == "POST":
        reservation_data = JSONParser().parse(request)
        reservation_serializer = ReservationSerializer(data = reservation_data)
        if reservation_serializer.is_valid():
            reservation_serializer.save()
            return JsonResponse("Added sucessfully.", safe=False)
        return JsonResponse("Failed to Add.", safe = False)

    elif request.method == "PUT":
        reservation_data = JSONParser().parse(request)
        reservation = Reservation.objects.get(id_reservation = reservation_data['id_reservation'])
        reservation_serializer = ReservationSerializer(reservation ,data = reservation_data)
        if reservation_serializer.is_valid():
            reservation_serializer.save()
            return JsonResponse("Updated sucessfully.", safe=False)
        return JsonResponse("Failed to update.", safe = False)

    elif request.method == "DELETE":
        reservation = Reservation.objects.get(id_reservation = id)
        reservation.delete()
        return JsonResponse("Delete sucessfully", safe=False)

# Create your views here.
