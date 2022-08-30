from base.views.customerserializers import CustomersSerializer
from base.views.flightserializers import FlightsSerializer

from base.views.userserializers import UserSerializer
from rest_framework.serializers import ModelSerializer
from base.models import Ticket
 
 
class TicketsSerializer(ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


    def getTickets(self,obj):
        return {
            "id": obj._id,
            "Flight": FlightsSerializer().getFlights(obj.Flight),
            "number_of_tickets" : obj.number_of_tickets,
            # "user": UserSerializer().getUser(obj.user)
            # "Customer": CustomersSerializer().getCustomers(obj.Customer),
    
            }

    def getTicketsId(self,id,):
        tickets= Ticket.objects.get(_id = id)
        return {
            "id": tickets._id,
            "Flight": FlightsSerializer().getFlights(tickets.Flight),
            "Customer": CustomersSerializer().getCustomers(tickets.Customer),
    
            }
        
    def get_Tickets_By_User(self,obj):
            #tickets = user.tickets_set.all()
        return {
            "id": obj._id,
            "Flight":  FlightsSerializer().getFlights(obj.Flight),
            "number_of_tickets" : obj.number_of_tickets,
            "user": UserSerializer().getUser(obj.user)
            }

    def getAllTickets(self):
        res=[] #create an empty list
        for ticketstObj in Ticket.objects.all(): #run on every row in the table...
            res.append(self.getTickets(ticketstObj)) #append row by to row to res list
        return res
        
    def get_All_Tickets_For_User(self,tickets):
        res=[] #create an empty list
        for ticketsObj in tickets: #run on every row in the table...
            res.append(self.get_Tickets_By_User(ticketsObj)) #append row by to row to res list
        return res    