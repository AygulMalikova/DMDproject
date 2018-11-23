import datetime
import math

from .tables import Table1, Table2, Table3, Table4, Table5, Table6, Table7, Table8, Table9, Table10
from .models import Employee, VehicleEngineer, VehiclePark, Workshop, ProvidingManager, CarParts, Car, ChargingStation, \
    Operator, Customer, Charge, Order, Payment, ProvidedPart
from django.contrib.gis.geoip2 import GeoIP2


def query1(plate, color):
    cars = Car.objects.all().filter(car_plate__startswith=plate).filter(color=color)
    return Table1(cars)


def query2(date):
    charges = Charge.objects.all().filter(time__day=date.day)
    result = []
    for i in range(24):
        result.append({'time': str(i) + ':00', 'amount': charges.filter(time__hour=i).count()})
    return Table2(result)


def query3(morningFrom, morningTo, afternoonFrom, aftenoonTo, eveningFrom, eveningTo):
    orders = Order.objects.all().filter(time_begin__gte=datetime.date.today() - datetime.timedelta(days=7))
    morning = orders.filter(time_begin__hour=morningFrom)
    afternoon = orders.filter(time_begin__hour=afternoonFrom)
    evening = orders.filter(time_begin__hour=eveningFrom)
    for i in range(morningFrom+1, morningTo+1):
        morning = morning | orders.filter(time_begin__hour=i)
    for i in range(afternoonFrom+1, aftenoonTo+1):
        afternoon = afternoon | orders.filter(time_begin__hour=i)
    for i in range(eveningFrom+1, eveningTo+1):
        evening = evening | orders.filter(time_begin__hour=i)
    amount_cars = Car.objects.all().count()
    result = []
    result.append({'percent': (morning.count()/amount_cars)*100})
    result.append({'percent': (afternoon.count()/amount_cars)*100})
    result.append({'percent': (evening.count()/amount_cars)*100})
    return Table3(result)


def query4(username):
    payments = Payment.objects.all().filter(time_of_payment__gte=datetime.date.today() - datetime.timedelta(days=30))\
        .filter(order__customer__username=username).order_by('time_of_payment')
    result = []
    for p in payments:
        result.append({'id': p.id, 'order': p.order_id, 'time': p.time_of_payment, 'price': p.price})
    return Table4(result)


def query5(date):
    result = []
    orders = Order.objects.all().filter(time_begin__day=date.day)
    distance = 0
    duration = 0
    for e in orders:
        first = e.location_car.split()
        second = e.location_end.split()
        x1 = int(first[0])
        y1 = int(first[1])
        x2 = int(second[0])
        y2 = int(second[1])
        distance += math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
        duration += (e.time_end.hour - e.time_begin.hour)*60 + e.time_end.minute-e.time_begin.time().minute
    n = orders.count()
    if n == 0:
        result.append({'avg_distance': 0, 'avg_duration': 0})
    else:
        result.append({'avg_distance': distance/n, 'avg_duration': duration/n})
    return Table5(result)


def query6(morningFrom, morningTo, afternoonFrom, aftenoonTo, eveningFrom, eveningTo): #return 9 elements: top3 at the morning, top3 at the afternoon and top3 at the evening
    orders = Order.objects.all()
    for i in range(morningFrom, morningTo + 1):
        morning = orders.filter(time_begin__hour=i)
    for i in range(afternoonFrom, aftenoonTo+1):
        afternoon = orders.filter(time_begin__hour=i)
    for i in range(eveningFrom, eveningTo+1):
        evening = orders.filter(time_begin__hour=i)
    result = []
    #11111
    top1, top2, top3 = "", "", ""
    mx1, mx2, mx3 = 0, 0, 0
    for e in morning:
        cur = morning.filter(location_begin=e.location_begin)
        if mx3 < cur.count():
            mx3 = cur.count()
            top3 = e.location_begin
        if mx2 < mx3:
            mx2, mx3 = mx3, mx2
            top2, top3 = top3, top2
        if mx1 < mx2:
            mx1,mx2 = mx2, mx1
            top1, top2 = top2, top1
    result.append({'top_morning_1': top1})
    result.append({'top_morning_1': top2})
    result.append({'top_morning_1': top3})
    #22222
    top1, top2, top3 = "", "", ""
    mx1, mx2, mx3 = 0, 0, 0
    for e in afternoon:
        cur = afternoon.filter(location_begin=e.location_begin)
        if mx3 < cur.count():
            mx3 = cur.count()
            top3 = e.location_begin
        if mx2 < mx3:
            mx2, mx3 = mx3, mx2
            top2, top3 = top3, top2
        if mx1 < mx2:
            mx1, mx2 = mx2, mx1
            top1, top2 = top2, top1
    result.append({'top_afternoon_1': top1})
    result.append({'top_afternoon_1': top2})
    result.append({'top_afternoon_1': top3})
    #33333
    top1, top2, top3 = "", "", ""
    mx1, mx2, mx3 = 0, 0, 0
    for e in evening:
        cur = evening.filter(location_begin=e.location_begin)
        if mx3 < cur.count():
            mx3 = cur.count()
            top3 = e.location_begin
        if mx2 < mx3:
            mx2, mx3 = mx3, mx2
            top2, top3 = top3, top2
        if mx1 < mx2:
            mx1, mx2 = mx2, mx1
            top1, top2 = top2, top1

    result.append({'top_evening_1': top1})
    result.append({'top_evening_1': top2})
    result.append({'top_evening_1': top3})
    #11111destination
    top1, top2, top3 = "", "", ""
    mx1, mx2, mx3 = 0, 0, 0
    for e in evening:
        cur = morning.filter(location_end=e.location_end)
        if mx3 < cur.count():
            mx3 = cur.count()
            top3 = e.location_begin
        if mx2 < mx3:
            mx2, mx3 = mx3, mx2
            top2, top3 = top3, top2
        if mx1 < mx2:
            mx1, mx2 = mx2, mx1
            top1, top2 = top2, top1
    result.append({'top_morning_2': top1})
    result.append({'top_morning_2': top2})
    result.append({'top_morning_2': top3})
    #22222destination
    top1, top2, top3 = "", "", ""
    mx1, mx2, mx3 = 0, 0, 0
    for e in evening:
        cur = afternoon.filter(location_end=e.location_end)
        if mx3 < cur.count():
            mx3 = cur.count()
            top3 = e.location_begin
        if mx2 < mx3:
            mx2, mx3 = mx3, mx2
            top2, top3 = top3, top2
        if mx1 < mx2:
            mx1, mx2 = mx2, mx1
            top1, top2 = top2, top1
    result.append({'top_afternoon_2': top1})
    result.append({'top_afternoon_2': top2})
    result.append({'top_afternoon_2': top3})
    #33333destination
    top1, top2, top3 = "", "", ""
    mx1, mx2, mx3 = 0, 0, 0
    for e in evening:
        cur = evening.filter(location_end=e.location_end)
        if mx3 < cur.count():
            mx3 = cur.count()
            top3 = e.location_begin
        if mx2 < mx3:
            mx2, mx3 = mx3, mx2
            top2, top3 = top3, top2
        if mx1 < mx2:
            mx1, mx2 = mx2, mx1
            top1, top2 = top2, top1
    result.append({'top_evening_2': top1})
    result.append({'top_evening_2': top2})
    result.append({'top_evening_2': top3})

    return Table6(result)


def takeFirst(elem):
    return elem[0]


def query7(perc, lastdays):
    percent = perc
    orders = Order.objects.all().filter(time_begin__gte=datetime.date.today() - datetime.timedelta(days=lastdays))
    n = Car.objects.all().count()
    cars = []
    for e in orders:
        current = orders.filter(car=e.car)
        cars.append((current.count, e.car))
    cars.sort(key=takeFirst)
    result = []
    for i in range(0, int(math.ceil(n*(percent/100)))):
        result.append(cars[i][1])
    return Table7(result)


def query8(days):#returns pair(customer, amount)
    customers = Customer.objects.all()
    orders = Order.objects.all().filter(time_begin__gte=datetime.date.today() - datetime.timedelta(days=days))
    charges = Charge.objects.all().filter(time__gte=datetime.date.today() - datetime.timedelta(days=days))
    result = []
    for e in customers:
        current = orders.filter(customer_id=e)
        amount = 0
        for c in current:
            amount += charges.filter(car=c.car).filter(time__day=c.time_begin.day).count()
        result.append({'customer': e.username, 'amount': amount})
    return Table8(result)


def query9(days):#returns list of pairs(workshop, amount)
    provided_parts = ProvidedPart.objects.all().filter(time_of_providing=datetime.date.today() - datetime.timedelta(days=days))
    workshops = Workshop.objects.all()
    result = []
    for w in workshops:
        result.append({'workshop': w.workshopid, 'amount': provided_parts.filter(workshop=w).count()})
    return Table9(result)


def query10():#returs car model
    provided_parts = ProvidedPart.objects.all()
    charges = Charge.objects.all()
    cars = Car.objects.all()
    max = 0
    best = cars[0]
    result = []
    for c in cars:
        used_parts = provided_parts.filter(car_part__car__model=c.model)
        current = 0
        for e in used_parts:
            current += e.car_part.price
        used_charges = charges.filter(car=c)
        for e in used_charges:
            current += e.charging_station.price
        if max < current:
            max = current
            best = c
    result.append({'best': best.model, "cost": max})
    return Table10(result)

