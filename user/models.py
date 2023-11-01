from django.db import models
import uuid


# User Model Class
class User(models.Model):
    user_id  = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    member_id = models.UUIDField(default = uuid.uuid4, editable = False)
    username = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
