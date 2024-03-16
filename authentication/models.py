from django.contrib.auth.models import AbstractUser
from django.db import models

class CompanyUser(AbstractUser):
    company_name = models.CharField(max_length=100, blank=True, null=True, unique=True)
    company_unique_identifier = models.CharField(max_length=100, blank=True, null=True, unique=True)
