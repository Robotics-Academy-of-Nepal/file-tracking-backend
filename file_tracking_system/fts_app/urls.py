
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet ,get_provinces, get_districts, get_municipalities

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')


urlpatterns = [
    path('api/', include(router.urls)),
    path('api/provinces/', get_provinces, name='get-provinces'),
    path('api/districts/<str:province>/', get_districts, name='get-districts'),
    path('api/municipalities/<str:province>/<str:district>/', get_municipalities, name='get-municipalities'),
]
