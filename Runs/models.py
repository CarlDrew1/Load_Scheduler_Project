from django.db import models
from django.contrib.auth.models import User
from .permit import permit
import pandas as pd



df= pd.read_csv('/Users/Carl/Downloads/Permit.csv').set_index('0')




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
    ("BC614","BC614"), ("BC621","BC621"),("BC610","BC610"),("BC622","BC622"),("Ole Yella","Ole Yella"),("BC623","BC623"),]
    back =[
    ("BC606B","BC606B"),("BC604B","BC604B"),("BC605B","BC605B"),("BC607B","BC607B"),("BC608B","BC608B"),("BC602B","BC602B"),("BC619B","BC619B"),("BC603B","BC603B"),
    ("BC615B","BC615B"),("BC620B","BC620B"),("BC609B","BC609B"),("FC501","FC501"),("BC614B","BC614B"),("BC621B","BC621B"),("BC610B","BC610B"),("5Y411","5Y411"),("Ole Yellab","Ole Yellab"),("BC622B","BC622B"),
    ("BC623B","BC623B")]
    route=[("FCC","FCC"),("CHC1","CHC1"),("CHC2","CHC2"),("CHC3","CHC3"),("CHC4","CHC4"),("CHC5","CHC5"),("CHC6","CHC6"),("CCI","CCI"),	("CHIG","CHIG"),("FCI","FCI"),("CHI","CHI"),("CHI2","CHI2"),("FCD","FCD"),("CHD1","CHD1"),("CHD2","CHD2"),	
    ("CHD3","CHD3"),("CHD4","CHD4"),("CHD5","CHD5"),("CHD6","CHD6"),("CBN","CBN"),("CBN1","CBN1"),("CHN","CHN"),("CHN1","CHN1"),("CHN2","CHN2"),("FCT","FCT"),("CHT1","CHT1"),("CHT2","CHT2"),("CHW","CHW"),("CHW1","CHW1"),]
    drivername=[("1","Aaron Boys"),("2","Allan Hunt"),("3","Allan Woodfield"),("4","Amanda Brown"),("5","Andrew Donehue"),("6","Andrew Shaw"),("7","Antoine Aulnette"),("8","Austin Aitcheson"),("9","Barry Milne"),
    ("10","Ben Rapley"),("11","Blair Murphy"),("12","Brad Cheyne"),("13","Brian George Greer"),("14","Brian Kenworthy"),("15","Bruce Jeffries"),("16","Bruce Mclean"),("17","Carl Laffey"),
    ("18","Charmaine Proudman"),("19","Chathura Don"),("20","Chontelle Brown"),("21","Chris Bell"),("22","Chris Erskine"),("23","Conrad Herbert"),("24","Craig Hewlett"),("25","Daniel Miller"),("26","Daniel Munro"),
    ("27","Darrell Clark"),("28","Dave Richards"),("29","David Cross"),("30","David Dunn"),("31","David Petersen"),("32","David Woodill"),("33","Deane Rodgers"),("34","Dennis Brennan"),("35","Dion Dunlop"),("36","Duncan McCorkindale"),
    ("37","Eden Haulage"),("38","Euan Dickie"),("39","Garry Kenton"),("40","Gary Smith"),("41","Gene Latchford"),("42","Glen Clarkson"),("43","Glen Tod"),("44","Glen Redmond"),("45","Glenn Reeves"),("46","Graeme Yianakis"),
    ("47","Grant Robertson"),("48","Greg Hunt"),("49","Gurri Brar"),("50","Hina Hunt"),("51","Ian Tamepo"),("52","James Eggers"),("53","James Watson"),("54","Jamie Landreth"),("55","Jamie Wessels"),("56","Jan Kurak"),
    ("57","Jarred Matheson"),("58","Jessie Wrigley"),("59","Joe Garrett"),("60","John Boulton"),("61","John Dodson-Cook"),("62","John Sayer"),("63","Kevin Ludemann"),("64","Kevin Murphy"),("65","Kym Parsons"),("66","Leigh Rout"),("67","Leon Cooze"),
    ("68","Les Brooks"),("69","Leslie Mortimer"),("70","Lindsay Mathers"),("71","Mangaldeep Singh"),("72","Mark Rosson"),("73","Matthew Doherty"),("74","Michael Williams"),("75","Michael Cotton"),("76","Michael Currie"),("77","Michael Dennison"),
    ("78","Michael O'reagan"),("79","Michael Scobie"),("80","Michelle Young"),("81","Morgan Perry"),("82","Neil Tomson"),("83","Nigel Johnson"),("84","Norman Ranford"),("85","Pare Pewhairangi"),("86","Paul Taiatini"),
    ("87","Paul Tobin"),("88","Peter Donald"),("89","Peter Stringer"),("90","Phillip Askin"),("91","RDNZ - Daryl Harvey"),("92","RDNZ - Mike Reiner"),("93","RDNZ - Mike Ward"),("94","RDNZ - Nathan Smith"),("95","RDNZ - Nick Blackler"),
    ("96","RDNZ - Phil Whitcombe"),("97","RDNZ - Sam Dampier"),("98","Rex Sharp"),("99","Ricky Rodgers"),("100","Riki Gilchrist"),("101","Rita Robinson"),("102","Robbie Dee"),("103","Robert Steven Beck"),("104","Robin Given"),
    ("105","Ron Matthews"),("106","Ross Millard"),("107","Ross Murdoch"),("108","Russell Webb"),("109","Sachin Kapoor"),("110","Scott Hamlin"),("111","Sergey Antonov"),("112","Shaun Kincaid"),("113","Stephen Wood"),("114","Steve Day-Clarke"),
    ("115","Steve Nelson"),("116","Steven Arps"),("117","Steven Mcara"),("118","Terry Duthie"),("119","Terry Lewis"),("120","Thomas Ruhl"),("121","Tim Mcdonald"),("122","Trevor Kelliher"),("123","Wayne Court"),("124","Wayne Redmond"),
    ("125","Vowles Transport"),("126","Wayne Kerr"),("127","Wayne Redmond")]
    
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

    def permit(self):
        permitted = (df[self.trailer_1][self.truck])
        return permitted 
