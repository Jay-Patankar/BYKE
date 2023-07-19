from django.db import models


# Create your models here.


class Person(models.Model):
    UserName = models.CharField(max_length=30)
    Password = models.CharField(max_length=30)


class Passenger(models.Model):
    UserName = models.CharField(max_length=15)
    First_Name= models.CharField(max_length=30 , default="DEFAULT")
    Password = models.CharField(max_length=30)
    SourceLat = models.DecimalField(max_digits=20, decimal_places=15)
    SourceLon = models.DecimalField(max_digits=20, decimal_places=15)
    DestinationLat = models.DecimalField(max_digits=20, decimal_places=15)
    DestinationLon = models.DecimalField(max_digits=20, decimal_places=15)
    RideDate=models.DateTimeField()

class Driver(models.Model):
    UserName = models.CharField(max_length=15)
    First_Name= models.CharField(max_length=30 , default="DEFAULT")
    Password = models.CharField(max_length=30)
    SourceLat = models.DecimalField(max_digits=20, decimal_places=15)
    SourceLon = models.DecimalField(max_digits=20, decimal_places=15)
    DestinationLat = models.DecimalField(max_digits=20, decimal_places=15)
    DestinationLon = models.DecimalField(max_digits=20, decimal_places=15)
    RideDate=models.DateTimeField()
    
class Notification(models.Model):
    Source=models.CharField(max_length=300)
    Destination=models.CharField(max_length=300)
    Fare=models.IntegerField()
    DateTime=models.DateTimeField()
    Driver_Name=models.CharField(max_length=30 , default="DEFAULT")
    Passenger_Name=models.CharField(max_length=30 ,default="DEFAULT")
    Driver_Phone=models.CharField(max_length=15 , default="DEFAULT")
    Passenger_Phone=models.CharField(max_length=15 , default="DEFAULT")
