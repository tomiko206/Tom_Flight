from base.models import Adminstrator
from base.views.adminstratorserializers import AdminstratorsSerializer
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
        token['is_superuser'] = user.is_superuser
        token['is_staff'] = user.is_staff
        
        # ...
 
        return token
 
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET','DELETE'])
@permission_classes([IsAuthenticated])
def getAdmin(request,id=-1):
    if request.method == 'DELETE': #method delete a row
        temp= Adminstrator.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    print("innnn")
    user = request.user
    print(user)
    if int(id) > -1: #get single product
        return JsonResponse(AdminstratorsSerializer().getAdminstratorsId(id),safe=False)
    else: # return all
        return JsonResponse(AdminstratorsSerializer().getAllAdminstrators(),safe=False) #return array as json response

 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addAdmin(request):
    print(request.data)
    user = request.user
    Adminstrator.objects.create(
        First_Name=request.data["First_Name"],
        Last_Name=request.data["Last_Name"],
        user=user)
 
    return JsonResponse(AdminstratorsSerializer().getAllAdminstrators(),safe=False)
    # return JsonResponse({'POST':"success"})
