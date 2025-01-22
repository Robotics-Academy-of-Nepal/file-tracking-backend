from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser 
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

CustomUser = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(queryset=Group.objects.all(), required=False, many=True)
    user_permissions = serializers.PrimaryKeyRelatedField(queryset=Permission.objects.all(), required=False, many=True)
    
    # Dynamic fields for districts and municipalities, as per province and district selected
    perm_district = serializers.ChoiceField(choices=[])
    perm_municipality = serializers.ChoiceField(choices=[])
    temp_district = serializers.ChoiceField(choices=[])
    temp_municipality = serializers.ChoiceField(choices=[])

    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Dynamically set district choices based on perm_state (province)
        perm_province = self.initial_data.get('perm_state', None)
        if perm_province:
            self.fields['perm_district'].choices = [(district, district) for district in CustomUser().get_district_choices(perm_province)]
        
        # Dynamically set municipality choices based on perm_state and perm_district
        perm_district = self.initial_data.get('perm_district', None)
        if perm_district and perm_province:
            self.fields['perm_municipality'].choices = [(municipality, municipality) for municipality in CustomUser().get_municipality_choices(perm_province, perm_district)]

        # Dynamically set temp_district choices based on temp_state (province)
        temp_province = self.initial_data.get('temp_state', None)
        if temp_province:
            self.fields['temp_district'].choices = [(district, district) for district in CustomUser().get_district_choices(temp_province)]
        
        # Dynamically set temp_municipality choices based on temp_state and temp_district
        temp_district = self.initial_data.get('temp_district', None)
        if temp_district and temp_province:
            self.fields['temp_municipality'].choices = [(municipality, municipality) for municipality in CustomUser().get_municipality_choices(temp_province, temp_district)]

    def create(self, validated_data):
        # Handle groups and permissions separately
        groups = validated_data.pop('groups', [])
        user_permissions = validated_data.pop('user_permissions', [])
        
        # Handle password hashing
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(password=password, **validated_data)
        
        # Assign groups and permissions if provided
        if groups:
            user.groups.set(groups)
        if user_permissions:
            user.user_permissions.set(user_permissions)
        
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        return user
