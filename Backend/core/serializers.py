from rest_framework import serializers
from core.models import User, Hosting, Ofert, Municipality, Tourist, Activity, Restaurant, Discovery, Reservation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id_user',
                'email',
                'password',
                'first_name',
                'last_name',
                'date_birth',
                'nationality',
                'phone_number')

class OfertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ofert
        fields = ('id_ofert',
                'in_ofert',
                'end_ofert',
                'discount',
                'name')

class MunicipalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipality
        fields = ('id_municipality',
                'name',
                'image',
                'desciption')


class HostingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hosting
        fields = ('id_hosting',
                'name',
                'description',
                'department',
                'municipality',
                'rating',
                'price_per_night')

class TouristSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist
        fields = ('id_tourist',
                'name',
                'direction',
                'department',
                'municipality',
                'cost',
                'rating',
                'schedule',
                'tipe_site_touristic')

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ('id_activity',
                'name',
                'rating',
                'type_actvity',
                'cost',
                'schedule',
                'duration_activity',
                'department',
                'municipality'
                )

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('id_restaurant',
                'name',
                'direction',
                'department',
                'municipality',
                'schedule',
                'rating',
                'type_food',
                )

class DiscoverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Discovery
        fields = ('id_discovery',
                'name',
                'direction',
                'rating',
                'description')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        field = ('id_reservation',
                'hour_reservation',
                'duration_reservation')

