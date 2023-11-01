from django.db import models
from patient.models import Patient
from doctor.models import Doctor
from disease.models import Disease
import uuid


# Appointment Model Class
class Appointment(models.Model):
    appointment_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    patient_id = models.ForeignKey(Patient, default = uuid.uuid4, on_delete = models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, default = uuid.uuid4, on_delete = models.CASCADE)
    disease_id =  models.ForeignKey(Disease, default = uuid.uuid4, on_delete = models.CASCADE)
    appointment_time = models.TimeField()
    appointment_date = models.DateField()
    status = models.CharField(max_length = 255)
