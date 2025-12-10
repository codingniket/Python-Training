from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    mfdate = models.DateField()

def __str__(self):
    return self.name