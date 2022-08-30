from base.views.countriesserializers import CountriesSerializer
from base.views.userserializers import UserSerializer
from rest_framework.serializers import ModelSerializer
from base.models import Airline_Companie
 
 
class Airline_CompaniesSerializer(ModelSerializer):
    class Meta:
        model = Airline_Companie
        fields = '__all__'



    def getAirline_Companies(self,obj):
        return {
            "id": obj._id,
            "Name": str(obj.Name),
            "Countrie": CountriesSerializer().getCountries(obj.Countrie),
            "user": UserSerializer().getUser(obj.user)
            
            }

    
 
    def getAirline_CompaniesId(self,id,):
        airline_Companies= airline_Companies.objects.get(_id = id)
        return {
            "id": airline_Companies._id,
            "Name": str(airline_Companies.Name),
            "Countrie": CountriesSerializer().getCountries(airline_Companies.Countrie),
            "user": UserSerializer().getUser(airline_Companies.user)
            
            
            }


    def getAllAirline_Companies(self):
        res=[] #create an empty list
        for airline_CompaniestObj in Airline_Companie.objects.all(): #run on every row in the table...
            res.append(self.getAirline_Companies(airline_CompaniestObj)) #append row by to row to res list
        return res
        