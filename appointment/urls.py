from appointment.views import AppointmentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('appointment', AppointmentViewSet, basename='appointment')
urlpatterns = router.urls