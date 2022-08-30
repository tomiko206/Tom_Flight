from django.contrib import admin

from .models import Adminstrator, Airline_Companie, Countrie, Customer, Flight, Ticket, Users_Role , Profile

# Register your models here.

admin.site.register(Customer)
admin.site.register(Adminstrator)
admin.site.register(Countrie)
admin.site.register(Airline_Companie)
admin.site.register(Flight)
admin.site.register(Ticket)
admin.site.register(Users_Role)
admin.site.register(Profile)


