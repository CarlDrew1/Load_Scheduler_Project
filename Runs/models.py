from django.db import models
from django.contrib.auth.models import User

import pandas as pd
from django.conf import settings
from django_pandas.io import read_frame

class staffname(models.Model):
    fullname=models.CharField(max_length=50)
    objects = models.Manager()

    def __str__(self):
        return self.fullname


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
        BC510=models.CharField(max_length=10, default='No')
        A125=models.CharField(max_length=10, default='No')
        A125B=models.CharField(max_length=10, default='No')
        ASJ583=models.CharField(max_length=10, default='No')
        AZP219=models.CharField(max_length=10, default='No')
        B373J=models.CharField(max_length=10, default='No')
        BC503=models.CharField(max_length=10, default='No')
        BC503B=models.CharField(max_length=10, default='No')
        BC506=models.CharField(max_length=10, default='No')
        BC506B=models.CharField(max_length=10, default='No')
        BC507=models.CharField(max_length=10, default='No')
        BC507B=models.CharField(max_length=10, default='No')
        BC509=models.CharField(max_length=10, default='No')
        BC509B=models.CharField(max_length=10, default='No')
        BC510B=models.CharField(max_length=10, default='No')
        BC511=models.CharField(max_length=10, default='No')
        BC511B=models.CharField(max_length=10, default='No')
        BC513B=models.CharField(max_length=10, default='No')
        BC514B=models.CharField(max_length=10, default='No')
        BC516=models.CharField(max_length=10, default='No')
        BC516B=models.CharField(max_length=10, default='No')
        BC518=models.CharField(max_length=10, default='No')
        BC518B=models.CharField(max_length=10, default='No')
        BC519B=models.CharField(max_length=10, default='No')
        BC520B=models.CharField(max_length=10, default='No')
        BC601=models.CharField(max_length=10, default='No')
        BC601B=models.CharField(max_length=10, default='No')
        BCF001=models.CharField(max_length=10, default='No')
        BCF002=models.CharField(max_length=10, default='No')
        BCF002B=models.CharField(max_length=10, default='No')
        BCF004=models.CharField(max_length=10, default='No')
        BCF005=models.CharField(max_length=10, default='No')
        BCF005B=models.CharField(max_length=10, default='No')
        FC401=models.CharField(max_length=10, default='No')
        FC402=models.CharField(max_length=10, default='No')
        FC403=models.CharField(max_length=10, default='No')
        FC404=models.CharField(max_length=10, default='No')
        FC408=models.CharField(max_length=10, default='No')
        FC409=models.CharField(max_length=10, default='No')
        CS403=models.CharField(max_length=10, default='No')
        SC403=models.CharField(max_length=10, default='No')
        U2982=models.CharField(max_length=10, default='No')
        Ole_Blue=models.CharField(max_length=10, default='No')
        GMU582=models.CharField(max_length=10, default='No')
        ST50_REAR=models.CharField(max_length=10, default='No')
        W469D=models.CharField(max_length=10, default='No')
        SW304=models.CharField(max_length=10, default='No')
        BCF003=models.CharField(max_length=10, default='No')
        SC301=models.CharField(max_length=10, default='No')
        ST50_Front=models.CharField(max_length=10, default='No')
        MT4028=models.CharField(max_length=10, default='No')
        P839B=models.CharField(max_length=10, default='No')
        SK401=models.CharField(max_length=10, default='No')
        DJC531=models.CharField(max_length=10, default='No')
        NI4214=models.CharField(max_length=10, default='No')
        GQS618=models.CharField(max_length=10, default='No')
        DYS67=models.CharField(max_length=10, default='No')
        ST72_Rear=models.CharField(max_length=10, default='No')
        S2632=models.CharField(max_length=10, default='No')
        FD402=models.CharField(max_length=10, default='No')
        ZK7820=models.CharField(max_length=10, default='No')
        BC508=models.CharField(max_length=10, default='No')
        SW302=models.CharField(max_length=10, default='No')
        SW401=models.CharField(max_length=10, default='No')
        BC508B=models.CharField(max_length=10, default='No')
        Ole_Yellow=models.CharField(max_length=10, default='No')
        Q602A_Rear=models.CharField(max_length=10, default='No')
        S2631=models.CharField(max_length=10, default='No')
        RH3415=models.CharField(max_length=10, default='No')
        SC402=models.CharField(max_length=10, default='No')
        N771A=models.CharField(max_length=10, default='No')
        ST61_Rear=models.CharField(max_length=10, default='No')
        FUM497=models.CharField(max_length=10, default='No')
        BC603=models.CharField(max_length=10, default='No')
        SK306=models.CharField(max_length=10, default='No')
        SW301=models.CharField(max_length=10, default='No')
        FD401=models.CharField(max_length=10, default='No')
        Ole_Blue=models.CharField(max_length=10, default='No')
        SK402=models.CharField(max_length=10, default='No')
        SR401=models.CharField(max_length=10, default='No')
        R705S=models.CharField(max_length=10, default='No')
        M339B=models.CharField(max_length=10, default='No')
        EWM744=models.CharField(max_length=10, default='No')
        N8017=models.CharField(max_length=10, default='No')
        SK304=models.CharField(max_length=10, default='No')
        M928M=models.CharField(max_length=10, default='No')
        SK303=models.CharField(max_length=10, default='No')
        Ole_Yellow=models.CharField(max_length=10, default='No')


       
        

        objects = models.Manager()

        def __str__(self):
            return self.Truck

        
#Permit convert to DF and truck list
qs = Permit.objects.all()
df = read_frame(qs).set_index('Truck')
df2 = read_frame(qs)
trucklist= list(df2.Truck)
trucklistsorted = sorted(trucklist)
newlis = [(x , x) for x in trucklistsorted]

staff = staffname.objects.all()
staffdf = read_frame(staff)
stafflist = list(staffdf.fullname)
staffsort = sorted(stafflist)
stafflisttuples = [(x , x) for x in staffsort]


class routes(models.Model):
    route = models.CharField(max_length=6)
    objects = models.Manager()

    def __str__(self):
        return self.route


root = routes.objects.all()
routedf = read_frame(root)
routelist = list(routedf.route)
routelistsort = sorted(routelist)
routelisttuples = [(x , x) for x in routelistsort]


class front_trailer(models.Model):
    ftrailer = models.CharField(max_length=12)
    objects = models.Manager()

    def __str__(self):
        return self.ftrailer

ft = front_trailer.objects.all()
ftdf = read_frame(ft)
ftlist = list(ftdf.ftrailer)
ftlistsort = sorted(ftlist)
ftlisttuples = [(x , x) for x in ftlistsort]

class back_trailer(models.Model):
    btrailer = models.CharField(max_length=12)
    objects = models.Manager()

    def __str__(self):
        return self.btrailer

bt = back_trailer.objects.all()
btdf = read_frame(bt)
btlist = list(btdf.btrailer)
btlistsort = sorted(btlist)
btlisttuples = [(x , x) for x in btlistsort]


class Runs(models.Model):
    
    run = models.CharField(choices=routelisttuples, max_length=10)
    driver = models.CharField(choices=stafflisttuples,max_length=50,null=True, blank=True)
    truck = models.CharField(choices=newlis,max_length=50)
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
    planning_date = models.DateField(auto_now_add=True)
    foodstuffs = models.IntegerField(blank=True, default=0, null=True,)
    gib = models.DecimalField(decimal_places=1, max_digits=4, blank=True, default=0, null=True,)
    run_details = models.CharField(max_length=50, blank=True, null=True,)
    weight = models.IntegerField(blank=True, default=0, null=True,)
    cubic = models.DecimalField(decimal_places=1, max_digits=4, blank=True, default=0, null=True,)

    def Unit_Permitted(self):
        permitted = (df[self.trailer_1][self.truck])
        return permitted

    def __str__(self):
        return self.run
   

