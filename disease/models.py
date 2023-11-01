from django.db import models
import uuid

# Create your models here.
class Disease(models.Model):
    disease_id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    disease_name = models.CharField(max_length = 255)
    disease_status = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    