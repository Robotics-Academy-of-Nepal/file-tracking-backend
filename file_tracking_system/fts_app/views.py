from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from fts_app.models import Group, Permission
from .models import CustomUser


class UserViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'], url_path='register', permission_classes=[AllowAny])
    def register(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            if 'groups' in request.data:
                groups = request.data['groups']
                group_objects = Group.objects.filter(id__in=groups)
                user.groups.set(group_objects)

            if 'user_permissions' in request.data:
                permissions = request.data['user_permissions']
                permission_objects = Permission.objects.filter(id__in=permissions)
                user.user_permissions.set(permission_objects)

            token, created = Token.objects.get_or_create(user=user)

            return Response({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "token": token.key
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "token": token.key  # Include the token in the response
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='logout')
    def logout(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_districts(request, province):
    """
    Fetch districts for the selected province. This doesn't depend on a logged-in user
    as it's just static data related to the province.
    """
    # Directly call CustomUser's method without using request.user
    districts = CustomUser().get_district_choices(province)
    return Response(districts, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_municipalities(request, province, district):
    """
    Fetch municipalities based on the selected province and district. 
    This method should not depend on the logged-in user.
    """
    # Directly call CustomUser's method without using request.user
    municipalities = CustomUser().get_municipality_choices(province, district)
    return Response(municipalities, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_provinces(request):
    """
    Fetch all available provinces.
    """
    provinces = [choice[0] for choice in CustomUser.PROVINCE_CHOICES]
    return Response(provinces, status=status.HTTP_200_OK)
