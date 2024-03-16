from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class Logout(APIView):
    @method_decorator(login_required(login_url='/user/module/login/'))
    def get(self, request):
        username = request.session.get('username')
        if not username:
            return Response({'message': 'Login first'})
        logout(request)
        return Response({'message': 'Logout successful'})