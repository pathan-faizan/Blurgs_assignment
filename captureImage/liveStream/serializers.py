from rest_framework import serializers
from . models import LiveImage

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveImage
        fields = '__all__'