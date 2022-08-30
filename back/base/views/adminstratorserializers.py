from base.models import Adminstrator
from base.views.userserializers import UserSerializer
from rest_framework.serializers import ModelSerializer
from base.models import Adminstrator
 
 
class AdminstratorsSerializer(ModelSerializer):
    class Meta:
        model = Adminstrator
        fields = '__all__'


    def getAdminstrators(self,obj):
        return {
            "id": obj._id,
            "First_Name": str(obj.First_Name),
            "Last_Name": str(obj.Last_Name),
            "user": UserSerializer().getUser(obj.user)
            
            }

    
    def getAdminstratorsId(self,id,):
        adminstrators= Adminstrator.objects.get(_id = id)
        return {
            "id": adminstrators._id,
            "First_Name": str(adminstrators.First_Name),
            "Last_Name": str(adminstrators.Last_Name),
            "user": UserSerializer().getUser(adminstrators.user)
            
            
            }

    def getAllAdminstrators(self):
        res=[] #create an empty list
        for adminstratorsstObj in Adminstrator.objects.all(): #run on every row in the table...
            res.append(self.getAdminstrators(adminstratorsstObj)) #append row by to row to res list
        return res
        