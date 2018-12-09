from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import CreateUserView, PostListCreateView

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', CreateUserView.as_view(), name='register'),

    path('posts/', PostListCreateView.as_view(), name='posts'),
]
