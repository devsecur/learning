from django.db import models


class Dataset(models.Model):
    dataset_name = models.CharField(max_length=200)
    number_of_records = models.IntegerField()


class Label(models.Model):
    label = models.CharField(max_length=200)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
