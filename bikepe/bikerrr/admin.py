from django.contrib import admin
from bikerrr.models import Bike, BikeCategory, Purchases, BikeCategoryColors, Colors
# Register your models here.

admin.site.register(Bike)
admin.site.register(BikeCategory)
admin.site.register(BikeCategoryColors)
admin.site.register(Colors)
admin.site.register(Purchases)
