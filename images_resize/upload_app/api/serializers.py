from rest_framework import serializers
from upload_app.models import Images

class ImageSerializer(serializers.Serializer):
    
    class Meta:
        model = Images
        fields = ('imageId', 'images')
        