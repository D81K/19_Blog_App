from django.urls import path
from .views import PostListCreateView, PostDetailView



urlpatterns = [
    path('posts/', PostListCreateView.as_view()),
    path('posts/<slug>/', PostDetailView.as_view(), name='detail'),
]
