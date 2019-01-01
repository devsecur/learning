from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import DatasetSerializer
from .models import Dataset


class DatasetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

#TODO Make API for everything working with https://www.django-rest-framework.org/tutorial/quickstart/
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
