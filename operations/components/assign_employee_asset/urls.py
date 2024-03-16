from django.urls import path, include
from .views import AssignCompanyEmployeeAsset, ReturnCompanyEmployeeAsset

urlpatterns = [
    path('', AssignCompanyEmployeeAsset.as_view(), name='assign_employee_asset'),
    path('return/<str:company_asset_id>/', ReturnCompanyEmployeeAsset.as_view(), name='return_employee_asset'),
]