from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.TextField(default='Missing pet')
    description = models.TextField()
    award = models.TextField()
    contact = models.TextField(default='000-000-000')
