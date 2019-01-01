from .models import Dataset, Label
from rest_framework import serializers


class DatasetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dataset
        fields = ('dataset_name', 'number_of_records')
