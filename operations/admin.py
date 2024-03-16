from django.contrib import admin
from operations.models import CompanyEmployee, CompanyAsset, CompanyEmployeeAsset

# Register your models here.
admin.site.register(CompanyEmployee)
admin.site.register(CompanyAsset)
admin.site.register(CompanyEmployeeAsset)