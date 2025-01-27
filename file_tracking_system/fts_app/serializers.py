from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from .models import CustomUser, Loan, Education, Awards, Punishments, Office
from django.contrib.auth import get_user_model
from .models import CustomUser, Loan, Education, Awards, Punishments, Office, Designation, Tippani, LettersAndDocuments, \
    File, Approval
from django.contrib.auth import authenticate

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
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},
            'citizenship_id': {'required': True},
            'employee_id': {'required': True},
        }

    def validate(self, data):
        """
        Validate the data before creating or updating a user.
        """
        # Ensure required fields are present
        if 'citizenship_id' not in data:
            raise ValidationError("Citizenship ID is required.")
        if 'employee_id' not in data:
            raise ValidationError("Employee ID is required.")
        return data

    def create(self, validated_data):
        """
        Create a new user with nested relationships.
        """
        # Extract nested data
        education_data = validated_data.pop('education', None)
        awards_data = validated_data.pop('awards', None)
        punishments_data = validated_data.pop('punishments', None)
        loan_data = validated_data.pop('loan', None)
        office_data = validated_data.pop('office', None)

        # Create user
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()

        # Create and link nested objects
        if education_data:
            education = Education.objects.create(**education_data)
            user.education = education

        if awards_data:
            award = Awards.objects.create(**awards_data)
            user.awards = award

        if punishments_data:
            punishment = Punishments.objects.create(**punishments_data)
            user.punishments = punishment

        if loan_data:
            loan = Loan.objects.create(**loan_data)
            user.loan = loan

        if office_data:
            office = Office.objects.create(**office_data)
            user.office = office

        user.save()
        return user

    def update(self, instance, validated_data):
        """
        Update an existing user with nested relationships.
        """
        # Handle nested updates
        education_data = validated_data.pop('education', None)
        awards_data = validated_data.pop('awards', None)
        punishments_data = validated_data.pop('punishments', None)
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
            award = Awards.objects.create(**awards_data)
            instance.awards = award

        if punishments_data:
            instance.punishments.clear()
            punishment = Punishments.objects.create(**punishments_data)
            instance.punishments = punishment

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
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if not user.is_active:
                    raise ValidationError("User account is disabled.")
                return {'user': user}
            else:
                raise ValidationError("Invalid credentials.")
        else:
            raise ValidationError("Must include 'username' and 'password'.")


class UserProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for updating user profile information.
    """
    class Meta:
        model = CustomUser
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    education = serializers.SerializerMethodField()
    awards = serializers.SerializerMethodField()
    punishments = serializers.SerializerMethodField()
    loan = serializers.SerializerMethodField()
    office = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = [
            'id', 'username', 'email', 'employee_id', 'position', 'perm_state', 'perm_district', 'perm_municipality',
            'temp_state', 'temp_district', 'temp_municipality', 'citizenship_id', 'citizenship_date_of_issue',
            'citizenship_district', 'home_number', 'phone_number', 'mobile_number', 'date_joined', 'recess_date',
            'employee_type', 'na_la_kos_no', 'accumulation_fund_no', 'bank_account_no', 'bank_name',
            'education', 'awards', 'punishments', 'loan', 'office'
        ]

    def get_education(self, obj):
        if obj.education:
            return {
                "education_level": obj.education.education_level,
                "institution": obj.education.institution,
                "board": obj.education.board,
                "percentage": obj.education.percentage,
                "year": obj.education.year
            }
        return None

    def get_awards(self, obj):
        if obj.awards:
            return {
                "name": obj.awards.name,
                "description": obj.awards.description
            }
        return None

    def get_punishments(self, obj):
        if obj.punishments:
            return {
                "name": obj.punishments.name,
                "description": obj.punishments.description
            }
        return None

    def get_loan(self, obj):
        if obj.loan:
            return {
                "loan_type": obj.loan.loan_type,
                "name": obj.loan.name,
                "interest_rate": obj.loan.interest_rate,
                "max_amount": obj.loan.max_amount,
                "min_amount": obj.loan.min_amount,
                "max_tenure": obj.loan.max_tenure,
                "min_tenure": obj.loan.min_tenure
            }
        return None

    def get_office(self, obj):
        if obj.office:
            return {
                "office_name": obj.office.office_name,
                "position": obj.office.position,
                "position_category": obj.office.position_category,
                "duration": obj.office.duration
            }
        return None        


class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Designation
        fields = '__all__'


class TippaniSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tippani
        fields = '__all__'


class LettersAndDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LettersAndDocuments
        fields = '__all__'


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = '__all__'  # ['id', 'file']


class ApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Approval
        fields = '__all__'
