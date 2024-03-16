from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from authentication.models import CompanyUser
from authentication.serializers import CompanyUserSerializer

class Signup(APIView):
    def get(self, request):
        context = {
            'message': 'create a user via POST request'
        }
        return Response(context, status=status.HTTP_200_OK)
    def post(self, request):
        username = request.session.get('username')
        if username:
            return Response({'message': 'Logout first'})
        serializer = CompanyUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = CompanyUser.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)