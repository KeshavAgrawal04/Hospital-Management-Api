from prescription.views import PrescriptionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', PrescriptionViewSet, basename = 'user')
urlpatterns = router.urls