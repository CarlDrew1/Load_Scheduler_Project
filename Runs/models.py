from django.db import models
from django.contrib.auth.models import User


class Runs(models.Model):
    run = models.CharField(max_length=10)
    driver = models.CharField(max_length=50)
    truck = models.CharField(max_length=50)
    trailer_1 = models.CharField(max_length=50)
    trailer_2 = models.CharField(max_length=50)
    load_comments = models.CharField(max_length=255)
    return_load_comments = models.CharField(max_length=255)
    depart_date = models.DateField()
    depart_time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()
