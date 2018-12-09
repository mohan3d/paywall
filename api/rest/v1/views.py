from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from paywall.utils import send_welcome_email
from posts.models import Post
from .serializers import CreateUserSerializer, PostSerializer
from .paginators import PostsPagination

User = get_user_model()


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        send_welcome_email(request.data['email'])
        return response


class PostListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = PostsPagination

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostListByCreatedView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        timestamp = self.kwargs['timestamp']
        return Post.objects.after(timestamp)
