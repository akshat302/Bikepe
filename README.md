# Bikepe
<h3>Entities :-</h3>

1.) User <br>
2.) Colors <br>
3.) BikeCategory <br>
4.) BikeCategoryColors <br>
5.) Bike <br>
6.) Purchases<br>

<h3>Database Models :-</h3>

Colors:

    name : name of the color

BikeCategory

    name : name of the bike category
    stockCount : number of bikes available for the particular category (default=0)

BikeCategoryColors

    bikeCategory : category of the individual bike
    color : name of the color
    isAvailable : tells whether the color is available for that bikeCategory or not (default=False)

Bike

    type : category of the individual bike
    modelNumber : model number of the bike (Unique for every bike)
    color : color of the bike available
    warranty : warranty of the bike in days
    price : price of the bike in rupees

Purchases

    user : user of the purchased bike
    purchaseDate : date of purchase of the bike
    bikeInfo : details of the bike


<h3>API Details :- </h3>

Register -

    URL - "http://127.0.0.1:8000/signup/"
    Type - POST
    Request Body - {"username":"akshat123", "password":"test123", "email":"akshat@test.com", "first_name":"Akshat",
                    "last_name":"Gupta"}
    Description - Used for registering a new user 
    Response - {"status": 201}

Login - 
    
    URL - "http://127.0.0.1:8000/login/"
    Type - POST
    Request Body - {"username":"akshat123", "password":"test123"}
    Description - Used for logging into the website as an authenticated user


Logout - 

    URL - "http://127.0.0.1:8000/logout/"
    Type - GET
    Description - Used for logging out an existing user


List_Bikes - 

    URL - "http://127.0.0.1:8000/bikes/"
    Type - GET
    Description - Used to list all the bikes and their Details
    Response - {'bikes': [{'modelNumber': '1MS19EE006',
                            'color': 'Black',
                            'warranty': '450',
                            'price': 292799.0,
                            'bike_category': 'Road Bikes',
                            'stock_count': 400,
                            'available_colors': ['Black', 'Blue']},
                            {'modelNumber': '1MS19EI006',
                            'color': 'Blue',
                            'warranty': '456',
                            'price': 180000.0,
                            'bike_category': 'Road Bikes',
                            'stock_count': 400,
                            'available_colors': ['Black', 'Blue']}]}


Purchase_Bike - 
    
    URL - "http://127.0.0.1:8000/buy/"
    Type - POST
    Request Body - {"model_number":"1MS19EE006"}
    Description - Used to purchase a Bike
    Response - 201/404


Update_Bike -

    URL - "http://127.0.0.1:8000/update_bike/"
    Type - POST
    Request Body - {"model_number":"1MS19EE006", "category_name":"Road Bikes", "bike_color":"Black"}
    Description - Allow the admin and staff members to update the Bike Details
    Response - 201/404


Purchases -

    URL - "http://127.0.0.1:8000/purchases/"
    Type - GET
    Description - Used to see the purchased bikes by an user
    Response - {'data': [{  'purchase_date': '2022-11-06 17:38:41.734324+00:00',
                            'model_number': '1MS19EI006',
                            'color': 'Blue',
                            'price': 180000.0,
                            'bike_type': 'Road Bikes',
                            'warranty_left': 456}]}

<h3> Instructions to run </h3>
1.) cd into the bikepe folder - cd bikepe. <br>
2.) run python manage.py migrate in the terminal.<br>
3.) run python manage.py runserver in the terminal to run the server.<br>
