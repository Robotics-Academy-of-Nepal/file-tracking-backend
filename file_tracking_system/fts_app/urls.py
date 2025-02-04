
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    TippaniViewSet, 
    LettersAndDocumentsViewSet,
    FileViewSet, 
    DesignationViewSet, 
    ApprovalViewSet, 
    get_provinces, 
    get_districts, 
    get_municipalities,
    LoanViewSet,
    EducationViewSet,
    AwardsViewSet,
    PunishmentsViewSet,
    OfficeViewSet
)


router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'tippani', TippaniViewSet)
router.register(r'letter-document', LettersAndDocumentsViewSet)
router.register(r'file', FileViewSet)
router.register(r'designation', DesignationViewSet)
router.register(r'approval', ApprovalViewSet)
router.register(r'loans', LoanViewSet)
router.register(r'educations', EducationViewSet)
router.register(r'awards', AwardsViewSet)
router.register(r'punishments', PunishmentsViewSet)
router.register(r'offices', OfficeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('provinces/', get_provinces, name='get-provinces'),
    path('districts/<str:province>/', get_districts, name='get-districts'),
    path('municipalities/<str:province>/<str:district>/', get_municipalities, name='get-municipalities'),
]
