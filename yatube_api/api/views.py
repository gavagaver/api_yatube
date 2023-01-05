from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from .permissions import IsAuthorOrReadOnly
from rest_framework.pagination import PageNumberPagination

from posts.models import Group, Post

from . import serializers


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer

    permission_classes = [IsAuthorOrReadOnly, ]
    pagination_class = None


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    permission_classes = [IsAuthorOrReadOnly, ]
    pagination_class = PageNumberPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CommentSerializer

    permission_classes = [IsAuthorOrReadOnly, ]
    pagination_class = None

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)
