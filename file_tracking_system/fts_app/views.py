from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .serializers import (
    UserRegistrationSerializer,
    UserLoginSerializer,
    UserProfileSerializer,
    LoanSerializer,
    EducationSerializer,
    AwardsSerializer,
    PunishmentsSerializer,
    OfficeSerializer
)
from .models import CustomUser, Loan, Education, Awards, Punishments, Office


class UserViewSet(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    parser_classes = [MultiPartParser, FormParser, JSONParser]
    
    def get_permissions(self):
        """
        Assign permissions based on the action.
        """
        if self.action in ['register', 'login']:
            return [AllowAny()]
        return [IsAuthenticated()]

    @action(detail=False, methods=['post'], url_path='register')
    def register(self, request):
        """
        Register a new user.
        """
        serializer = UserRegistrationSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "employee_id": user.employee_id,
                    "position": user.position
                },
                "token": token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        """
        Authenticate and log in a user.
        """
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "employee_id": user.employee_id,
                    "position": user.position,
                    "province": user.perm_state,
                    "district": user.perm_district,
                    "municipality": user.perm_municipality
                },
                "token": token.key
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'], url_path='logout')
    def logout(self, request):
        """
        Log out the current user by deleting their token.
        """
        try:
            request.user.auth_token.delete()
            return Response(
                {"detail": "Successfully logged out"},
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"detail": "Failed to log out. Please try again."},
                status=status.HTTP_400_BAD_REQUEST
            )

    @action(detail=False, methods=['put', 'patch'], url_path='me')
    def update_profile(self, request):
        """
        Update the profile of the current user.
        """
        user = request.user
        serializer = UserProfileSerializer(
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
    """
    Get a list of all provinces.
    """
    provinces = [choice[0] for choice in CustomUser.Province.choices]
    return Response(provinces, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_districts(request, province):
    """
    Get a list of districts for a given province.
    """
    if province not in [choice[0] for choice in CustomUser.Province.choices]:
        return Response({"error": "Invalid province"}, status=status.HTTP_400_BAD_REQUEST)
    districts = CustomUser.get_district_choices(province)
    return Response(districts, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_municipalities(request, province, district):
    """
    Get a list of municipalities for a given district and province.
    """
    if province not in [choice[0] for choice in CustomUser.Province.choices]:
        return Response({"error": "Invalid province"}, status=status.HTTP_400_BAD_REQUEST)
    districts = CustomUser.get_district_choices(province)
    if district not in districts:
        return Response({"error": "Invalid district"}, status=status.HTTP_400_BAD_REQUEST)
    municipalities = CustomUser.get_municipality_choices(province, district)
    return Response(municipalities, status=status.HTTP_200_OK)


# Example views for other models (optional)
class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

class AwardsViewSet(viewsets.ModelViewSet):
    queryset = Awards.objects.all()
    serializer_class = AwardsSerializer


class PunishmentsViewSet(viewsets.ModelViewSet):
    queryset = Punishments.objects.all()
    serializer_class = PunishmentsSerializer


class OfficeViewSet(viewsets.ModelViewSet):
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer