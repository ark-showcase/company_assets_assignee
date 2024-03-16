from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from operations.serializers import CompanyEmployeeSerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class AssignCompanyEmployee(APIView):
    @method_decorator(login_required(login_url='/user/module/login/'))
    def get(self, request):
        context = {
            'message': 'assign an employee via POST request'
        }
        return Response(context, status=status.HTTP_200_OK)


    @method_decorator(login_required(login_url='/user/module/login/'))
    def post(self, request):
        serializer = CompanyEmployeeSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'employee assigned successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)