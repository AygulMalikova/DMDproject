from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return render(request, 'core/index.html')


def query1(request):
    from .queries import query1
    text = "A customer claims she forgot her bag in a car and asks to help. " \
           "She was using cars several times this day, " \
           "but she believes the right car was red and its plate starts with “AN”. " \
           "Find all possible cars that match the description."
    # sql = "SELECT * FROM cars WHERE color = "
    context = {"text": text, "query": query1()}
    return render(request, 'core/query.html', context)


def query2(request):
    text = "Company management wants to get a statistics on the efficiency of charging stations utilization. " \
           "Given a date, compute how many sockets were occupied each hour."
    context = {'text': text}
    return render(request, 'core/query.html', context)


def query3(request):
    text = "Company management considers using price increasing coefficients. " \
           "They need to gather statistics for one week on how many cars are busy " \
           "(% to the total amount of taxis) during the morning (7AM - 10 AM), " \
           "afternoon (12AM - 2PM) and evening (5PM - 7PM) time."
    context = {'text': text}
    return render(request, 'core/query.html', context)


def query4(request):
    text = "A customer claims that he was charged twice for the trip, " \
           "but he can’t say exactly what day it happened " \
           "(he deleted notification from his phone and he is too lazy to ask the bank), " \
           "so you need to check all his payments for the last month to be be sure that nothing was doubled."
    context = {'text': text}
    return render(request, 'core/query.html', context)


def query5(request):
    text = "The department of development has requested the following statistics: " \
        "- Average distance a car has to travel per day to customer’s order location - Average trip duration"\
        " Given a date as an input, compute the statistics above."
    context = {'text': text}
    return render(request, 'core/query.html', context)


def query6(request):
    text = "In order to accommodate traveling demand, " \
           "the company decided to distribute cars according to demand locations. " \
           "Your task is to compute top-3 most popular pick-up locations and travel destination for each time of day: " \
           "morning (7am-10am), afternoon (12am-2pm) and evening (5pm-7pm)."
    context = {'text': text}
    return render(request, 'core/query.html', context)


def query7(request):
    text = "Despite the wise management, the company is going through hard times " \
           "and can’t afford anymore to maintain the current amount of self-driving cars. " \
           "The management decided to stop using 10% of all self-driving cars, " \
           "which take least amount of orders for the last 3 months."
    context = {'text': text}
    return render(request, 'core/query.html', context)


def query8(request):
    text = "The company management decided to participate in the research on " \
           "“does customer location of residence depend on " \
           "how many charging station the self-driving cars was using the same day”. " \
           "Now you as DB developer need to provide this data. " \
           "You’ve decided to collect the data for each day within one month and then sum them up."
    context = {'text': text}
    return render(request, 'core/query.html', context)


def query9(request):
    text = "The company management decided to optimize repair costs " \
           "by buying parts in bulks from providers for every workshop. " \
           "Help them decide which parts are used the most every week " \
           "by every workshop and compute the necessary amount of parts to order."
    context = {'text': text}
    return render(request, 'core/query.html', context)


def query10(request):
    text = "The company management decided to cut costs by getting rid of the most expensive car to maintain. " \
           "Find out which car type has had the highest average (per day) cost of repairs and charging (combined)."
    context = {'text': text}
    return render(request, 'core/query.html', context)


