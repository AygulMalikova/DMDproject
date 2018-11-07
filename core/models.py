from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    username = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.TextField(default="")
    country = models.TextField(default="")
    zipcode = models.CharField(max_length=30)
    city = models.TextField(default="")
    phone_number = models.TextField(default="")

class Employee(models.Model):
    username = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.TextField(default="")
    phone_number = models.TextField(default="")

class ProvidngManager(models.Model):
    companyid = models.AutoField(primary_key=True)
    country = models.TextField(default="")
    zipcode = models.CharField(max_length=30)
    city = models.TextField(default="")
    name_of_the_provider = models.TextField(default="")

class Operator(models.Model):

class VehicleEngineer(models.Model):

class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    model = models.TextField(default="")
    amount_of_places = models.IntegerField(default=4)
    color = models.TextField(default="white")

class Workshop(models.Model):
    workshopid = models.AutoField(primary_key=True)
    country = models.TextField(default="")
    zipcode = models.CharField(max_length=30)
    city = models.TextField(default="")

class CarParts(models.Model):
    type = models.TextField(default="")
    car_model = models.TextField(default="")
    count = models.IntegerField(default=0)
    color = models.TextField(default="white")

class ChargingStation(models.Model):
    uid = models.AutoField(primary_key=True)
    price = models.IntegerField(default=0)
    amount_of_available_sockets = models.IntegerField(default=0)
    gps_location = models.TextField(default="")
    size_of_plug = models.TextField(default="")
    shape_of_plug = models.TextField(default="")

class VehiclePark(models.Model):
    vid = models.AutoField(primary_key=True)
    location = models.TextField(default="")
    amount_of_cars = models.IntegeField(default=0)

    def __unicode__(self):
        return u"%s" % self.model
