import datetime

from .tables import CarTable, ChargeTable, OrderTable
from .models import Employee, VehicleEngineer, VehiclePark, Workshop, ProvidingManager, CarParts, Car, ChargingStation, Operator, Customer, Charge, Order, Payment
from django.contrib.gis.geoip2 import GeoIP2


def query1():
    cars = Car.objects.all().filter(car_plate__startswith='AN').filter(color='red')
    return CarTable(cars)


def query2(date):
    charges = Charge.objects.all().filter(time__day=date)
    amounts = []
    for i in range(24):
        amounts.append(charges.filter(time__hour=i))
    return ChargeTable(amounts)


def query3(morningFrom, morningTo, afternoonFrom, aftenoonTo, eveningFrom, eveningTo):
    orders = Order.objects.all().filter(time_begin__gte=datetime.date.today() - datetime.timedelta(days=7))
    orders1 = orders.filter(time_begin__hour=[7, 8, 9])
    orders2 = orders.filter(time_begin__hour=[12, 13])
    orders3 = orders.filter(time_begin__hour=[19, 20, 21])
    amount_cars = Car.objects.all().count()
    ans = []
    ans.append(orders1.count()/amount_cars)
    ans.append(orders2.count()/amount_cars)
    ans.append(orders3.count()/amount_cars)
    return OrderTable(ans)

def query4(customer):
    text = "A customer claims that he was charged twice for the trip, " \
           "but he can’t say exactly what day it happened " \
           "(he deleted notification from his phone and he is too lazy to ask the bank), " \
           "so you need to check all his payments for the last month to be be sure that nothing was doubled."
    payments = Payment.objects.all().filter(time_of_payment__gte=datetime.date.today() - datetime.timedelta(days = 30))
    payments.filter(order__customer=customer)
    payments = payments.order_by('time_of_payment')
    if len(payments) <= 1:
        return False
    last = payments[0]
    for e in payments[1:-1]:
        if e.order_id == last.order_id:
            return True
        last = e
    return False

def query5(date):
    text = "The department of development has requested the following statistics: " \
           "- Average distance a car has to travel per day to customer’s order location - Average trip duration" \
           " Given a date as an input, compute the statistics above."
    orders = Order.objects.all().filter(time_begin__day = date.day)
    distance = 0
    duration = 0
    for e in orders:
        first = GeoIP2.geos(e.location_car)
        second = GeoIP2.geos(e.location_end)
        distance+=first.distance(second)
        duration+=e.time_end-e.time_begin
    n = orders.count()
    return [distance/n, duration/n]

def query6(): #return 9 elements: top3 at the morning, top3 at the afternoon and top3 at the evening
    text = "In order to accommodate traveling demand, " \
           "the company decided to distribute cars according to demand locations. " \
           "Your task is to compute top-3 most popular pick-up locations and travel destination for each time of day: " \
           "morning (7am-10am), afternoon (12am-2pm) and evening (5pm-7pm)."
    orders = Order.objects.all()
    orders1 = orders.filter(time_begin__hour=[7, 8, 9])
    orders2 = orders.filter(time_begin__hour=[12, 13])
    orders3 = orders.filter(time_begin__hour=[19, 20, 21])
    ans = []
    #11111
    top1, top2, top3 = "", "", ""
    mx1,mx2,mx3 = 0, 0, 0
    for e in orders1:
        cur = orders1.filter(location_begin=e.location_begin)
        if mx3 < cur.count():
            mx3 = cur.count()
            top3 = e.location_begin
        if mx2<mx3:
            mx2, mx3 = mx3, mx2
            top2, top3 = top3, top2
        if mx1<mx2:
            mx1,mx2 = mx2, mx1
            top1, top2 = top2, top1
    ans.append(top1)
    ans.append(top2)
    ans.append(top3)
    #22222
    top1, top2, top3 = "", "", ""
    mx1, mx2, mx3 = 0, 0, 0
    for e in orders2:
        cur = orders2.filter(location_begin=e.location_begin)
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
    for e in orders3:
        cur = orders3.filter(location_begin=e.location_begin)
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
    return ans

def takeFirst(elem):
    return elem[0]
def query7():
    text = "Despite the wise management, the company is going through hard times " \
           "and can’t afford anymore to maintain the current amount of self-driving cars. " \
           "The management decided to stop using 10% of all self-driving cars, " \
           "which take least amount of orders for the last 3 months."
    orders = Order.objects.all().filter(time_begin__gte=datetime.date.today() - datetime.timedelta(days=90))
    n = Car.objects.all().count()
    cars = []
    for e in orders:
        current = orders.filter(car=e.car)
        cars.append((current.count, e.car))
    cars.sort(key=takeFirst)
    ans=[]
    for i in range(0, n):
        ans.append(cars[i][1])
    return ans

def query8():#returns pair(customer, amount)
    text = "The company management decided to participate in the research on " \
           "“does customer location of residence depend on " \
           "how many charging station the self-driving cars was using the same day”. " \
           "Now you as DB developer need to provide this data. " \
           "You’ve decided to collect the data for each day within one month and then sum them up."
    customers = Customer.objects.all()
    orders = Order.objects.all().filter(time_begin__gte=datetime.date.today() - datetime.timedelta(days=30))
    charges = Charge.objects.all().filter(time__gte=datetime.date.today() - datetime.timedelta(days=30))
    ans = []
    for e in customers:
        current = orders.filter(Customer = e)
        amount = 0
        for c in current:
            amount += charges.filter(car=c.car).filter(time__day=c.time_begin.day).count()
        ans.append((e, amount))
    return ans

def query9():#returns list of pairs(workshop, amount)
    text = "The company management decided to optimize repair costs " \
           "by buying parts in bulks from providers for every workshop. " \
           "Help them decide which parts are used the most every week " \
           "by every workshop and compute the necessary amount of parts to order."
    proivded_parts = ProvidedPart.objects.all().filter(time_begin__gte=datetime.date.today() - datetime.timedelta(days=42))
    workshops = Workshop.objects.all()
    ans = []
    for w in workshops:
        ans.append(w, proivded_parts.filter(workshop=w).count())

    return ans

def query10():#returs car
    text = "The company management decided to cut costs by getting rid of the most expensive car to maintain. " \
           "Find out which car type has had the highest average (per day) cost of repairs and charging (combined)."
    proivded_parts = ProvidedPart.objects.all()
    charges = Charge.objects.all()
    cars = Car.objects.all()
    mx = 0
    best = cars[0]
    for c in cars:
        used_parts = proivded_parts.filter(car_part__car=c)
        cur = 0
        for e in used_parts:
            cur += e.car_part.price
        used_charges = charges.filter(car=c)
        for e in used_charges:
            cur+=e.charging_station.price
        if mx<cur:
            mx = cur
            best = c
    return best