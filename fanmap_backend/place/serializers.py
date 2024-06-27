from rest_framework.serializers import ModelSerializer
from .models import Place

class PlaceSerializer(ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'location', 'pName', 'purpose', 'sTime', 'eTime',
                  'basic_cate', 'detail_cate', 'require', 'link', 'thumbnail',
                  'image1', 'image2', 'image3']