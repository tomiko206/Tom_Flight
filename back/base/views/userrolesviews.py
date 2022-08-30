from base.models import Users_Role
from base.views.users_rolesserializers import Users_RolesSerializer
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        token['username'] = user.username
        # ...
 
        return token
 
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticated])
def getUserroles(request,id=-1):
    if request.method == 'DELETE': #method delete a row
        temp= Users_Role.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    print("innnn")
    user = request.user
    print(user)
    if int(id) > -1: #get single product
        return JsonResponse(Users_RolesSerializer().getUsers_RolesId(id),safe=False)
    else: # return all
        return JsonResponse(Users_RolesSerializer().getAllUsers_Roles(),safe=False) #return array as json response

 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addUserroles(request):
    print(request.data)
    user = request.user
    Users_Role.objects.create(
        Role_Name=request.data["Role_Name"],
        )
   
    # return JsonResponse({'POST':"success"})
    return JsonResponse(Users_RolesSerializer().getAllUsers_Roles(),safe=False)
