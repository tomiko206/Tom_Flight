
from rest_framework.serializers import ModelSerializer
from base.models import Users_Role
 
 
class Users_RolesSerializer(ModelSerializer):
    class Meta:
        model = Users_Role
        fields = '__all__'


    def getUsers_Roles(self,obj):
        return {
            "id": obj._id,
            "Role_Name": str(obj.Role_Name),
            
            }
    
    def getUsers_RolesId(self,id,):
        users_Roles= Users_Role.objects.get(_id = id)
        return {  "id": users_Roles._id,
            "Role_Name": str(users_Roles.Role_Name),
            
            }
        
    def getAllUsers_Roles(self):
        res=[] #create an empty list
        for customerstObj in Users_Role.objects.all(): #run on every row in the table...
            res.append(self.getUsers_Roles(customerstObj)) #append row by to row to res list
        return res
        