from django.db import models
import uuid
from modules.stores.models import Store

# Create your models here.
class Assistants(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    name_assistants = models.CharField(max_length = 255)
    phone_assistants = models.IntegerField()
    email_assistants = models.EmailField()
    address_assistants = models.TextField()
    fkstore = models.ForeignKey(Store, on_delete= models.CASCADE, related_name="assistants")
    timestamp = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name_assistants