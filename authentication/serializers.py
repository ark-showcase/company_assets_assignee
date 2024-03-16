from rest_framework import serializers

from .models import CompanyUser

class CompanyUserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CompanyUser
        fields = [
            'username',
            'company_name',
            'company_unique_identifier',
            'password',
            'email',
        ]

    def validate_company_name(self, value):
        """
        Validate that the company_name has a minimum length of 3 characters.
        """
        if not value:
            raise serializers.ValidationError("company name must be provided.")
        if len(value) < 3:
            raise serializers.ValidationError("The company name must be at least 3 characters long.")
        return value

    def create(self, validated_data):
        # Extract the company_name from the validated data
        company_name = validated_data.get('company_name')

        company_name_having = company_name.split(' ')

        # Calculate the unique identifier
        unique_identifier = ''

        for word in company_name_having:
            unique_identifier += word[:3].upper()

        # Create the CompanyUser object first
        company_user = CompanyUser.objects.create(**validated_data)

        # Set the company_unique_identifier attribute to the ID
        company_user.company_unique_identifier = unique_identifier+str(company_user.id)
        company_user.save()

        return company_user