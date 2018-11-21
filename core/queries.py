from django.shortcuts import render

# Create your views here.

from .tables import CarTable
from .tables import ChargeTable
from .models import Employee, VehicleEngineer, VehiclePark, Workshop, ProvidngManager, CarParts, Car, ChargingStation, Operator, Customer, Charge


def query1():
    cars = Car.objects.all().filter(car_plate__startswith='AN').filter(color='red')
    return cars


def query2(date):
    charges = Charge.objects.all().filter(time__day=date)
    print(charges)
    amounts = []
    for i in range(24):
        amounts.append(charges.filter(time__hour=i))
    # return ChargeTable(amounts)
    # return ChargeTable(charges)