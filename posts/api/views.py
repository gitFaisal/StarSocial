from rest_framework.generics import (
                            ListAPIView,
                            UpdateAPIView,
                            DestroyAPIView,
                            RetrieveAPIView,
                            )
from  posts.models import Post
from .serializers import PostListSerializer, PostDetailSerializer

class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer

class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

class PostUpdateView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
