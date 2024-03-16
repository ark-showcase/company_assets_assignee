from django.urls import path, include
from .views import AssignCompanyAsset

urlpatterns = [
    path('', AssignCompanyAsset.as_view(), name='assign_asset'),
]