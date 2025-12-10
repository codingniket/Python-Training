from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField()


    def __str__(self):
        return self.name

class Vehicle(models.Model):
    number_plate = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=10)
    manufacturer = models.CharField(max_length=10)
    year = models.IntegerField()


    def __str__(self):
        return self.name