from rest_framework import serializers
from .models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    model = Post
    fields = "__all__"
