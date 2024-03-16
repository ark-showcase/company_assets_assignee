from django.urls import path, include
from .views import AssignCompanyEmployee

urlpatterns = [
    path('', AssignCompanyEmployee.as_view(), name='assign_employee'),
]