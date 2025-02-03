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
    UserDetailSerializer,
    TippaniSerializer, 
    LettersAndDocumentsSerializer, 
    FileSerializer, 
    DesignationSerializer, 
    ApprovalSerializer,
    LoanSerializer,
    EducationSerializer,
    OfficeSerializer,
    AwardsSerializer,
    PunishmentsSerializer
)
from .models import (
    CustomUser,
    Approval, 
    Designation, 
    File , 
    LettersAndDocuments, 
    Tippani, 
    Loan , 
    Education, 
    Awards, 
    Punishments, 
    Office
)

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
        print(request.data)
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
    
    @action(detail=False, methods=['get'], url_path='all')
    def get_all_users(self, request):
        """
        Get details of all users.
        """
        users = CustomUser.objects.all()
        serializer = UserDetailSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], url_path='details')
    def get_user_details(self, request, pk=None):
        """
        Get details of a specific user by ID.
        """
        try:
            user = CustomUser.objects.get(pk=pk)
            serializer = UserDetailSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response(
                {"detail": "User not found."},
                status=status.HTTP_404_NOT_FOUND
            )

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

class TippaniViewSet(viewsets.ModelViewSet):
    queryset = Tippani.objects.all()
    serializer_class = TippaniSerializer

class LettersAndDocumentsViewSet(viewsets.ModelViewSet):
    queryset = LettersAndDocuments.objects.all()
    serializer_class = LettersAndDocumentsSerializer

    def get_queryset(self):
        queryset = LettersAndDocuments.objects.all()
        tippani_id = self.request.query_params.get('tippani_id', None)
        if tippani_id is not None:
            queryset = queryset.filter(tippani_id=tippani_id)
        return queryset


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def get_queryset(self):
        queryset = File.objects.all()
        letter_document_id = self.request.query_params.get('letter_document_id', None)
        if letter_document_id is not None:
            queryset = queryset.filter(letter_document_id=letter_document_id)
        return queryset
    
class DesignationViewSet(viewsets.ModelViewSet):
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class ApprovalViewSet(viewsets.ModelViewSet):
    queryset = Approval.objects.all()
    serializer_class = ApprovalSerializer

    def get_queryset(self):
        queryset = Approval.objects.all()
        tippani_id = self.request.query_params.get('tippani_id', None)
        if tippani_id is not None:
            queryset = queryset.filter(tippani_id=tippani_id)
        return queryset
    
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
