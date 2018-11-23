import datetime

from .tables import Table1, Table2, Table3, Table4, Table5, Table6, Table7, Table8, Table9, Table10
from .models import Employee, VehicleEngineer, VehiclePark, Workshop, ProvidingManager, CarParts, Car, ChargingStation, \
    Operator, Customer, Charge, Order, Payment, ProvidedPart
from django.contrib.gis.geoip2 import GeoIP2


def query1(plate, color):
    cars = Car.objects.all().filter(car_plate__startswith=plate).filter(color=color)
    return Table1(cars)


def query2(date):
    charges = Charge.objects.all().filter(time__day=date.day)
    amounts = []
    for i in range(24):
        amounts.append(charges.filter(time__hour=i))
    return Table2(amounts)


def query3(morningFrom, morningTo, afternoonFrom, aftenoonTo, eveningFrom, eveningTo):
    orders = Order.objects.all().filter(time_begin__gte=datetime.date.today() - datetime.timedelta(days=7))
    for i in range(morningFrom, morningTo+1):
        morning = orders.filter(time_begin__hour=i)
    for i in range(afternoonFrom, aftenoonTo+1):
        afternoon = orders.filter(time_begin__hour=i)
    for i in range(eveningFrom, eveningTo+1):
        evening = orders.filter(time_begin__hour=i)
    amount_cars = Car.objects.all().count()
    ans = []
    ans.append(morning.count()/amount_cars)
    ans.append(afternoon.count()/amount_cars)
    ans.append(evening.count()/amount_cars)
    return Table3(ans)



def query4(username):
    payments = Payment.objects.all().filter(time_of_payment__gte=datetime.date.today() - datetime.timedelta(days=30))
    payments.filter(order__customer__username=username)
    payments = payments.order_by('time_of_payment')
    return Table4(payments)


def query5(date):
    orders = Order.objects.all().filter(time_begin__day=date.day)
    distance = 0
    duration = 0
    for e in orders:
        first = GeoIP2.geos(e.location_car)
        second = GeoIP2.geos(e.location_end)
        distance += first.distance(second)
        duration += e.time_end-e.time_begin
    n = orders.count() + 1
    return Table5([distance/n, duration/n])


def query6(morningFrom, morningTo, afternoonFrom, aftenoonTo, eveningFrom, eveningTo): #return 9 elements: top3 at the morning, top3 at the afternoon and top3 at the evening
    orders = Order.objects.all()
    for i in range(morningFrom, morningTo + 1):
        morning = orders.filter(time_begin__hour=i)
    for i in range(afternoonFrom, aftenoonTo+1):
        afternoon = orders.filter(time_begin__hour=i)
    for i in range(eveningFrom, eveningTo+1):
        evening = orders.filter(time_begin__hour=i)
    ans = []
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
    ans.append(top1)
    ans.append(top2)
    ans.append(top3)
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
    ans.append(top1)
    ans.append(top2)
    ans.append(top3)
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
    ans.append(top1)
    ans.append(top2)
    ans.append(top3)
    return Table6(ans)


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
    ans = []
    for i in range(0, int(n*(percent/100))):
        ans.append(cars[i][1])
    return Table7(ans)


def query8(days):#returns pair(customer, amount)
    customers = Customer.objects.all()
    orders = Order.objects.all().filter(time_begin__gte=datetime.date.today() - datetime.timedelta(days=days))
    charges = Charge.objects.all().filter(time__gte=datetime.date.today() - datetime.timedelta(days=days))
    ans = []
    for e in customers:
        current = orders.filter(Customer = e)
        amount = 0
        for c in current:
            amount += charges.filter(car=c.car).filter(time__day=c.time_begin.day).count()
        ans.append((e, amount))
    return Table8(ans)


def query9(days):#returns list of pairs(workshop, amount)
    provided_parts = ProvidedPart.objects.all().filter(time_of_providing=datetime.date.today() - datetime.timedelta(days=days))
    workshops = Workshop.objects.all()
    ws = []
    amount = []
    for w in workshops:
        ws.append(w)
        amount.append(provided_parts.filter(workshop=w).count())
    return Table9([ws, amount])


def query10():#returs car model
    provided_parts = ProvidedPart.objects.all()
    charges = Charge.objects.all()
    cars = Car.objects.all()
    max = 0
    best = cars[0]
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
    return Table10([best.model])

