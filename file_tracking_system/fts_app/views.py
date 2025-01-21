from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.authtoken.models import Token

from .serializers import UserRegistrationSerializer , UserLoginSerializer

class UserViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'], url_path='register', permission_classes=[AllowAny])
    def register(self, request):
        """
        Handles user registration.
        """
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            # Save the user instance
            user = serializer.save()

            # Create an authentication token for the user
            token, created = Token.objects.get_or_create(user=user)

            return Response({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "branch": user.branch.name if user.branch else None,
                "role": user.role.name if user.role else None,
                "token": token.key  # Include the token in the response
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # User login
    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            # Generate a token for the logged-in user
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "branch": user.branch.name if user.branch else None,
                "role": user.role.name if user.role else None,
                "token": token.key  # Include the token in the response
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # User logout
    @action(detail=False, methods=['post'], url_path='logout')
    def logout(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
 