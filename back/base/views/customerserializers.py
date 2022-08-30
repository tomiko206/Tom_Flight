from base.views.userserializers import UserSerializer
from rest_framework.serializers import ModelSerializer
from base.models import Customer
 
 
class CustomersSerializer(ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


    def getCustomers(self,obj):
        return {
            "id": obj._id,
            "First_Name": str(obj.First_Name),
            "Last_Name": str(obj.Last_Name),
            "Address": str(obj.Address),
            "Phone_No": obj.Phone_No,
            # "Credit_Card_No": obj.Credit_Card_No,
            "user": UserSerializer().getUserName(obj.user)
            
            }

    def getCustomersId(self,id):
        customers= Customer.objects.get(_id = id)
        return {
            "id": customers._id,
            "First_Name": str(customers.First_Name),
            "Last_Name": str(customers.Last_Name),
            "Address": str(customers.Address),
            "Phone_No": customers.Phone_No,
            # "Credit_Card_No": customers.Credit_Card_No,
            "user": UserSerializer().getUserName(customers.user)
            
            }
        
        
    def getAllCustomers(self):
        res=[] #create an empty list
        for customersObj in Customer.objects.all(): #run on every row in the table...
            res.append(self.getCustomers(customersObj)) #append row by to row to res list
        return res