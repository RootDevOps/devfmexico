from rest_framework import serializers
from .models import Assistants

class AssistantModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assistants
        fields = ('__all__')