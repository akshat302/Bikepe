from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from bikerrr.models import Bike, BikeCategory, Purchases
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
import json
from django.utils import timezone
from django.urls import reverse

app_name = "bikerrr"
# Create your views here.
def list_bikes(request):


    if not request.user.is_authenticated:
        return HttpResponse(status=401)

    if request.method == "GET":
        bikes = Bike.objects.values() 
        bike_info_list = []
        
        
        for bike in bikes:
            bike_info = {}
            bike_category_id = bike["type_id"]
            bike_type = BikeCategory.objects.get(pk=bike_category_id) 
            bike_info["modelNumber"] = bike["modelNumber"] 
            bike_info["color"] = bike["color"] 
            bike_info["warranty"] = str(bike["warranty"])
            bike_info["price"] = bike["price"] 
            bike_info["bike_category"] = bike_type.name 
            bike_info["stock_count"] = bike_type.stockCount 
            bike_info["available_colors"] = list(bike_type.bikecategorycolors_set.filter(isAvailable=True).values_list("color__name", flat=True)) # reverse
            bike_info_list.append(bike_info)

        content = {"bikes": bike_info_list}

        return HttpResponse(json.dumps(content), content_type="application/json")

def register(request):

    if request.method == "POST":

        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
        user.save()
        return HttpResponse(status=201)
    else:
        return HttpResponse(status=403)


def purchase_bike(request):
    
    if not request.user.is_authenticated: # status code - 403
        return HttpResponse(status=403)

    if request.method == "POST":

        data = request.POST
        model_number = data.get("model_number")
        purchase_date = timezone.now()

        bike_details = Bike.objects.filter(modelNumber=model_number).first()
        if bike_details is None:
            return HttpResponse(status=404)

        Purchases.objects.create(user=request.user, purchaseDate=purchase_date, bikeInfo=bike_details)
        stock_count = bike_details.type.stockCount-1
        bike_details.type.stockCount = stock_count
        bike_details.type.save()

        return HttpResponse(status=201)
    
    return HttpResponse(status=400) # bad request

def update_bike_details(request):

    if not request.user.is_superuser or not request.user.is_staff:
        return HttpResponse(status=401)
    
    if request.method == "POST":

        data = request.POST
        model_number = data.get("model_number")
    

        bike_attributes = Bike.objects.filter(modelNumber=model_number).first()
        if bike_attributes is None:
            return HttpResponse(status=400)

        color = data.get("bike_color")
        warranty = data.get("warranty")
        price = data.get("price")
        category = data.get("category_name")
        
        if category is not None:
            bike_category = BikeCategory.objects.filter(name=category).first()
            if bike_category is not None:
                bike_attributes.type = bike_category
            else:
                return HttpResponse("Category Not Found", status=404)
        if color is not None:
            bike_attributes.color = color
        if warranty is not None:
            bike_attributes.warranty = warranty
        if price is not None:
            bike_attributes.price = price

        bike_attributes.save()
        return HttpResponse(status=201)
    
    return HttpResponse(status=404)

def update_bikeCategory_details(request):

    if not request.user.is_superuser or not request.user.is_staff:
            return HttpResponse(status=401)

    if request.method == "POST":

        data = request.POST

        name = data.get("name")
        bike_category_attributes = BikeCategory.objects.filter(name=name).first()

        stockCount = data.get("stock_count")

        if stockCount is not None:
            bike_category_attributes.stockCount = stockCount
        
        bike_category_attributes.save()
        return HttpResponse(status=201)
    
    return HttpResponse(status=401)

def login_api(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=401)
    
    return HttpResponse(status=404)


def logout_api(request):

    logout(request)
    return HttpResponse(status=200)

def purchases(request):

    if not request.user.is_authenticated:
        return HttpResponse(status=403)
    
    if request.method == "GET":

        purchases = Purchases.objects.filter(user=request.user)
        #warranty calculation
        current_time = timezone.now()
        data = []
        for purchase in purchases:
            purchase_date = purchase.purchaseDate
            rem_time = current_time-purchase_date
            rem_days = rem_time.days
            warranty_left = purchase.bikeInfo.warranty-rem_days
            if warranty_left < 0:
                warranty_left = 0
            data.append({"purchase_date":str(purchase.purchaseDate), "model_number": purchase.bikeInfo.modelNumber,
            "color":purchase.bikeInfo.color, "price":purchase.bikeInfo.price, "bike_type":purchase.bikeInfo.type.name, "warranty_left":warranty_left})
       
        ctx = {
            "data":data
        }


        return HttpResponse(json.dumps(ctx), content_type="application/json")