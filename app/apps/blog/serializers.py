from rest_framework import serializers
from .models import Post
from apps.category.serializers import CategorySerializer
class PostSerializer(serializers.ModelSerializer):
    
    thumbnail = serializers.charField(source='get_thumbnail')
    video = serializers.charField(source='get_video')
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = ['blog_uuid','title', 'slug', 'thmbnail', 'video', 'description', 'excerpt', 'category', 'published', 'status']