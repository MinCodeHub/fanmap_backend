from rest_framework.serializers import ModelSerializer
from .models import Community, Comment

class CommunitySerializer(ModelSerializer):
    class Meta:
        model = Community
        fields = ['id', 'title', 'content', 'created_at', 'image', 'video', 'link', 'location']
    
class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'comment', 'date', 'post']