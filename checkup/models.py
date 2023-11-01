import uuid
from django.db import models
from disease.models import Disease
from prescription.models import Prescription 
from patient.models import Patient
from doctor.models import Doctor
from appointment.models import Appointment


# Checkup Model Class
class CheckUp(models.Model):
    checkup_id =  models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    doctor_id = models.ForeignKey(Doctor, default = uuid.uuid4, on_delete = models.CASCADE)
    patient_id = models.ForeignKey(Patient, default = uuid.uuid4, on_delete = models.CASCADE)
    appointment_id = models.ForeignKey(Appointment, default = uuid.uuid4, on_delete = models.CASCADE)
    disease_id =  models.ForeignKey(Disease, default = uuid.uuid4, on_delete = models.CASCADE)
    prescription_id =  models.ForeignKey(Prescription, default = uuid.uuid4, on_delete = models.CASCADE )
    check_status =  models.CharField(max_length = 255)
    next_appointment_date = models.DateField()
    next_appointment_time = models.TimeField()
    
    
    
    
    
