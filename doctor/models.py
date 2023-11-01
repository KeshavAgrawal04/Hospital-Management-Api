from django.db import models
from employee.models import Employee
import uuid


# Doctor Model Class
class Doctor(models.Model):
    doctor_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    employee_id = models.ForeignKey(Employee, default = uuid.uuid4, on_delete=models.CASCADE)
    # doctor_profile_picture = models.ImageField(upload_to='doctor_profile_picture/')
    disease_specialist = models.CharField(max_length = 255)
    doctor_type = models.CharField(max_length = 255)
    # doctor_time_schedule = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)