from hospital.views import HospitalViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hospital', HospitalViewSet, basename = 'hospital')
urlpatterns = router.urls