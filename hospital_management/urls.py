from django.contrib import admin
from django.urls import path, include

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title = "Hospital Management System",
      default_version = 'v1',),
   public = True,
   permission_classes = (permissions.AllowAny,),
)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api/docs/', schema_view.with_ui('swagger', cache_timeout = 0),name = 'schema-swagger-ui'),
   path('api/', include('appointment.urls')),
   path('api/', include('patient.urls')),
   path('api/', include('doctor.urls')),
   path('api/', include('disease.urls')),
   path('api/', include('hospital.urls')),
   path('api/', include('prescription.urls')),
   path('api/', include('checkup.urls')),
   path('api/', include('user.urls')),
   path('api/', include('employee.urls')),
]
