from django.conf import settings
from django.db import models


class PostQuerySet(models.QuerySet):
    def after(self, timestamp):
        return self.filter(created__gt=timestamp)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    objects = PostQuerySet.as_manager()

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return "{}: {}".format(self.author.username, self.content[:20])
