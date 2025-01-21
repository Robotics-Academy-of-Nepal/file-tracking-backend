from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser , Branch , Role , File , Tippani
from django.contrib.auth import get_user_model


CustomUser = get_user_model()

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'       


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'branch', 'role')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Remove many-to-many fields from validated_data
        branch = validated_data.pop('branch', None)
        role = validated_data.pop('role', None)

        # Create user instance
        user = CustomUser.objects.create_user(**validated_data)

        # Set many-to-many fields after saving the user instance
        if branch:
            user.branch = branch
        if role:
            user.role = role
        user.save()

        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        # Authenticate the user
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Invalid credentials")
        return user
