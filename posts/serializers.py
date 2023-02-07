from rest_framework import serializers
from .models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)
    
    detail_url = serializers.HyperlinkedIdentityField(
        view_name='detail',
        lookup_field='slug',
    )

    class Meta:
        model = Post
        fields = '__all__'
