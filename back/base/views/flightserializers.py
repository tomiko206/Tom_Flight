from base.views.countriesserializers import CountriesSerializer
from base.views.airlinecompaniesserializers import Airline_CompaniesSerializer
from base.views.userserializers import UserSerializer
from rest_framework.serializers import ModelSerializer
from base.models import Flight
 
 
class FlightsSerializer(ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


    def getFlights(self,obj):
        return {
            "id": obj._id,
            "Airline_Companie": Airline_CompaniesSerializer().getAirline_Companies(obj.Airline_Companie),
            "Origin_Countrie": CountriesSerializer().getCountries(obj.Origin_Countrie),
            "Destination_Countrie": CountriesSerializer().getCountries(obj.Destination_Countrie),
            "Departure_Time": obj.Departure_Time,
            "Landing_Time": obj.Landing_Time,
            "Remaining_Tickets": obj.Landing_Time,
            "Price": obj.Price, 
            
            }
        
    def getAllCFlights(self):
        res=[] #create an empty list
        for flightstObj in Flight.objects.all(): #run on every row in the table...
            res.append(self.getFlights(flightstObj)) #append row by to row to res list
        return res

    def getFlightsId(self,id,):
        flights= Flight.objects.get(_id = id)
        return {
            "id": flights._id,
            "Airline_Companie": Airline_CompaniesSerializer().getAirline_Companies(flights),
            "Origin_Countrie": CountriesSerializer().getCountries(flights),
            "Destination_Countrie": CountriesSerializer().getCountries(flights),
            "Departure_Time": flights.Departure_Time,
            "Landing_Time": flights.Landing_Time,
            "Remaining_Tickets": flights.Landing_Time,
            "Price": flights.Price, 
            
            }
        
        
    def get_Flights_For_Airline(self,obj):
        return {
            "id": obj._id,
            "Airline_Companie":  Airline_CompaniesSerializer().getAirline_Companies(obj.Airline_Companie),
            "Origin_Countrie":  CountriesSerializer().getCountries(obj.Origin_Countrie),
            "Destination_Countrie": CountriesSerializer().getCountries(obj.Destination_Countrie),
            "Departure_Time": obj.Departure_Time,
            "Landing_Time": obj.Landing_Time,
            "Remaining_Tickets": obj.Remaining_Tickets,
            # "status": obj.status, 
            "Price": obj.Price, 
        }
    
        
    def get_All_Flights_For_Airline(self,flights):
        res=[] #create an empty list
        for flightObj in flights: #run on every row in the table...
            res.append(self.get_All_Flights_For_Airline(flightObj)) #append row by to row to res list
        return res