# Title / Repository Name
Flight Project - Tom

## About / Usage
this application is supposed to manage Flight system. 

* What is it, what does it do / Abstract
Build a client application to use the DAL (from project file instruction). i will be using Django as logic and React as gui and  sqlite3 as SQL database.

* this is what i will use
i will use dal to handle the database part.
i will use Django to build a development server to upload the program to the web and allows fast debugging at real time. also, use Class to divide the program.
i will use React in order to let the user view the program online.
i will be working in a virtual enviorment.

* Project status: working/prototype
just starting at 27/6. this is a prototype, wishing i will continue and build this app to further versions. perhaps i will need to remake.

## Installation/Requirements
* python version 3
* sqlite3 
* env -pip install virtualenv -> python -m virtualenv myenv -> source myenv/bin/activate
* django - pip install django -> packege: django-admin startproject backend . -> packege:django-admin startapp base
* restframework - pip install djangorestframework , pip install djangorestframework-simplejwt , pip install django-cors-headers
* Requirements file - Pip install -r requirements.txt

### Features
in general i will be implementing CRUD.
Add the following operations (display a simple menu)
•	Add..
•	Update..
•	Remove ..
•	Get..
•	Create..
•	login/sign up..

### Content (Description, sub-modules organization...)
1.	Create a sqlite3 database with 8 tables:
(Filghts )
    Id (PK)
	Airline_Company (FK)
	Origin_Country (FK)
	Destination_Country (FK)
	Departure_Time 
    Landing_Time
    Remaining_Tickets
(Customers)
    Id (PK)
    Name (U)
(Tickets)
    Id (PK)
    Flight_Id (FK)
    Customer_Id (FK)
(Airline_Companies)    
    Id (PK)
    Name (U)
    Country_Id (FK)
    User_Id (FK)
(Customers)
    Id (PK)
    First_Name
    Last_Name
    Address
    Phone_No (U)
    Credit_Card_No (U)
    User (FK)
(Users)
    Id (PK)
    Username (U)
    Password 
    Email (U)
    User_Role (FK)
(User_Role)
    Id (FK)
    Role_Name (U)
(Adminstrators)
    Id (PK)
    First_Name
    Last_Name
    User_Id (FK)

## Resources (Documentation and other links)
i have the support of colleagues using zoom to work together and the support of john bryce instructor. examples from programming forums.

## About the programmer
Tom Eliyahu is a junior programmer with python language.
Enrolled in python course at john bryce technical college.
is an open source.