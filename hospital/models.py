from django.db import models
import uuid


# Hospital Model Class
class Hospital(models.Model):
    hospital_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    hospital_name = models.CharField(max_length = 255)
    hospital_email = models.EmailField(max_length = 255)
    hospital_phone = models.BigIntegerField()
    hospital_owner_name = models.CharField(max_length = 255)
    hospital_owner_phone = models.BigIntegerField()
    hospital_owner_email = models.EmailField(max_length = 255)
    hospital_address = models.CharField(max_length = 255)
    hospital_city = models.CharField(max_length = 255)
    hospital_status =  models.BooleanField()
    # hospital_logo = models.ImageField(upload_to = 'hospital_logo/')
    hospital_type = models.CharField(max_length = 255)
    hospital_category = models.CharField(max_length = 255)
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
