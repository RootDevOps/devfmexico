from rest_framework import serializers
from .models import Cutflowers

class CutflowerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cutflowers
        fields = ('__all__')