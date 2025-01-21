from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from fts_app.views import UserViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
