from django.conf import settings
from rest_framework.pagination import CursorPagination


class PostsPagination(CursorPagination):
    page_size = settings.POSTS_PAGE_SIZE
