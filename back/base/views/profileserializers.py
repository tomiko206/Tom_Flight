
from base.views.users_rolesserializers import Users_RolesSerializer
from base.views.userserializers import UserSerializer
from rest_framework.serializers import ModelSerializer
from base.models import Profile
 
 
class TicketsSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

def get_UserProfile(self,obj):
        return {
            "id": obj._id,
            "user": UserSerializer().getUser(obj.user),
            "User_Role": Users_RolesSerializer().getUsers_Roles(obj.user_role)
            }
        
def getProfileId(self,id,):
        profile= Profile.objects.get(_id = id)
        return {   
            "id": profile._id,
            "User": UserSerializer().getUser(profile.User),
            "User_Role": Users_RolesSerializer().getUsers_RolesId(profile.user_role)
            }

def getAllProfile(self):
        res=[] #create an empty list
        for profiletObj in Profile.objects.all(): #run on every row in the table...
            res.append(self.get_UserProfile(profiletObj)) #append row by to row to res list
        return res
    