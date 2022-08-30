

from django.http import JsonResponse
from base.views.users_rolesserializers import Users_RolesSerializer
from rest_framework.serializers import ModelSerializer
from base.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
    def getUserName(self,obj):
        return obj.username
    
 
    def getUser(self,obj):
        print(obj)
        if obj == None : return {}
        return {
            "username":obj.username,
            "email":   obj.email,
   
            }

    def getAllUser(self):
        res=[] #create an empty list
        for usertObj in User.objects.all(): #run on every row in the table...
            res.append(self.getUser(usertObj)) #append row by to row to res list
        return res