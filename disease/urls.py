from disease.views import DiseaseViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('disease', DiseaseViewSet, basename='disease')
urlpatterns = router.urls