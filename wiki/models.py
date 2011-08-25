from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    body = models.TextField()
    date_modified = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
