from rest_framework import serializers
from .models import Store
from modules.assistants.serializers import AssistantModelSerializer
from modules.cutflowers.serializers import CutflowerModelSerializer

class StoreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('__all__')
        
class StoreAssistantSerializer(serializers.ModelSerializer):
    assistants = AssistantModelSerializer(many = True, read_only = True)
    cut_flowers = CutflowerModelSerializer(many = True, read_only = True)
    class Meta:
        model = Store
        fields = ('id','username','name_store','address_store','city_store','state_store','postal_store','country_store','phone_store','send_box','clabe','assistants','cut_flowers')