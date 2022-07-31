from django.db import models
from django.conf import settings

class Tag(models.Model):
    value = models.TextField(max_length=100, unique=True)

    def __str__(self):
        return self.value


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True,  db_index=True)
    modified_at = models.DateTimeField(auto_now=True,  db_index=True)
    published_at = models.DateTimeField(blank=True, null=True, db_index=True)

    title = models.TextField(max_length=100)
    slug = models.SlugField(unique=True)
    summary = models.TextField(max_length=500)
    content = models.TextField()

    tags = models.ManyToManyField(Tag, related_name="posts")