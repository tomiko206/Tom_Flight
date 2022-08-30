
from django.http import JsonResponse
from base.models import User
from base.views.userserializers import UserSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import logout

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
def getUser(request,id=-1):
    if request.method == 'DELETE': #method delete a row
        temp= User.objects.get(_id = id)
        temp.delete()
        return JsonResponse({'DELETE': id})
    print("innnn")
    user = request.user
    print(user)
    if int(id) > -1: #get single product
        return JsonResponse(UserSerializer().getUser(id),safe=False)
    else: # return all
        return JsonResponse(UserSerializer().getAllUser(),safe=False) #return array as json response
    
@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def adduser(request):
    print(request.data)
    User.objects.create_user(
        username=request.data['username'],
        email=request.data['email'],
        password=request.data['password'])
    
    #return JsonResponse({'POST':"success"})
    return JsonResponse({"user created":request.data['username']} )    

# logout
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    print(request.user, "logged out")
    logout(request) 
    return JsonResponse("user Logout",safe=False)
# Register
# @api_view(['POST'])
# def addUser(request):
#     user = User.objects.create_user(username=request.data['username'],
#                                  email=request.data['email'],
#                                  password=request.data['pwd'])
#     UserProfile.objects.create(user=user,user_role_id=1)
#     return JsonResponse({"user created":request.data['username']} )

# @api_view(['POST'])   
# @permission_classes([IsAuthenticated])
# def addUser(request):
#     print(request.data)
#     user = request.user
#     user.objects.create(
#         Username=request.data["Username"],
#         Password=request.data["Password"],
#         Email=request.data["Email"],
#         User_Role=request.data["User_Role"],
#         user=user)
#     print(user)
#     user = user.user_set.all()
#     print(user)
#     serializer = Users(user, many=True)
#     return Response(serializer.data)

 