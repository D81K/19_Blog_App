from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import PostSerializer
from rest_framework.permissions import IsAdminUser


# Create your views here.

class PostListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminUser]