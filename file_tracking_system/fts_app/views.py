from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from .models import CustomUser

class UserViewSet(viewsets.ViewSet):
    queryset = CustomUser.objects.all() 
    authentication_classes = [TokenAuthentication]
    parser_classes = [MultiPartParser, FormParser]

    def get_permissions(self):
        if self.action in ['register', 'login']:
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=False, methods=['post'], url_path='register')
    def register(self, request):
        serializer = UserRegistrationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user=user)
            return Response({
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                },
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email
                },
                "token": token.key
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'], url_path='logout')
    def logout(self, request):
        request.user.auth_token.delete()
        return Response(
            {"detail": "Successfully logged out"},
            status=status.HTTP_200_OK
        )

    @action(detail=False, methods=['put', 'patch'], url_path='me')
    def update_profile(self, request):
        user = request.user
        serializer = UserRegistrationSerializer(
            user,
            data=request.data,
            partial=True,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Helper views for address data
@api_view(['GET'])
def get_provinces(request):
    provinces = [choice[0] for choice in CustomUser.PROVINCE_CHOICES]
    return Response(provinces, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_districts(request, province):
    districts = CustomUser.get_district_choices(province)
    return Response(districts, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_municipalities(request, province, district):
    municipalities = CustomUser.get_municipality_choices(province, district)
    return Response(municipalities, status=status.HTTP_200_OK)