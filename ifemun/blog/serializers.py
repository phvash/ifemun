from rest_framework import serializers
from ifemun.blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'short_summary', 'text', 'picture', 'created_date', 'published_date')