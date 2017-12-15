from django.db import models
import uuid
from modules.stores.models import Store

# Create your models here.
class Cutflowers(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    image_cutflower = models.CharField(max_length = 255)
    name_cutflower = models.CharField(max_length = 255)
    weight_cutflower = models.CharField(max_length = 255)
    description_cutflower = models.TextField()
    price_cutflower = models.DecimalField(decimal_places = 2, max_digits = 6)
    pricesend_cutflower = models.DecimalField(decimal_places = 2, max_digits = 6)
    fkstore = models.ForeignKey(Store, on_delete= models.CASCADE, related_name="cut_flowers")
    timestamp = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name_cutflower