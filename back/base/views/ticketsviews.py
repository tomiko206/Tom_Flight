from base.models import Ticket,Flight,Customer
from base.views.ticketsserializers import TicketsSerializer

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
# @permission_classes([IsAuthenticated])
def getTickets(request,id=-1):
    if request.method == 'DELETE': #method delete a row
        temp= Ticket.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    print("innnn")
    user = request.user
    print(user)
    if int(id) > -1: #get single product
        return JsonResponse(TicketsSerializer().getTicketsId(id),safe=False)
    else: # return all
        return JsonResponse(TicketsSerializer().getAllTickets(),safe=False) #return array as json response

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteTickets(request,id=-1):
    temp= Ticket.objects.get(_id = id)
    temp.delete()
    return JsonResponse({'DELETE': id})

 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addTickets(request):
    print(request.data)
    user = request.user
    Ticket.objects.create(
        Flight=Flight.objects.get(_id=request.data['flight_id']),
        number_of_tickets=request.data["number_of_tickets"],
        user=user)
    print(user)
    return JsonResponse({'POST':"success"})
 



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getTicketsForUSER(request):
    user = request.user
    print(user)
    tickets = user.ticket_set.all()
    return JsonResponse(TicketsSerializer().get_All_Tickets_For_User(tickets),safe=False) #return array as json response