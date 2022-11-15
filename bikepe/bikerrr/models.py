from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Colors(models.Model):

    name = models.CharField(max_length=16)

    def __str__(self):
        return f"Colors : {self.name}"

class BikeCategory(models.Model):
    
    name = models.CharField(max_length=100)
    stockCount = models.IntegerField(default=0)

    def __str__(self):
        return f"BikeCategory : {self.name}"


class BikeCategoryColors(models.Model):

    bikeCategory = models.ForeignKey(BikeCategory, on_delete=models.CASCADE)
    color = models.ForeignKey(Colors, on_delete=models.CASCADE)
    isAvailable = models.BooleanField(default=False)

    
class Bike(models.Model):

    type = models.ForeignKey(BikeCategory, on_delete=models.CASCADE)
    modelNumber = models.CharField(max_length=20,primary_key=True)
    color = models.CharField(max_length=10, null=True)
    warranty = models.IntegerField(default=0) # Assuming warranty is in days
    price = models.FloatField()

    def __str__(self):
        return f"{self.type} : {self.modelNumber}"


class Purchases(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    purchaseDate = models.DateTimeField(null=True)
    bikeInfo = models.ForeignKey(Bike, on_delete=models.CASCADE)

    def __str__(self):
        return f"Purchases : {self.user.username}"