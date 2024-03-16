from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.contrib.auth import authenticate, login
class Login(APIView):
    def get(self, request):
        context = {
            'message': 'enter username and password'
        }
        return Response(context, status=status.HTTP_200_OK)
    def post(self, request):
        username = request.session.get('username')
        if username:
            return Response({'message': 'A user already logged in'})
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['username'] = username
            return Response({'message': 'Login successful'})
        else:
            return Response({'message': 'Invalid credentials'}, status=400)