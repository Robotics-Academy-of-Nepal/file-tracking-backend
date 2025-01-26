
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, get_provinces, get_districts, get_municipalities
router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')



urlpatterns = [
    path('', include(router.urls)),
    path('provinces/', get_provinces, name='get-provinces'),
    path('districts/<str:province>/', get_districts, name='get-districts'),
    path('municipalities/<str:province>/<str:district>/', get_municipalities, name='get-municipalities'),
]
