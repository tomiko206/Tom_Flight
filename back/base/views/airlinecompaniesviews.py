from base.models import Airline_Companie, Countrie
from base.views.airlinecompaniesserializers import Airline_CompaniesSerializer
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
def getCompanies(request,id=-1):
    if request.method == 'DELETE': #method delete a row
        temp= Airline_Companie.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    print("innnn")
    user = request.user
    print(user)
    if int(id) > -1: #get single product
        return JsonResponse(Airline_CompaniesSerializer().getAirline_CompaniesId(id),safe=False)
    else: # return all
        return JsonResponse(Airline_CompaniesSerializer().getAllAirline_Companies(),safe=False) #return array as json response

 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addairline_Companies(request):
    print(request.data)
    user = request.user
    Airline_Companie.objects.create(
        Name=request.data["Name"],
        Countrie=Countrie.objects.get(_id=request.data['Countrie_id']),
        user=user)

    return JsonResponse(Airline_CompaniesSerializer().getAllAirline_Companies(),safe=False)
    # return JsonResponse({'POST':"success"})

