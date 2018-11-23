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
    else:
        return redirect('/1')


def query2(request):
    from .queries import query2
    text = "Company management wants to get a statistics on the efficiency of charging stations utilization. " \
           "Given a date, compute how many sockets were occupied each hour."
    if request.method == 'GET':
        dateyear = 2018
        datemonth = 11
        dateday = 21
        date = datetime.date(dateyear, datemonth, dateday)
        result = query2(date)
        context = {"text": text, "result": result, "year": dateyear, "month": datemonth, "day": dateday}
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
    from .queries import query4
    text = "A customer claims that he was charged twice for the trip, " \
           "but he can’t say exactly what day it happened " \
           "(he deleted notification from his phone and he is too lazy to ask the bank), " \
           "so you need to check all his payments for the last month to be be sure that nothing was doubled."
    if request.method == 'GET':
        username = "Mark"
        result = query4(username)
        context = {"text": text, "result": result, "username": username}
        return render(request, 'core/query4.html', context)

    if request.method == 'POST':
        username = request.POST['username']
        result = query4(username)
        context = {"text": text, "result": result, "username": username}
        return render(request, 'core/query4.html', context)


def query5(request):
    from .queries import query5
    text = "The department of development has requested the following statistics: " \
           "- Average distance a car has to travel per day to customer’s order location - Average trip duration" \
           " Given a date as an input, compute the statistics above."
    if request.method == 'GET':
        dateyear = 2018
        datemonth = 11
        dateday = 21
        date = datetime.date(dateyear, datemonth, dateday)
        result = query5(date)
        context = {"text": text, "result": result, "year": dateyear, "month": datemonth, "day": dateday}
        return render(request, 'core/query5.html', context)

    if request.method == 'POST':
        dateyear = int(request.POST['year'])
        datemonth = int(request.POST['month'])
        dateday = int(request.POST['day'])
        date = datetime.date(dateyear, datemonth, dateday)
        result = query5(date)
        context = {"text": text, "result": result, "year": dateyear, "month": datemonth, "day": dateday}
        return render(request, 'core/query5.html', context)


def query6(request):
    from .queries import query6
    text = "In order to accommodate traveling demand, " \
           "the company decided to distribute cars according to demand locations. " \
           "Your task is to compute top-3 most popular pick-up locations and travel destination for each time of day: " \
           "morning (7am-10am), afternoon (12am-2pm) and evening (5pm-7pm)."
    if request.method == 'GET':
        morning_from = 7
        morning_to = 10
        afternoon_from = 12
        afternoon_to = 14
        evening_from = 17
        evening_to = 19
        result = query6(morning_from, morning_to, afternoon_from, afternoon_to, evening_from, evening_to)
        context = {"text": text, "result": result,
                   "morning_from": morning_from,
                   "morning_to": morning_to,
                   "afternoon_from": afternoon_from,
                   "afternoon_to": afternoon_to,
                   "evening_from": evening_from,
                   "evening_to": evening_to
                   }
        return render(request, 'core/query6.html', context)

    if request.method == 'POST':
        morning_from = request.POST['morning_from']
        morning_to = request.POST['morning_to']
        afternoon_from = request.POST['afternoon_from']
        afternoon_to = request.POST['afternoon_to']
        evening_from = request.POST['evening_from']
        evening_to = request.POST['evening_to']
        result = query6(morning_from, morning_to, afternoon_from, afternoon_to, evening_from, evening_to)
        context = {"text": text, "result": result,
                   "morning_from": morning_from,
                   "morning_to": morning_to,
                   "afternoon_from": afternoon_from,
                   "afternoon_to": afternoon_to,
                   "evening_from": evening_from,
                   "evening_to": evening_to
                   }
        return render(request, 'core/query6.html', context)


def query7(request):
    from .queries import query7
    text = "Despite the wise management, the company is going through hard times " \
           "and can’t afford anymore to maintain the current amount of self-driving cars. " \
           "The management decided to stop using 10% of all self-driving cars, " \
           "which take least amount of orders for the last 3 months."
    if request.method == 'GET':
        percent = 10
        lastdays = 90
        result = query7(percent, lastdays)
        context = {"text": text, "result": result, "percent": percent, "days": lastdays}
        return render(request, 'core/query7.html', context)

    if request.method == 'POST':
        percent = int(request.POST['percent'])
        lastdays = int(request.POST['days'])
        result = query7(percent, lastdays)
        context = {"text": text, "result": result, "percent": percent, "days": lastdays}
        return render(request, 'core/query7.html', context)


def query8(request):
    from .queries import query8
    text = "The company management decided to participate in the research on " \
           "“does customer location of residence depend on " \
           "how many charging station the self-driving cars was using the same day”. " \
           "Now you as DB developer need to provide this data. " \
           "You’ve decided to collect the data for each day within one month and then sum them up."
    if request.method == 'GET':
        lastdays = 30
        result = query8(lastdays)
        context = {"text": text, "result": result, "days": lastdays}
        return render(request, 'core/query8.html', context)

    if request.method == 'POST':
        lastdays = int(request.POST['days'])
        result = query8(lastdays)
        context = {"text": text, "result": result, "days": lastdays}
        return render(request, 'core/query8.html', context)


def query9(request):
    from .queries import query9
    text = "The company management decided to optimize repair costs " \
           "by buying parts in bulks from providers for every workshop. " \
           "Help them decide which parts are used the most every week " \
           "by every workshop and compute the necessary amount of parts to order."
    if request.method == 'GET':
        lastdays = 42
        result = query9(lastdays)
        context = {"text": text, "result": result, "days": lastdays}
        return render(request, 'core/query9.html', context)

    if request.method == 'POST':
        lastdays = int(request.POST['days'])
        result = query9(lastdays)
        context = {"text": text, "result": result, "days": lastdays}
        return render(request, 'core/query9.html', context)


def query10(request):
    from .queries import query10
    text = "The company management decided to cut costs by getting rid of the most expensive car to maintain. " \
           "Find out which car type has had the highest average (per day) cost of repairs and charging (combined)."
    attribute = "model"
    result = query10()
    context = {'text': text, "result": result, "attribute": attribute}
    return render(request, 'core/query10.html', context)
