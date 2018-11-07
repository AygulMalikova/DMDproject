from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):

   # template = loader.get_template('polls/index.html')
    return render(request, 'core/index.html')