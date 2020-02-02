from django.db import models
from django.contrib.auth.models import User

import pandas as pd
from django.conf import settings
from django_pandas.io import read_frame

class staffname(models.Model):
    fullname=models.CharField(max_length=50)
    objects = models.Manager()


class Permit(models.Model):
        Truck =models.CharField(max_length=50)
        TBC=models.CharField(max_length=50)
        H180J=models.CharField(max_length=10)
        FC505=models.CharField(max_length=10)
        FC503=models.CharField(max_length=10)
        FC504=models.CharField(max_length=10)
        M441R=models.CharField(max_length=10)
        Q738U=models.CharField(max_length=10)
        BC606=models.CharField(max_length=10)
        BC606B=models.CharField(max_length=10)
        BC604=models.CharField(max_length=10)
        BC604B=models.CharField(max_length=10)
        BC605=models.CharField(max_length=10)
        BC605B=models.CharField(max_length=10)
        BC607=models.CharField(max_length=10)
        BC607B=models.CharField(max_length=10)
        BC608=models.CharField(max_length=10)
        BC608B=models.CharField(max_length=10)
        BC602=models.CharField(max_length=10)
        BC602B=models.CharField(max_length=10)
        BC619=models.CharField(max_length=10)
        BC619B=models.CharField(max_length=10)
        BC603=models.CharField(max_length=10)
        BC603B=models.CharField(max_length=10)
        BC615=models.CharField(max_length=10)
        BC615B=models.CharField(max_length=10)
        BC620=models.CharField(max_length=10)
        BC620B=models.CharField(max_length=10)
        BC609=models.CharField(max_length=10)
        BC609B=models.CharField(max_length=10)
        FC502=models.CharField(max_length=10)
        FC501=models.CharField(max_length=10)
        BC614=models.CharField(max_length=10)
        BC614B=models.CharField(max_length=10)
        BC621=models.CharField(max_length=10)
        BC621B=models.CharField(max_length=10)
        BC610=models.CharField(max_length=10)
        BC610B = models.CharField(max_length=10)
        BC622=models.CharField(max_length=10)
        BC622B=models.CharField(max_length=10)
        BC623=models.CharField(max_length=10)
        BC623B=models.CharField(max_length=10)
        Spare1=models.CharField(max_length=10)
        Spare2=models.CharField(max_length=10)
        Spare3=models.CharField(max_length=10)
        Spare4=models.CharField(max_length=10)
        Spare5=models.CharField(max_length=10)
        Spare6=models.CharField(max_length=10)
        Spare7=models.CharField(max_length=10)
        Spare8=models.CharField(max_length=10)
        Spare9=models.CharField(max_length=10)
        Spare10=models.CharField(max_length=10)
        objects = models.Manager()

        
#Permit convert to DF and truck list
qs = Permit.objects.all()
df = read_frame(qs).set_index('Truck')
df2 = read_frame(qs)
trucklist= list(df2.Truck)
newlis = [(x , x) for x in trucklist]

staff = staffname.objects.all()
staffdf = read_frame(staff)
stafflist = list(staffdf.fullname)
stafflisttuples = [(x , x) for x in stafflist]


class routes(models.Model):
    route = models.CharField(max_length=6)
    objects = models.Manager()

root = routes.objects.all()
routedf = read_frame(root)
routelist = list(routedf.route)
routelisttuples = [(x , x) for x in routelist]

class front_trailer(models.Model):
    ftrailer = models.CharField(max_length=6)
    objects = models.Manager()

ft = front_trailer.objects.all()
ftdf = read_frame(ft)
ftlist = list(ftdf.ftrailer)
ftlisttuples = [(x , x) for x in ftlist]

class back_trailer(models.Model):
    btrailer = models.CharField(max_length=6)
    objects = models.Manager()

bt = back_trailer.objects.all()
btdf = read_frame(bt)
btlist = list(btdf.btrailer)
btlisttuples = [(x , x) for x in btlist]


class Runs(models.Model):
    
    run = models.CharField(choices=routelisttuples, max_length=10)
    driver = models.CharField(choices=stafflisttuples,max_length=50,null=True, blank=True)
    truck = models.CharField(choices=newlis, max_length=50)
    trailer_1 = models.CharField(choices=ftlisttuples,max_length=50)
    trailer_2 = models.CharField(choices=btlisttuples, max_length=50, null=True, blank=True)
    load_comments = models.CharField(max_length=255,null=True, blank=True)
    return_load_comments = models.CharField(max_length=255, null=True, blank=True)
    depart_date = models.DateField()
    depart_time = models.TimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()
    Planned_depart_time = models.TimeField()
    finished_loading_time = models.TimeField(null=True, blank=True)

    def permit_call(self):
        permitted = (df[self.trailer_1][self.truck])
        return permitted
   

