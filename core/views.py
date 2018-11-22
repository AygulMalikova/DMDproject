# coding=utf-8
from django.shortcuts import render
import datetime
from django.contrib.gis.geoip2 import GeoIP2

def index(request):
    return render(request, 'core/index.html')


def query1(request):
    from .queries import query1
    text = "A customer claims she forgot her bag in a car and asks to help. " \
           "She was using cars several times this day, " \
           "but she believes the right car was red and its plate starts with “AN”. " \
           "Find all possible cars that match the description."
    if request.method == 'GET':
        plate = "AN"
        color = "red"
        result = query1(plate, color)
        context = {"text": text, "result": result, "plate": plate, "color": color}
        return render(request, 'core/query1.html', context)

    if request.method == 'POST':
        plate = request.POST['plate']
        color = request.POST['color']
        result = query1(plate, color)
        context = {"text": text, "result": result, "plate": plate, "color": color}
        return render(request, 'core/query1.html', context)


def query2(request):
    from .queries import query2
    text = "Company management wants to get a statistics on the efficiency of charging stations utilization. " \
           "Given a date, compute how many sockets were occupied each hour."
    if request.method == 'GET':
        dateyear = 2018
        print
        datemonth = 11
        dateday = 21
        date = datetime.date(dateyear, datemonth, dateday)
        result = query2(date)
        context = {"text": text, "result": result,  "year": dateyear, "month": datemonth, "day": dateday}
        return render(request, 'core/query2.html', context)

    if request.method == 'POST':
        dateyear = int(request.POST['year'])
        datemonth = int(request.POST['month'])
        dateday = int(request.POST['day'])
        date = datetime.date(dateyear, datemonth, dateday)
        result = query2(date)
        context = {"text": text, "result": result, "year": dateyear, "month": datemonth, "day": dateday}
        return render(request, 'core/query2.html', context)


def query3(request):
    from .queries import query3
    text = "Company management considers using price increasing coefficients. " \
           "They need to gather statistics for one week on how many cars are busy " \
           "(% to the total amount of taxis) during the morning (7AM - 10 AM), " \
           "afternoon (12AM - 2PM) and evening (5PM - 7PM) time."
    if request.method == 'GET':
        morning_from = 7
        morning_to = 10
        afternoon_from = 12
        afternoon_to = 14
        evening_from = 17
        evening_to = 19
        result = query3(morning_from, morning_to, afternoon_from, afternoon_to, evening_from, evening_to)
        context = {"text": text, "result": result,
                   "morning_from": morning_from,
                   "morning_to": morning_to,
                   "afternoon_from": afternoon_from,
                   "afternoon_to": afternoon_to,
                   "evening_from": evening_from,
                   "evening_to": evening_to
                   }
        return render(request, 'core/query3.html', context)

    if request.method == 'POST':
        morning_from = request.POST['morning_from']
        morning_to = request.POST['morning_to']
        afternoon_from = request.POST['afternoon_from']
        afternoon_to = request.POST['afternoon_to']
        evening_from = request.POST['evening_from']
        evening_to = request.POST['evening_to']
        result = query3(morning_from, morning_to, afternoon_from, afternoon_to, evening_from, evening_to)
        context = {"text": text, "result": result,
                   "morning_from": morning_from,
                   "morning_to": morning_to,
                   "afternoon_from": afternoon_from,
                   "afternoon_to": afternoon_to,
                   "evening_from": evening_from,
                   "evening_to": evening_to
                   }
        return render(request, 'core/query3.html', context)


def query4(request):
    text = "A customer claims that he was charged twice for the trip, " \
           "but he can’t say exactly what day it happened " \
           "(he deleted notification from his phone and he is too lazy to ask the bank), " \
           "so you need to check all his payments for the last month to be be sure that nothing was doubled."
    if request.method == 'GET':
        username = "Mark"
        result = query4(username)
        context = {"text": text, "result": result, "username": username}
        return render(request, 'core/query2.html', context)

    # if request.method == 'POST':
    #     # date = request.POST['date']
    #     result = query4(date)
    #     context = {"text": text, "result": result, "date": date}
    #     return render(request, 'core/query2.html', context)


def query5(request):
    from .queries import query5
    text = "The department of development has requested the following statistics: " \
        "- Average distance a car has to travel per day to customer’s order location - Average trip duration"\
        " Given a date as an input, compute the statistics above."
    if request.method == 'GET':
        d = date(2005, 7, 14)
        result = query5(d)
        print (result)
    # context = {"text": text, "result": result, "date": d}
        return render(request, 'core/query5.html',)

    # if request.method == 'POST':
    #     date = request.POST['date']
    #     result = query5(date)
    #     context = {"text": text, "result": result, "date": date}
    #     return render(request, 'core/query5.html', context)


def query6(request):
    text = "In order to accommodate traveling demand, " \
           "the company decided to distribute cars according to demand locations. " \
           "Your task is to compute top-3 most popular pick-up locations and travel destination for each time of day: " \
           "morning (7am-10am), afternoon (12am-2pm) and evening (5pm-7pm)."
    context = {'text': text}
    return render(request, 'core/header.html', context)


def query7(request):
    text = "Despite the wise management, the company is going through hard times " \
           "and can’t afford anymore to maintain the current amount of self-driving cars. " \
           "The management decided to stop using 10% of all self-driving cars, " \
           "which take least amount of orders for the last 3 months."
    context = {'text': text}
    return render(request, 'core/header.html', context)


def query8(request):
    text = "The company management decided to participate in the research on " \
           "“does customer location of residence depend on " \
           "how many charging station the self-driving cars was using the same day”. " \
           "Now you as DB developer need to provide this data. " \
           "You’ve decided to collect the data for each day within one month and then sum them up."
    context = {'text': text}
    return render(request, 'core/header.html', context)


def query9(request):
    from .queries import query9
    text = "The company management decided to optimize repair costs " \
           "by buying parts in bulks from providers for every workshop. " \
           "Help them decide which parts are used the most every week " \
           "by every workshop and compute the necessary amount of parts to order."
    result = query9()
    context = {'text': text, "result": result}

    return render(request, 'core/header.html', context)


def query10(request):
    from .queries import query10
    text = "The company management decided to cut costs by getting rid of the most expensive car to maintain. " \
           "Find out which car type has had the highest average (per day) cost of repairs and charging (combined)."
    result = query9()
    context = {'text': text, "result": result}
    return render(request, 'core/header.html', context)


