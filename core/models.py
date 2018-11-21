from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Employee(models.Model):
    username = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.TextField(default="")
    phone_number = models.TextField(default="")

    def __unicode__(self):
        return u"%s" % self.username


class VehicleEngineer(models.Model):
    info = models.ForeignKey(Employee, on_delete=models.CASCADE)



class Workshop(models.Model):
    workshopid = models.CharField(max_length=10, primary_key=True)
    country = models.TextField(default="")
    zipcode = models.CharField(max_length=30)
    city = models.TextField(default="")

    def __unicode__(self):
        return u"%s" % self.workshopid

class ProvidngManager(models.Model):
    companyid = models.CharField(max_length=10, primary_key=True)
    country = models.TextField(default="")
    zipcode = models.CharField(max_length=30)
    city = models.TextField(default="")
    name_of_the_provider = models.TextField(default="")
    info = models.ForeignKey(Employee, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s" % self.companyid

class CarParts(models.Model):
    type = models.TextField(default="")
    car_model = models.TextField(default="")
    count = models.IntegerField(default=0)
    color = models.TextField(default="white")
    engineer = models.ForeignKey(VehicleEngineer, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s" % self.type

class ChargingStation(models.Model):
    uid = models.CharField(max_length=10, primary_key=True)
    price = models.IntegerField(default=0)
    amount_of_available_sockets = models.IntegerField(default=0)
    gps_location = models.TextField(default="")
    size_of_plug = models.TextField(default="")
    shape_of_plug = models.TextField(default="")

    def __unicode__(self):
        return u"%s" % self.uid

class VehiclePark(models.Model):
    vid = models.CharField(max_length=10, primary_key=True)
    location = models.TextField(default="")
    amount_of_cars = models.IntegerField(default=0)

    def __unicode__(self):
        return u"%s" % self.vid

class Car(models.Model):
    car_id = models.CharField(max_length=10, primary_key=True)
    model = models.TextField(default="")
    amount_of_places = models.IntegerField(default=4)
    color = models.TextField(default="white")
    engineer = models.ForeignKey(VehicleEngineer, on_delete=models.CASCADE)
    park = models.ForeignKey(VehiclePark, on_delete=models.CASCADE)
    car_plate = models.TextField(default="")

    def __unicode__(self):
        return u"%s" % self.car_id

class Charge(models.Model):
    charge_id = models.CharField(max_length=10, primary_key=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    charging_station = models.ForeignKey(ChargingStation, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.now, blank=True)


class Operator(models.Model):
    parks = models.ManyToManyField(VehiclePark)
    cars = models.ManyToManyField(Car)
    info = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s" % self.info

class Customer(models.Model):
    username = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.TextField(default="")
    country = models.TextField(default="")
    zipcode = models.CharField(max_length=30)
    city = models.TextField(default="")
    phone_number = models.TextField(default="")
    operator = models.ForeignKey(Operator, on_delete=models.CASCADE)
    car = models.OneToOneField(Car, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s" % self.username




