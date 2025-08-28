from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from post.models import  User
from post.serializers import UserSerializer

class UserView(APIView):
     def get(self, request):
        user = User.objects.all()
        serializer_user = UserSerializer(user, many=True) 
        return Response(serializer_user.data, status=status.HTTP_200_OK)

     def post(self, request):
        serializer_user = UserSerializer(data=request.data)
        if serializer_user.is_valid():
           serializer_user.save() 
           return Response(serializer_user.data, status=status.HTTP_201_CREATED) 
        return Response(serializer_user.errors, status=status.HTTP_400_BAD_REQUEST)