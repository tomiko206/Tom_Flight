import datetime
from base.models import Countrie, Flight,Airline_Companie
from base.views.countriesserializers import CountriesSerializer
from base.views.flightserializers import FlightsSerializer
from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from datetime import datetime


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        token['username'] = user.username
        token['is_superuser'] = user.is_superuser
        token['is_staff'] = user.is_staff
        
        return token
 
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET','DELETE'])
# @permission_classes([IsAuthenticated])
def getFlights(request,id=-1):
    if request.method == 'DELETE': #method delete a row
        temp= Flight.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    print("innnn")
    user = request.user
    print(user)
    if int(id) > -1: #get single product
        return JsonResponse(FlightsSerializer().getFlightsId(id),safe=False)
    else: # return all
        return JsonResponse(FlightsSerializer().getAllCFlights(),safe=False) #return array as json response

 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addFlights(request):
    print(request.data)
    Flight.objects.create(
        Airline_Companie=Airline_Companie.objects.get(_id=request.data['Airline_Companie_id']),
        Origin_Countrie=Countrie.objects.get(_id=request.data['Origin_Countrie_id']),
        Destination_Countrie=Countrie.objects.get(_id=request.data['Destination_Countrie_id']),
        Departure_Time=request.data["Departure_Time"],
        Landing_Time=request.data["Landing_Time"],
        Remaining_Tickets=request.data["Remaining_Tickets"],
        Price=request.data["Price"])
    
    #return JsonResponse({'POST':"success"})
    return JsonResponse(FlightsSerializer().getAllCFlights(),safe=False) 
@api_view(['GET'])
def get_filght_by_filters(request,Origin_Countrie=-1,Destination_Countrie=-1,Departure_Time="",Landing_Time=""):
    Departure_Time_obj = datetime.strptime(Departure_Time, '%Y-%m-%d')
    Landing_Time_obj = datetime.strptime(Landing_Time, '%Y-%m-%d')
    res=[]
    print(Origin_Countrie, Destination_Countrie)
    selectedFlight = Flight.objects.all()
    if int(Origin_Countrie) > -1 :
        Origin_Countrie_id = CountriesSerializer().getCountriesId(Origin_Countrie)["id"]
        selectedFlight = selectedFlight .filter(Origin_Countrie_id=Origin_Countrie_id)
    if int(Destination_Countrie) > -1 :
        Destination_Countrie_id = CountriesSerializer().getCountriesId(Destination_Countrie)["id"]
        selectedFlight = selectedFlight .filter(Destination_Countrie_id=Destination_Countrie_id)
    if Departure_Time_obj != "" and Landing_Time_obj != "":
        selectedFlight = selectedFlight.filter(Departure_Time__range=[Departure_Time_obj,Landing_Time_obj])
    selectedFlight = selectedFlight.filter(status = True)
    for flight in selectedFlight:
        res.append(FlightsSerializer().getFlights(flight))
    return JsonResponse(res,safe =False)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteFlight(request,id=-1):
    user = request.user
    print(user,"innnn")
    temp= Flight.objects.get(_id = id)
    temp.delete()
    return JsonResponse({'DELETE': id})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getFlightForAirline(request):
    user = request.user
    flights = user.flight_set.all()
    return JsonResponse(FlightsSerializer().get_All_Flights_For_Airline(flights),safe=False) #return array as json response
