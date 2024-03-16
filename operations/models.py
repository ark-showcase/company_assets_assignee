from django.db import models
from django.utils import timezone

# Create your models here.
class CompanyEmployee(models.Model):
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_unique_identifier = models.CharField(max_length=100, blank=True, null=True)
    company_employee_id = models.CharField(max_length=100, blank=True, null=True, unique=True)
    employee_name = models.CharField(max_length=100, blank=True, null=True)
    employee_department = models.CharField(max_length=100, blank=True, null=True)
    employee_cell_no = models.CharField(max_length=100, blank=True, null=True)
    employee_email = models.EmailField(max_length=100, blank=True, null=True)



class CompanyAsset(models.Model):
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_unique_identifier = models.CharField(max_length=100, blank=True, null=True)
    company_asset_id = models.CharField(max_length=100, blank=True, null=True, unique=True)
    asset_category = models.CharField(max_length=100, blank=True, null=True)
    asset_name = models.CharField(max_length=100, blank=True, null=True)
    asset_brand = models.CharField(max_length=100, blank=True, null=True)
    asset_model = models.CharField(max_length=100, blank=True, null=True)
    asset_condition = models.CharField(max_length=100, blank=True, null=True, default='new')
    asset_status = models.CharField(max_length=100, blank=True, null=True, default='free')



class CompanyEmployeeAsset(models.Model):
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_unique_identifier = models.CharField(max_length=100, blank=True, null=True)
    company_employee_id = models.CharField(max_length=100, blank=True, null=True)
    company_asset_id = models.CharField(max_length=100, blank=True, null=True)
    assigned_date = models.DateField(blank=True, null=True, default=timezone.now())
    returned_date = models.DateField(blank=True, null=True)
    assigned_asset_condition = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True, default='assigned')