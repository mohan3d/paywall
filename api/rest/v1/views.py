from django.contrib.auth import get_user_model
from rest_framework import generics

from paywall.utils import send_welcome_email
from .serializers import CreateUserSerializer

User = get_user_model()


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        send_welcome_email(request.data['email'])
        return response
