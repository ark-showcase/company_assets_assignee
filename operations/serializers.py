from rest_framework import serializers
from .models import CompanyEmployee, CompanyAsset, CompanyEmployeeAsset
from authentication.models import CompanyUser
import datetime

class CompanyEmployeeSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CompanyEmployee
        fields = [
            'company_name',
            'company_unique_identifier',
            'company_employee_id',
            'employee_name',
            'employee_department',
            'employee_cell_no',
            'employee_email',
        ]

    def validate_employee_name(self, value):
        """
        Validate that the company_name has a minimum length of 3 characters.
        """
        if not value:
            raise serializers.ValidationError("employee name must be provided.")
        if len(value) < 3:
            raise serializers.ValidationError("The employee name must be at least 3 characters long.")
        return value

    def create(self, validated_data):
        # Access the request object from the context
        request = self.context.get('request')

        current_user = request.session.get('username')

        current_user_object = CompanyUser.objects.filter(username=current_user).values('company_name', 'company_unique_identifier')

        validated_data['company_name'] = current_user_object[0]['company_name']
        validated_data['company_unique_identifier'] = current_user_object[0]['company_unique_identifier']

        # Create the CompanyEmployee object first
        company_employee = CompanyEmployee.objects.create(**validated_data)

        # Set the company_unique_identifier attribute to the ID
        company_employee.company_employee_id = validated_data['company_unique_identifier'] + '-' + str(company_employee.id)
        company_employee.save()

        return company_employee



class CompanyAssetSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CompanyAsset
        fields = [
            'company_name',
            'company_unique_identifier',
            'company_asset_id',
            'asset_category',
            'asset_name',
            'asset_brand',
            'asset_model',
            'asset_condition',
        ]

    def validate_asset_name(self, value):
        """
        Validate that the company_name has a minimum length of 3 characters.
        """
        if not value:
            raise serializers.ValidationError("asset name must be provided.")
        if len(value) < 3:
            raise serializers.ValidationError("The asset name must be at least 3 characters long.")
        return value

    def create(self, validated_data):
        # Access the request object from the context
        request = self.context.get('request')

        current_user = request.session.get('username')

        current_user_object = CompanyUser.objects.filter(username=current_user).values('company_name', 'company_unique_identifier')

        validated_data['company_name'] = current_user_object[0]['company_name']
        validated_data['company_unique_identifier'] = current_user_object[0]['company_unique_identifier']

        # Create the CompanyEmployee object first
        company_asset = CompanyAsset.objects.create(**validated_data)

        # Set the company_unique_identifier attribute to the ID
        company_asset.company_asset_id = validated_data['company_unique_identifier'] + '-' + str(company_asset.id)
        company_asset.save()

        return company_asset



class CompanyEmployeeAssetSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CompanyEmployeeAsset
        fields = [
            'company_name',
            'company_unique_identifier',
            'company_employee_id',
            'company_asset_id',
            'assigned_date',
            'returned_date',
            'assigned_asset_condition',
        ]

    def validate_assigned_date(self, value):
        """
        Validate that the assigned_date if the date not earlier than now.
        """
        if value < datetime.date.today():
            raise serializers.ValidationError("Invalid assign date.")
        return value

    def validate_company_employee_id(self, value):

        # Access the request object from the context
        request = self.context.get('request')

        current_user = request.session.get('username')

        current_user_object = CompanyUser.objects.filter(username=current_user).values('company_unique_identifier')

        this_company_unique_identifier = current_user_object[0]['company_unique_identifier']

        """
        Validate that the company_employee_id if the company_employee_id belongs to logged in company.
        """
        if not value:
            raise serializers.ValidationError("company_employee_id must be provided.")
        if not CompanyEmployee.objects.filter(company_employee_id=value, company_unique_identifier=this_company_unique_identifier).exists:
            raise serializers.ValidationError("This employee is not belongs to this company.")
        return value

    def validate_company_asset_id(self, value):

        # Access the request object from the context
        request = self.context.get('request')

        current_user = request.session.get('username')

        current_user_object = CompanyUser.objects.filter(username=current_user).values('company_unique_identifier')

        this_company_unique_identifier = current_user_object[0]['company_unique_identifier']

        """
        Validate that the company_asset_id if the company_employee_id belongs to logged in company.
        """
        if not value:
            raise serializers.ValidationError("company_asset_id must be provided.")
        if not CompanyAsset.objects.filter(company_asset_id=value, company_unique_identifier=this_company_unique_identifier).exists:
            raise serializers.ValidationError("This asset is not belongs to this company.")

        """
        Validate that the asset already assigned or not.
        """
        if CompanyAsset.objects.filter(company_asset_id=value, company_unique_identifier=this_company_unique_identifier).values('asset_status').first()['asset_status'] != 'free':
            raise serializers.ValidationError("This asset is already assigned to someone.")

        return value

    def create(self, validated_data):
        # Access the request object from the context
        request = self.context.get('request')

        current_user = request.session.get('username')

        current_user_object = CompanyUser.objects.filter(username=current_user).values('company_name', 'company_unique_identifier')
        validated_data['company_name'] = current_user_object[0]['company_name']
        validated_data['company_unique_identifier'] = current_user_object[0]['company_unique_identifier']

        assigned_asset_object = CompanyAsset.objects.filter(company_asset_id=validated_data['company_asset_id']).values('asset_condition')
        validated_data['assigned_asset_condition'] = assigned_asset_object[0]['asset_condition']

        # Create the CompanyEmployee object first
        company_employee_asset = CompanyEmployeeAsset.objects.create(**validated_data)
        company_employee_asset.save()

        #set asset_condition to old
        affected_rows = CompanyAsset.objects.filter(company_asset_id= validated_data['company_asset_id']).update(asset_condition='used', asset_status='assigned')

        return company_employee_asset