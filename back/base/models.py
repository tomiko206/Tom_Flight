from unicodedata import decimal
from django.db import models
from django.contrib.auth.models import User

class Users_Role(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    Role_Name = models.CharField(max_length=50,null=True,blank=True)
    
    def __str__(self):
        return self.Role_Name
    
class Profile(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    user =models.OneToOneField( User,on_delete=models.CASCADE)
    User_Role = models.ForeignKey(Users_Role, on_delete=models.CASCADE, null=True) 
    
    def __str__(self):
 	   return str(self.user)

class Customer(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    First_Name = models.CharField(max_length=50,null=True,blank=True)
    Last_Name = models.CharField(max_length=50,null=True,blank=True)
    Address = models.CharField(max_length=50,null=True,blank=True)
    Phone_No = models.CharField(max_length=50,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
     	return self.First_Name + self.Last_Name
    
class Adminstrator(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    First_Name = models.CharField(max_length=50,null=True,blank=True)
    Last_Name = models.CharField(max_length=50,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
     	return self.First_Name + self.Last_Name
    
class Countrie(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    Name = models.CharField(max_length=50,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    
    
    def __str__(self):
     	return self.Name 

class Airline_Companie(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    Name = models.CharField(max_length=50,null=True,blank=True)
    Countrie = models.ForeignKey(Countrie, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
     
    def __str__(self):
     	return self.Name 
  
 
class Flight(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    status =models.BooleanField(default=True)
    Airline_Companie = models.ForeignKey(Airline_Companie, on_delete=models.CASCADE, null=True)
    Origin_Countrie = models.ForeignKey(Countrie,related_name='Origin_Countrie', on_delete=models.CASCADE, null=True)
    Destination_Countrie = models.ForeignKey(Countrie,related_name='Destination_Countrie', on_delete=models.CASCADE, null=True)
    Departure_Time = models.DateTimeField(auto_now = False, auto_now_add= False)
    Landing_Time = models.DateTimeField(auto_now = False, auto_now_add= False)
    Remaining_Tickets =  models.CharField(max_length=50,null=True,blank=True)
    Price = models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
     	return str(self.Origin_Countrie) + str(self.Destination_Countrie) +str(self.Airline_Companie)
    
class Ticket(models.Model): 
    _id=models.AutoField(primary_key=True,editable=False)
    Flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=True)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    number_of_tickets = models.IntegerField(null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    
    def __str__(self):
     	return str(self.Flight) + str(self.Customer)
    
# class Users(models.Model):
#     _id=models.AutoField(primary_key=True,editable=False)
#     Username = models.TextField()
#     Password =  models.CharField(max_length=50,null=True,blank=True)
#     Email =  models.CharField(max_length=50,null=True,blank=True)
#     User_Role = models.ForeignKey(Users_Roles, on_delete=models.CASCADE, null=True)  
    
    # def __str__(self):
    #     return self.Username
 

    