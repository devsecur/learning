from django.shortcuts import render
from django.http import HttpResponse

#TODO Make API for everything working with https://www.django-rest-framework.org/tutorial/quickstart/
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
