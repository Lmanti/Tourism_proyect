from django.db import models

# Create your models here.

class User(models.Model):
    id_user = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=35)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_birth = models.DateField()
    nationality = models.CharField(max_length=50)
    phone_number = models.IntegerField()

class Ofert(models.Model):
    id_ofert = models.IntegerField(primary_key=True)
    in_ofert = models.DateField()
    end_ofert = models.DateField()
    discount = models.FloatField(max_length=5)
    name = models.CharField(max_length=30)

class Municipality(models.Model):
    id_municipality = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    image = models.CharField(max_length=255) # This is a image
    desciption = models.TextField()

class Hosting(models.Model):
    id_hosting = models.IntegerField(primary_key=True)
    id_municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=25)
    description = models.TextField()
    department = models.CharField(max_length=25)
    municipality = models.CharField(max_length=30, default=None)
    rating = models.FloatField(max_length=1)
    price_per_night = models.FloatField()

# class Hosting_municipality(models.Model):
#     id_municipalitys = models.ManyToManyRel(Hosting)
#     id_hosting = models.ManyToManyRel(Municipality)

class Tourist(models.Model):
    id_tourist = models.IntegerField(primary_key=True)
    id_municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, default=None)
    id_ofert_site = models.IntegerField()
    name = models.CharField(max_length=30)
    direction = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    municipality = models.CharField(max_length=30)
    cost = models.FloatField()
    rating = models.FloatField(max_length=1)
    schedule = models.DateTimeField()
    tipe_site_touristic = models.CharField(max_length=30)

class Activity(models.Model):
    id_activity = models.IntegerField(primary_key=True)
    id_municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE, default=None)
    id_ofert_activity = models.IntegerField()
    name = models.CharField(max_length=30)
    rating = models.FloatField(max_length=1)
    type_actvity = models.CharField(max_length=30)
    cost = models.FloatField()
    schedule = models.DateTimeField()
    duration_activity = models.DateTimeField()
    department = models.CharField(max_length=30)
    municipality = models.CharField(max_length=30, default=None)

class Restaurant(models.Model):
    id_restaurant = models.IntegerField(primary_key=True)
    id_ofert_restaurant = models.IntegerField()
    name = models.CharField(max_length=30)
    direction = models.CharField(max_length=30)
    department = models.CharField(max_length=30, default=None)
    municipality = models.CharField(max_length=30)
    schedule = models.DateTimeField()
    rating = models.FloatField(max_length=1)
    type_food = models.CharField(max_length=30)
    municipality_restaurant = models.ManyToManyField(Municipality)

class Discovery(models.Model):
    id_discovery = models.IntegerField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_municipality = models.ForeignKey(Municipality,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    direction = models.CharField(max_length=30)
    rating = models.FloatField(max_length=1)
    description = models.TextField()

class Reservation(models.Model):
    id_reservation = models.IntegerField(primary_key=True, default=None)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    id_tourist = models.ForeignKey(Tourist, on_delete=models.CASCADE, default=None)
    id_activity = models.ForeignKey(Activity, on_delete=models.CASCADE, default=None)
    id_hosting = models.ForeignKey(Hosting, on_delete=models.CASCADE, default=None)
    id_restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default=None)
    id_ofert = models.ForeignKey(Ofert, on_delete=models.CASCADE, default=None)
    hour_reservation = models.DateTimeField(auto_now=True)
    duration_reservation = models.DateTimeField(auto_now=True)

