from django.shortcuts import render

# Create your views here.

from .tables import CarTable
from .models import Employee, VehicleEngineer, VehiclePark, Workshop, ProvidngManager, CarParts, Car, ChargingStation, Operator, Customer


def query1():
    cars = Car.objects.all().filter(car_plate__startswith='AN').filter(color='red')
    return CarTable(cars)

