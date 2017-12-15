from django.db import models
import uuid
# Create your models here.
class Store(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    username = models.CharField(max_length = 255)
    name_store = models.CharField(max_length = 255)
    address_store = models.CharField(max_length = 255)
    city_store = models.CharField(max_length = 255)
    state_store = models.CharField(max_length = 255)
    postal_store = models.CharField(max_length = 255)
    country_store = models.CharField(max_length = 255)
    phone_store = models.IntegerField()
    send_box = models.BooleanField(default = False)
    clabe = models.CharField(max_length = 255)
    timestamp = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name_store