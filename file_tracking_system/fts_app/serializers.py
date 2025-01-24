from rest_framework import serializers
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
    # Nested serializers for related fields
    loan = LoanSerializer(required=False)
    education = EducationSerializer(required=True)
    awards = AwardsSerializer(many=True, required=False)
    punishments = PunishmentsSerializer(many=True, required=False)
    office = OfficeSerializer(required=False)

    # Explicitly declare all fields from CustomUser
    perm_state = serializers.ChoiceField(choices=CustomUser.PROVINCE_CHOICES)
    perm_district = serializers.CharField()
    perm_municipality = serializers.CharField()
    perm_ward_no = serializers.CharField()
    temp_state = serializers.ChoiceField(choices=CustomUser.PROVINCE_CHOICES)
    temp_district = serializers.CharField()
    temp_municipality = serializers.CharField()
    temp_ward_no = serializers.CharField()
    citizenship_id = serializers.CharField()
    citizenship_date_of_issue = serializers.DateField()
    citizenship_district = serializers.CharField()
    citizenship_front_image = serializers.ImageField()
    citizenship_back_image = serializers.ImageField()
    home_number = serializers.CharField()
    phone_number = serializers.CharField()
    mobile_number = serializers.CharField()
    date_joined = serializers.DateTimeField()
    recess_date = serializers.DateTimeField()
    position = serializers.CharField()
    position_category = serializers.ChoiceField(choices=CustomUser.position_category_choices)
    employee_type = serializers.ChoiceField(choices=CustomUser.EMPLOYEE_TYPE_CHOICES)
    empolyee_id = serializers.CharField()
    na_la_kos_no = serializers.CharField()
    accumulation_fund_no = serializers.CharField()
    bank_account_no = serializers.CharField()
    bank_name = serializers.ChoiceField(choices=CustomUser.BANK_CHOICES)

    class Meta:
        model = CustomUser
        fields = [
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
            'employee_type','empolyee_id', 'na_la_kos_no', 'accumulation_fund_no',
            'bank_account_no', 'bank_name', 'position', 'position_category',
            # Dates
            'date_joined', 'recess_date',
            # Nested relationships
            'loan', 'education', 'awards', 'punishments', 'office'
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'citizenship_front_image': {'required': True},
            'citizenship_back_image': {'required': True}
        }

    def validate(self, data):
        # Validate permanent address
        if data.get('perm_state'):
            valid_districts = CustomUser.get_district_choices(data['perm_state'])
            if data.get('perm_district') not in valid_districts:
                raise serializers.ValidationError({
                    'perm_district': 'Invalid district for selected province'
                })

        # Validate temporary address
        if data.get('temp_state'):
            valid_temp_districts = CustomUser.get_district_choices(data['temp_state'])
            if data.get('temp_district') not in valid_temp_districts:
                raise serializers.ValidationError({
                    'temp_district': 'Invalid district for selected province'
                })
        
        return data

    def create(self, validated_data):
        # Extract nested data
        loan_data = validated_data.pop('loan', None)
        education_data = validated_data.pop('education')
        awards_data = validated_data.pop('awards', [])
        punishments_data = validated_data.pop('punishments', [])
        office_data = validated_data.pop('office', None)

        # Create user
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(password=password, **validated_data)

        # Create related objects
        if loan_data:
            user.loan = Loan.objects.create(**loan_data)
        
        education = Education.objects.create(**education_data)
        user.education = education

        for award_data in awards_data:
            award = Awards.objects.create(**award_data)
            user.awards.add(award)

        for punishment_data in punishments_data:
            punishment = Punishments.objects.create(**punishment_data)
            user.punishments.add(punishment)

        if office_data:
            office = Office.objects.create(**office_data)
            user.office = office

        user.save()
        return user
    
    def update(self, instance, validated_data):
        # Remove nested data from update
        validated_data.pop('loan', None)
        validated_data.pop('education', None)
        validated_data.pop('awards', None)
        validated_data.pop('punishments', None)
        validated_data.pop('office', None)

        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        
        return super().update(instance, validated_data)

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Invalid credentials")
        
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled")
        
        return {
            'user': user,
            'token': user.auth_token.key
        }


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
