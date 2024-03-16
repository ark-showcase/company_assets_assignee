from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from operations.models import CompanyAsset, CompanyEmployeeAsset
from authentication.models import CompanyUser
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ViewAssets(APIView):
    @method_decorator(login_required(login_url='/user/module/login/'))
    def get(self, request):
        username = request.session.get('username')
        company_unique_identifier = CompanyUser.objects.filter(username=username).values('company_unique_identifier').first()['company_unique_identifier']

        all_assets =CompanyAsset.objects.filter(company_unique_identifier=company_unique_identifier).values('asset_name', 'asset_status')
        if not all_assets.exists:
            all_assets = None
        assigned_assets = CompanyEmployeeAsset.objects.filter(company_unique_identifier=company_unique_identifier).values('company_asset_id', 'company_employee_id', 'status')
        if not assigned_assets.exists:
            assigned_assets = None

        print('==================')
        print(all_assets)
        print(assigned_assets)
        print('==================')

        context = {
            'all_assets': all_assets,
            'assigned_assets': assigned_assets,
        }
        return Response(context, status=status.HTTP_200_OK)