from django.db import models
from django.contrib.auth.models import User
from .permit import permit_call
import pandas as pd
from django.conf import settings


from django_pandas.io import read_frame




class Permit(models.Model):
        Truck =models.CharField(max_length=50)
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
        objects = models.Manager()




    

qs = Permit.objects.all()
df = read_frame(qs).set_index('Truck')



class Runs(models.Model):
    vehicles = [('BEVS BEAUTY', 'BEVS BEAUTY'),
    ('BORN TO RUN','BORN TO RUN'), ('BROTHERS IN ARMS', 'BROTHERS IN ARMS'),('CHARLOTTES WEB','CHARLOTTES WEB'),('CLUDEN GREEN', 'CLUDEN GREEN'),('COASTAL TRADER', 'COASTAL TRADER'),('DANCING IN THE DARK', 'DANCING IN THE DARK'),('DEWEY LOUIE', 'DEWEY LOUIE'),
    ('FIFTY SHADES', 'FIFTY SHADES'),('GREEN ADDICTION', 'GREEN ADDICTION'),('GREEN CURRY', 'GREEN CURRY'),('DREGREEN DREAMAM', 'GREEN DREAM'),('GREEN EGGS', 'GREEN EGGS'),('GREEN ENVY', 'GREEN ENVY'),('GREEN GOBLIN', 'GREEN GOBLIN'),('GREEN GODDESS', 'GREEN GODDESS'),
    ('GREEN GROCER', 'GREEN GROCER'),('GREEN IVY', 'GREEN IVY'),('GREEN MAISE', 'GREEN MAISE'),('GREEN MILE', 'GREEN MILE'),('GREEN MILKY', 'GREEN MILKY'),('GREEN MIST', 'GREEN MIST'),('GREEN STRALLIS', 'GREEN STRALLIS'),('GREEN TRUMP', 'GREEN TRUMP'),
    ('HARD ANTLER', 'HARD ANTLER'),('HOT LOUIE', 'HOT LOUIE'),('ICE LOUIE', 'ICE LOUIE'),('JELLEY BABY', 'JELLEY BABY'),('KING LOUIE', 'KING LOUIE'),('LOYAL', 'LOYAL'),('PASTA LOUIE', 'PASTA LOUIE'),('STAR ATTRACTION', 'STAR ATTRACTION'), ('STAR LOUIE', 'STAR LOUIE'),
    ('THE DRIFTER', 'THE DRIFTER'),('THE GUV', 'THE GUV'),('THUNDER ROAD', 'THUNDER ROAD'),('Z LAST', 'Z LAST')]
    front = [("H180J","H180J"),
    ("FC505","FC505"),("FC503","FC503"),("FC504","FC504"),("M441R","M441R"),("Q738U","Q738U"),
    ("BC606","BC606"),("BC604","BC604"),("BC605","BC605"),("BC607","BC607"),("BC608","BC608"),("BC602","BC602"),("BC619","BC619"),("BC603","BC603"),("BC615","BC615"),("BC620","BC620"),("BC609","BC609"),("FC502","FC502"),
    ("BC614","BC614"), ("BC621","BC621"),("BC610","BC610"),("BC622","BC622"),("BC623","BC623"),]
    back =[
    ("BC606B","BC606B"),("BC604B","BC604B"),("BC605B","BC605B"),("BC607B","BC607B"),("BC608B","BC608B"),("BC602B","BC602B"),("BC619B","BC619B"),("BC603B","BC603B"),
    ("BC615B","BC615B"),("BC620B","BC620B"),("BC609B","BC609B"),("FC501","FC501"),("BC614B","BC614B"),("BC621B","BC621B"),("BC610B","BC610B"),("5Y411","5Y411"),("BC622B","BC622B"),
    ("BC623B","BC623B")]
    route=[("FCC","FCC"),("CHC1","CHC1"),("CHC2","CHC2"),("CHC3","CHC3"),("CHC4","CHC4"),("CHC5","CHC5"),("CHC6","CHC6"),("CCI","CCI"),	("CHIG","CHIG"),("FCI","FCI"),("CHI","CHI"),("CHI2","CHI2"),("FCD","FCD"),("CHD1","CHD1"),("CHD2","CHD2"),	
    ("CHD3","CHD3"),("CHD4","CHD4"),("CHD5","CHD5"),("CHD6","CHD6"),("CBN","CBN"),("CBN1","CBN1"),("CHN","CHN"),("CHN1","CHN1"),("CHN2","CHN2"),("FCT","FCT"),("CHT1","CHT1"),("CHT2","CHT2"),("CHW","CHW"),("CHW1","CHW1"),]
    drivername=[("Aaron Boys","Aaron Boys"),("Allan Hunt","Allan Hunt"),("Allan Woodfield","Allan Woodfield"),("Amanda Brown","Amanda Brown"),("Andrew Donehue","Andrew Donehue"),("Andrew Shaw","Andrew Shaw"),("Antoine Aulnette","Antoine Aulnette"),
    ("Austin Aitcheson","Austin Aitcheson"),("Barry Milne","Barry Milne"),("Ben Rapley","Ben Rapley"),("Blair Murphy","Blair Murphy"),("Brad Cheyne","Brad Cheyne"),("Brian George Greer","Brian George Greer"),("Brian Kenworthy","Brian Kenworthy"),("Bruce Mclean","Bruce Mclean"),
    ("Carl Laffey","Carl Laffey"),("Charmaine Proudman","Charmaine Proudman"),("Chontelle Brown","Chontelle Brown"),("Chris Bell","Chris Bell"),("Chris Erskine","Chris Erskine"),("Conrad Herbert","Conrad Herbert"),("Craig Hewlett","Craig Hewlett"),("Daniel Miller","Daniel Miller"),("Daniel Munro","Daniel Munro"),
    ("Darrell Clark","Darrell Clark"),("David Cross","David Cross"),("David Dunn","David Dunn"),("David Woodill","David Woodill"),("Deane Rodgers","Deane Rodgers"),("Dennis Brennan","Dennis Brennan"),("Dion Dunlop","Dion Dunlop"),("Duncan McCorkindale","Duncan McCorkindale"),("Eden Haulage","Eden Haulage"),
    ("Garry Kenton","Garry Kenton"),("Gary Smith","Gary Smith"),("Gene Latchford","Gene Latchford"),("Geoff Roper","Geoff Roper"),("Glen Clarkson","Glen Clarkson"),("Glen Tod","Glen Tod"),("Glen Redmond","Glen Redmond"),("Glenn Reeves","Glenn Reeves"),("Graeme Yianakis","Graeme Yianakis"),
    ("Grant Robertson","Grant Robertson"),("Greg Hunt","Greg Hunt"),("Gurri Brar","Gurri Brar"),("Hina Hunt","Hina Hunt"),("Ian Tamepo","Ian Tamepo"),("James Eggers","James Eggers"),("James Watson","James Watson"),("Jamie Landreth","Jamie Landreth"),("Jamie Wessels","Jamie Wessels"),
    ("Jan Kurak","Jan Kurak"),("Jarred Matheson","Jarred Matheson"),("Jessie Wrigley","Jessie Wrigley"),("Joe Garrett","Joe Garrett"),("Joe Hodge","Joe Hodge"),("Joe Maehe","Joe Maehe"),("John Boulton","John Boulton"),("John Sayer","John Sayer"),("Kevin Ludemann","Kevin Ludemann"),
    ("Kevin Murphy","Kevin Murphy"),("Kym Parsons","Kym Parsons"),("Leigh Rout","Leigh Rout"),("Leon Cooze","Leon Cooze"),("Les Brooks","Les Brooks"),("Leslie Mortimer","Leslie Mortimer"),("Leslie Pennal","Leslie Pennal"),("Lindsay Mathers","Lindsay Mathers"),("Mangaldeep Singh","Mangaldeep Singh"),
    ("Matthew Doherty","Matthew Doherty"),("Michael Williams","Michael Williams"),("Michael Cotton","Michael Cotton"),("Michael Currie","Michael Currie"),("Michael Dennison","Michael Dennison"),("Michael O'reagan","Michael O'reagan"),("Michael Scobie","Michael Scobie"),("Michelle Young","Michelle Young"),
    ("Morgan Perry","Morgan Perry"),("Norman Ranford","Norman Ranford"),("Pare Pewhairangi","Pare Pewhairangi"),("Paul Taiatini","Paul Taiatini"),("Paul Tobin","Paul Tobin"),("Peter Donald","Peter Donald"),("Peter Stringer","Peter Stringer"),("Phillip Askin","Phillip Askin"),("Ravi Sharma","Ravi Sharma"),
    ("RDNZ - Daryl Harvey","RDNZ - Daryl Harvey"),("RDNZ - Mike Reiner","RDNZ - Mike Reiner"),("RDNZ - Nathan Smith","RDNZ - Nathan Smith"),("RDNZ - Nick Blackler","RDNZ - Nick Blackler"),("RDNZ - Phil Radford","RDNZ - Phil Radford"),("RDNZ - Phil Whitcombe","RDNZ - Phil Whitcombe"),("RDNZ - Sam Dampier","RDNZ - Sam Dampier"),
    ("Rex Sharp","Rex Sharp"),("Ricky Rodgers","Ricky Rodgers"),("Riki Gilchrist","Riki Gilchrist"),("Robbie Dee","Robbie Dee"),("Robert Keen","Robert Keen"),("Robert Steven Beck","Robert Steven Beck"),("Robin Given","Robin Given"),("Ron Matthews","Ron Matthews"),
    ("Ross Millard","Ross Millard"),("Ross Murdoch","Ross Murdoch"),("Russell Webb","Russell Webb"),("Scott Hamlin","Scott Hamlin"),("Shaun Mills","Shaun Mills"),("Sergey Antonov","Sergey Antonov"),("Shaun Kincaid","Shaun Kincaid"),("Stephen Wood","Stephen Wood"),
    ("Steve Day-Clarke","Steve Day-Clarke"),("Steve Nelson","Steve Nelson"),("Steven Arps","Steven Arps"),("Steven Mcara","Steven Mcara"),("Terry Duthie","Terry Duthie"),("Terry Lewis","Terry Lewis"),("Thomas Ruhl","Thomas Ruhl"),("Tim Mcdonald","Tim Mcdonald"),
    ("Trevor Kelliher","Trevor Kelliher"),("Wayne Redmond","Wayne Redmond"),("Wayne Kerr","Wayne Kerr"),]
    
    run = models.CharField(choices=route, max_length=10)
    driver = models.CharField(choices=drivername,max_length=50)
    truck = models.CharField(choices=vehicles, max_length=50)
    trailer_1 = models.CharField(choices=front,max_length=50)
    trailer_2 = models.CharField(choices=back, max_length=50, null=True, blank=True)
    load_comments = models.CharField(max_length=255)
    return_load_comments = models.CharField(max_length=255)
    depart_date = models.DateField()
    depart_time = models.TimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()
    Planned_depart_time = models.TimeField()

   
    def permit_call(self):
        permitted = (df[self.trailer_1][self.truck])
        return permitted


