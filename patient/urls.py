from patient.views import PatientViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('patient', PatientViewSet, basename = 'patient')
urlpatterns = router.urls