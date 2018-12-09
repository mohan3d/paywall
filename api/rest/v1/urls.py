from django.urls import path, re_path
from django.utils.dateparse import datetime_re
from rest_framework.authtoken.views import obtain_auth_token

from .views import CreateUserView, PostListCreateView, PostListByCreatedView

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', CreateUserView.as_view(), name='register'),

    path('posts/', PostListCreateView.as_view(), name='posts'),
]

DATETIME_REGEX = datetime_re.pattern[:-1]

urlpatterns += [
    re_path(
        r'^posts/(?P<timestamp>{})/$'.format(DATETIME_REGEX),
        PostListByCreatedView.as_view(),
        name='posts-filter'
    ),
]
