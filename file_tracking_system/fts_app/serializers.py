from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser, Loan, Education, Awards, Punishments, Office
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

CustomUser = get_user_model()

# Nested serializers for related models
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class AwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awards
        fields = '__all__'

class PunishmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Punishments
        fields = '__all__'

class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = '__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    # Handle nested relationships as writable fields
    education = EducationSerializer(required=False)
    awards = AwardsSerializer(required=False)
    punishments = PunishmentsSerializer(required=False)
    office = OfficeSerializer(required=False)
    loan = LoanSerializer(required=False)

    class Meta:
        model = CustomUser
        fields = [
            # User fields
            'username', 'password', 'email', 
            # Address fields
            'perm_state', 'perm_district', 'perm_municipality', 'perm_ward_no',
            'temp_state', 'temp_district', 'temp_municipality', 'temp_ward_no',
            # Citizenship details
            'citizenship_id', 'citizenship_date_of_issue', 'citizenship_district',
            'citizenship_front_image', 'citizenship_back_image',
            # Contact info
            'home_number', 'phone_number', 'mobile_number',
            # Employment details
            'employee_id', 'employee_type', 'na_la_kos_no', 'accumulation_fund_no',
            'bank_account_no', 'bank_name', 'position', 'position_category',
            # Dates
            'date_joined', 'recess_date',
            # Nested relationships
            'loan', 'education', 'awards', 'punishments', 'office'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'citizenship_id': {'required': True},
            'employee_id': {'required': True},
        }

    def create(self, validated_data):
        # Extract nested data
        education_data = validated_data.pop('education', None)
        awards_data = validated_data.pop('awards', [])  # Default to empty list
        punishments_data = validated_data.pop('punishments', [])  # Default to empty list
        loan_data = validated_data.pop('loan', None)
        office_data = validated_data.pop('office', None)

        # Create user
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()

        # Create and link education
        if education_data:
            education = Education.objects.create(**education_data)
            user.education = education

        # Create and link awards
        for award_data in awards_data:  # This will work even if awards_data is an empty list
            award = Awards.objects.create(**award_data)
            user.awards.add(award)

        # Create and link punishments
        for punishment_data in punishments_data:  # This will work even if punishments_data is an empty list
            punishment = Punishments.objects.create(**punishment_data)
            user.punishments.add(punishment)

        # Create and link loan
        if loan_data:
            loan = Loan.objects.create(**loan_data)
            user.loan = loan

        # Create and link office
        if office_data:
            office = Office.objects.create(**office_data)
            user.office = office

        user.save()
        return user
    
    def update(self, instance, validated_data):
        """
        Update and return an existing user instance with nested relationships.
        """
        # Handle nested updates
        education_data = validated_data.pop('education', None)
        awards_data = validated_data.pop('awards', [])
        punishments_data = validated_data.pop('punishments', [])
        loan_data = validated_data.pop('loan', None)
        office_data = validated_data.pop('office', None)

        # Update user fields
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Update nested relationships
        if education_data:
            education_serializer = EducationSerializer(instance.education, data=education_data, partial=True)
            if education_serializer.is_valid():
                education_serializer.save()

        if awards_data:
            instance.awards.clear()
            for award_data in awards_data:
                award = Awards.objects.create(**award_data)
                instance.awards.add(award)

        if punishments_data:
            instance.punishments.clear()
            for punishment_data in punishments_data:
                punishment = Punishments.objects.create(**punishment_data)
                instance.punishments.add(punishment)

        if loan_data:
            loan_serializer = LoanSerializer(instance.loan, data=loan_data, partial=True)
            if loan_serializer.is_valid():
                loan_serializer.save()

        if office_data:
            office_serializer = OfficeSerializer(instance.office, data=office_data, partial=True)
            if office_serializer.is_valid():
                office_serializer.save()

        instance.save()
        return instance

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        """
        Validate user credentials.
        """
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise ValidationError("Invalid credentials")

        if not user.is_active:
            raise ValidationError("User account is disabled")

        return {
            'user': user,
            'token': user.auth_token.key
        }