from django.urls import path
from bikerrr.views import list_bikes, purchase_bike, update_bike_details, update_bikeCategory_details, register, login_api, logout_api, purchases

app_name = "bikerrr"

urlpatterns = [
    path('bikes/', list_bikes, name="bikes"),
    path('buy/', purchase_bike, name="buy"),
    path("update_bike/", update_bike_details, name="update_bike"),
    #path("update_bike_category/", update_bikeCategory_details, name="update_bike_category"),
    path("signup/", register, name="register"),
    path("login/", login_api, name="login"),
    path("logout/", logout_api, name="logout"),
    path("purchases/", purchases, name="purchases"),
]   
