from checkup.views import CheckUpViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('checkup', CheckUpViewSet, basename='checkup')
urlpatterns = router.urls