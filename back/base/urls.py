from django.urls import path
from .views import adminstratorsviews, airlinecompaniesviews, userrolesviews,customersviews, countriesviews,flightsviews,ticketsviews,userviews
from .views.userviews import MyTokenObtainPairView
from .views.customersviews import MyTokenObtainPairView
from .views.adminstratorsviews import MyTokenObtainPairView
from .views.flightsviews import MyTokenObtainPairView
from .views.countriesviews import MyTokenObtainPairView
from .views.airlinecompaniesviews import MyTokenObtainPairView
from .views.ticketsviews import MyTokenObtainPairView
from .views.userrolesviews import MyTokenObtainPairView


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
 
urlpatterns = [
    # eyal urls: 
    # path("userprod",views.getProductsForUSER,name='userprod'),
    # path('add', views.addProductsForUSER,name='add'),
    # path('addProfile', views.addProfile,name='Profile'),
    # Authentication
    # Register /signup
    # path('addUser/', views.addUser),
    
    # customers urls:
    path('customers', customersviews.getCustomers),
    path('customers/<id>', customersviews.getCustomers),
    path('addcustomer', customersviews.addCustomers),
    # adminstrators urls:
    path('adminstrators', adminstratorsviews.getAdmin),
    path('adminstrators/<id>', adminstratorsviews.getAdmin),
    path('addadminstrators', adminstratorsviews.addAdmin),
    # airline_Compamies urls:
    path('airline_Companie', airlinecompaniesviews.getCompanies),
    path('airline_Companie/<id>', airlinecompaniesviews.getCompanies),
    path('addairline_Companies', airlinecompaniesviews.addairline_Companies),
    # countries urls:
    path('countrie', countriesviews.getCountries),
    path('countrie/<id>', countriesviews.getCountries),
    path('deletecountrie/<id>', countriesviews.deleteCountries),
    path('addcountrie', countriesviews.addCountries),
    # flights urls:
    path('flight', flightsviews.getFlights),
    path('flight/<id>', flightsviews.getFlights),
    path('addflight', flightsviews.addFlights),
    path('airlineflights', flightsviews.getFlightForAirline),
    path('deleteflight/<id>', flightsviews.deleteFlight),
     path('selectflight/<Origin_Countrie>/<Destination_Countrie>/<Departure_Time>/<Landing_Time>', flightsviews.get_filght_by_filters),
    # tickets urls:
    path('tickets', ticketsviews.getTickets),
    path('usertickets', ticketsviews.getTicketsForUSER),
    path('tickets/<id>', ticketsviews.getTickets),
    path('addtickets', ticketsviews.addTickets), 
    path('deletetickets/<id>', ticketsviews.deleteTickets),
    # user urls:
    path('users', userviews.getUser),
    path('users/<id>', userviews.getUser),
     #register/signup
    path('adduser', userviews.adduser),
    #logout
    path('logout/',userviews.logout_view),
    # user role urls:
    path('users_Roles', userrolesviews.getUserroles),
    path('users_Roles/<id>', userrolesviews.getUserroles),
    path('addusers_Roles/', userrolesviews.addUserroles),
    # login
    path('token/', userviews.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    
]
