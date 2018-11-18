from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse



def query1():
    from .models import Employee, VehicleEngineer, VehiclePark, Workshop, ProvidngManager, CarParts, Car, ChargingStation, Operator, Customer
    text = "A customer claims she forgot her bag in a car and asks to help. " \
           "She was using cars several times this day, " \
           "but she believes the right car was red and its plate starts with “AN”. " \
           "Find all possible cars that match the description."
    cars = Car.objects.all().filter(car_plate__startswith='AN').filter(color = 'red')
    return cars
def query2():
    from .models import Employee, VehicleEngineer, VehiclePark, Workshop, ProvidngManager, CarParts, Car, ChargingStation, Operator, Customer
    text = "Company management wants to get a statistics on the efficiency of charging stations utilization. " \
           "Given a date, compute how many sockets were occupied each hour."

