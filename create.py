from faker import Faker
from django.db import models
from core.models import Workshop
from core.models import Employee
from core.models import VehicleEngineer
from core.models import Operator
from core.models import VehiclePark
from core.models import Car
from core.models import Customer
from core.models import Charge
from core.models import ChargingStation
from core.models import Order
from core.models import Payment
from core.models import ProvidedPart
from core.models import CarParts
from random import randint
import time
import random
import datetime
import pytz
import math
from django.utils import timezone
from django.utils.timezone import make_aware
from random import randrange
from datetime import datetime
from datetime import timedelta
from .models import Employee, VehicleEngineer, VehiclePark, Workshop, ProvidingManager, CarParts, Car, ChargingStation, Operator, Customer, Charge, Order, Payment, ProvidedPart
fake = Faker('en_GB')
def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

d1 = datetime.strptime('1/1/2018 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('11/25/2018 4:50 AM', '%m/%d/%Y %I:%M %p')

park = VehiclePark(vid = 0, location = fake.location_on_land(), amount_of_cars = 100)
park.save()

employee = Employee(username = fake.user_name(), first_name = fake.first_name(), last_name = fake.last_name(), email = fake.free_email(), phone_number = fake.phone_number())
employee.save()
engineer = VehicleEngineer(info = employee)
engineer.save()


employee = Employee(username = fake.user_name(), first_name = fake.first_name(), last_name = fake.last_name(), email = fake.free_email(), phone_number = fake.phone_number())
employee.save()
engineer = VehicleEngineer(info = employee)
engineer.save()

for i in range(20, 40):
    car = Car(car_id=i, model="BMW i3", amount_of_places=4, color=fake.color_name(), engineer=engineer,park=park, car_plate=2)
    car.save()

employee = Employee(username = fake.user_name(), first_name = fake.first_name(), last_name = fake.last_name(), email = fake.free_email(), phone_number = fake.phone_number())
employee.save()
engineer = VehicleEngineer(info = employee)
engineer.save()

for i in range(40, 60):
    car = Car(car_id=i, model="Nissan Leaf", amount_of_places=4, color=fake.color_name(), engineer=engineer,park=park, car_plate=3)
    car.save()


employee = Employee(username = fake.user_name(), first_name = fake.first_name(), last_name = fake.last_name(), email = fake.free_email(), phone_number = fake.phone_number())
employee.save()
engineer = VehicleEngineer(info = employee)
engineer.save()

for i in range(60, 80):
    car = Car(car_id=i, model="Volkswagen e-Golf", amount_of_places=4, color=fake.color_name(), engineer=engineer,park=park, car_plate=4)
    car.save()

employee = Employee(username = fake.user_name(), first_name = fake.first_name(), last_name = fake.last_name(), email = fake.free_email(), phone_number = fake.phone_number())
employee.save()
engineer = VehicleEngineer(info = employee)
engineer.save()

for i in range(80, 100):
    car = Car(car_id=i, model="Chevrolet Bolt EV", amount_of_places=4, color=fake.color_name(), engineer=engineer,park=park, car_plate=5)
    car.save()


for i in range(0, 10):
    workshop = Workshop(workshopid = i, country = fake.country(), zipcode = fake.postcode(), city = fake.city())
    workshop.save()



for i in range(0, 210):
    try:
        charging_station = ChargingStation.objects.get(uid = random.randint(0, 2))
    except ChargingStation.DoesNotExist:
        charging_station = ChargingStation(uid = 0, price = 25, amount_of_available_sockets = 25, gps_location = '234 412', size_of_plug = 2, shape_of_plug = 2)
    try:
        car = Car.objects.get(car_id = random.randint(0, 99))
    except Car.DoesNotExist:
            car = Car(car_id=i, model="BMW i3", amount_of_places=4, color=fake.color_name(), engineer=engineer,park=park, car_plate=2)
    try:
        customer = Customer.objects.get(username='efewfwe')
    except Customer.DoesNotExist:
        employee = Employee(username=fake.user_name(), first_name=fake.first_name(), last_name=fake.last_name(), email=fake.free_email(), phone_number=fake.phone_number())
        operator = Operator(info=employee, park=park, car=None)
        car = Car(car_id=i, model="BMW i3", amount_of_places=4, color=fake.color_name(), engineer=engineer, park=park,car_plate=2)
        customer = Customer(username=fake.user_name(), first_name=fake.first_name(), last_name=fake.last_name(),email=fake.free_email(), country=fake.country(), zipcode=fake.postcode(), city=fake.city(),phone_number=fake.phone_number(), operator=operator, car=car)
    p = datetime.now()
    p = random_date(d1, d2)
    make_aware(p)
    charge = Charge(charge_id = i, car = car, charging_station = charging_station, time = random_date(d1, d2), customer = customer)
    charge.save()


for i in range(4, 110):
    try:
        engineer = VehicleEngineer.objects.get(info = Employee.objects.get(username = 'tbird'))
    except VehicleEngineer.DoesNotExist:
        employee = Employee(username=fake.user_name(), first_name=fake.first_name(), last_name=fake.last_name(),email=fake.free_email(), phone_number=fake.phone_number())
        employee.save()
        VehicleEngineer = VehicleEngineer(info = employee)
    try:
        car = Car.objects.get(car_id = i)
    except Car.DoesNotExist:
        car = Car(car_id=i, model="BMW i3", amount_of_places=4, color=fake.color_name(), engineer=engineer,park=park, car_plate=2)
    try:
        workshop = Workshop.objects.get(workshopid = randint(0,2))
    except Workshop.DoesNotExist:
        workshop = Workshop(workshopid = 0, country = fake.country(), zipcode = fake.postcode(), city = fake.city())
    carpart = CarParts(car=car,  type = "Door", count = randint(25, 500), color = fake.color_name(), engineer = engineer, workshop = workshop)
    carpart .save()
    providedpart = ProvidedPart(car_part = carpart, workshop =workshop, time_of_providing = random_date(d1, d2), price = randint(25, 300))
    providedpart.save()



for i in range(0, 30):
    try:
        customer = Customer.objects.get(username ='BillV')
    except Customer.DoesNotExist:
        employee = Employee(username=fake.user_name(), first_name=fake.first_name(), last_name=fake.last_name(),email=fake.free_email(), phone_number=fake.phone_number())
        operator = Operator(info = employee, park=park,car = None)
        car = Car(car_id=i, model="BMW i3", amount_of_places=4, color=fake.color_name(), engineer=engineer, park=park,car_plate=2)
        customer = Customer(username=fake.user_name(), first_name=fake.first_name(), last_name=fake.last_name(),email=fake.free_email(), country=fake.country(), zipcode=fake.postcode(), city=fake.city(),phone_number=fake.phone_number(), operator=operator, car=car)
    try:
        car = Car.objects.get(car_id = random.randint(0, 99))
    except Car.DoesNotExist:
        car = Car(car_id=i, model="BMW i3", amount_of_places=4, color=fake.color_name(), engineer=engineer,park=park, car_plate=2)
    p = random_date(d1, d2)
    z = p + timedelta(hours = randint(1, 9))
    order = Order(customer = customer, car = car,time_begin = p, time_end = z, location_begin = str(randint(0, 1000)) + ' ' + str(randint(0, 1000)), location_end = str(randint(0, 1000)) + ' ' + str(randint(0, 1000)), location_car = str(randint(0, 1000)) + ' ' + str(randint(0, 1000)))
    order.save()
    payment = Payment(order = order, time_of_payment = z, price = randint(25, 500))
    payment.save()



for i in range(0, 110):
    try:
        operator = Operator.objects.get(info = Employee.objects.get(username = 'qwetuk'))
    except Operator.DoesNotExist:
        employee = Employee(username=fake.user_name(), first_name=fake.first_name(), last_name=fake.last_name(),email=fake.free_email(), phone_number=fake.phone_number())
        employee.save()
        operator = Operator(info = employee, park=park,car = None)
    try:
        car = Car.objects.get(car_id = i)
    except Car.DoesNotExist:
        car = Car(car_id=i, model="BMW i3", amount_of_places=4, color=fake.color_name(), engineer=engineer,park=park, car_plate=2)
    customer = Customer(username=fake.user_name(), first_name=fake.first_name(), last_name=fake.last_name(),email=fake.free_email(), country=fake.country(), zipcode=fake.postcode(), city=fake.city(),phone_number=fake.phone_number(), operator=operator,car=car)
    customer.save()


for i in range(0, 300):
    try:
        charging_station = ChargingStation.objects.get(uid = random.randint(0, 2))
    except ChargingStation.DoesNotExist:
        charging_station = ChargingStation(uid = 0, price = 25, amount_of_available_sockets = 25, gps_location = '234 412', size_of_plug = 2, shape_of_plug = 2)
    try:
        car = Car.objects.get(car_id = random.randint(0, 99))
    except Car.DoesNotExist:
            car = Car(car_id=i, model="BMW i3", amount_of_places=4, color=fake.color_name(), engineer=engineer,park=park, car_plate=2)
    p = datetime.now()
    p = random_date(d1, d2)
    make_aware(p)
    charge = Charge(charge_id = i, car = car, charging_station = charging_station, time = random_date(d1, d2))
    charge.save()








