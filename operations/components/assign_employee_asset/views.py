from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import datetime

from operations.serializers import CompanyEmployeeAssetSerializer
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from authentication.models import CompanyUser
from operations.models import CompanyEmployeeAsset

class AssignCompanyEmployeeAsset(APIView):
    @method_decorator(login_required(login_url='/user/module/login/'))
    def get(self, request):
        context = {
            'message': 'assign an asset to an employee via POST request'
        }
        return Response(context, status=status.HTTP_200_OK)


    @method_decorator(login_required(login_url='/user/module/login/'))
    def post(self, request):
        serializer = CompanyEmployeeAssetSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'asset assigned to an employee successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReturnCompanyEmployeeAsset(APIView):
    @method_decorator(login_required(login_url='/user/module/login/'))
    def get(self, request, company_asset_id):
        username = request.session.get('username')
        company_unique_identifier = CompanyUser.objects.filter(username=username).values('company_unique_identifier').first()['company_unique_identifier']
        last_assigned_record = CompanyEmployeeAsset.objects.filter(company_unique_identifier=company_unique_identifier, company_asset_id=company_asset_id).\
            order_by('-id').first()

        if last_assigned_record:
            last_assigned_record.returned_date = datetime.date.today()
            last_assigned_record.status = 'returned'
            last_assigned_record.save()

            context = {
                'message': 'assigned asset returned successfully'
            }
            return Response(context, status=status.HTTP_200_OK)
        context = {
            'message': 'can not return asset'
        }
        return Response(context, status=status.HTTP_400_BAD_REQUEST)