from django.db import models
from django.contrib.auth.models import User
import datetime


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
    workshopid = models.IntegerField(default=0, primary_key=True)
    country = models.TextField(default="")
    zipcode = models.CharField(max_length=30)
    city = models.TextField(default="")

    def __unicode__(self):
        return u"%s" % self.workshopid

class ProvidingManager(models.Model):
    company_id = models.IntegerField(default=0, primary_key=True)
    country = models.TextField(default="")
    zipcode = models.CharField(max_length=30)
    city = models.TextField(default="")
    name_of_the_provider = models.TextField(default="")
    info = models.ForeignKey(Employee, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s" % self.companyid


class ChargingStation(models.Model):
    uid = models.IntegerField(default=0, primary_key=True)
    price = models.IntegerField(default=0)
    amount_of_available_sockets = models.IntegerField(default=0)
    gps_location = models.TextField(default="")
    size_of_plug = models.TextField(default="")
    shape_of_plug = models.TextField(default="")

    def __unicode__(self):
        return u"%s" % self.uid

class VehiclePark(models.Model):
    vid = models.IntegerField(default=0, primary_key=True)
    location = models.TextField(default="")
    amount_of_cars = models.IntegerField(default=0)

    def __unicode__(self):
        return u"%s" % self.vid

class Car(models.Model):
    car_id = models.IntegerField(default=0, primary_key=True)
    model = models.TextField(default="")
    amount_of_places = models.IntegerField(default=4)
    color = models.TextField(default="white")
    engineer = models.ForeignKey(VehicleEngineer, on_delete=models.CASCADE)
    park = models.ForeignKey(VehiclePark, on_delete=models.CASCADE)
    car_plate = models.TextField(default="")

    def __unicode__(self):
        return u"%s" % self.car_id

class CarParts(models.Model):
    type = models.TextField(default="")
    car = models.ForeignKey(Car, default=None, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    color = models.TextField(default="white")
    engineer = models.ForeignKey(VehicleEngineer, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)

    def __unicode__(self):
        return u"%s" % self.type

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

class Charge(models.Model):
    charge_id = models.IntegerField(default=0, primary_key=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    charging_station = models.ForeignKey(ChargingStation, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.datetime.now())


class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    time_begin = models.DateTimeField(default=datetime.datetime.now())
    time_end = models.DateTimeField(default=datetime.datetime.now())
    location_begin = models.TextField(default="")
    location_end = models.TextField(default="")
    location_car = models.TextField(default="")

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    time_of_payment = models.DateTimeField(default=datetime.datetime.now())
    price = models.IntegerField(default=0)


class ProvidedPart(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    car_part = models.ForeignKey(CarParts, on_delete=models.CASCADE)
    time_of_providing = models.DateTimeField(default=datetime.datetime.now())
    price = models.IntegerField(default=0)