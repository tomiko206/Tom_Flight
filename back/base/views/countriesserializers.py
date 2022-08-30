
from rest_framework.serializers import ModelSerializer
from base.models import Countrie
 
 
class CountriesSerializer(ModelSerializer):
    class Meta:
        model = Countrie
        fields = '__all__'


    def getCountries(self,obj):
        return {
            "id": obj._id,
            "Name": str(obj.Name),
            
            }
        
    def getCountriesId(self,id,):
        countries= Countrie.objects.get(_id = id)
        return {
            "id": countries._id,
            "Name": str(countries.Name),
            
 
          
            
            }

    def getAllCountries(self):
        res=[] #create an empty list
        for countriestObj in Countrie.objects.all(): #run on every row in the table...
            res.append(self.getCountries(countriestObj)) #append row by to row to res list
        return res
        