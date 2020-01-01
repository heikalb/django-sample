from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)
    picture = models.FileField(upload_to='uploads/', blank=True, null=True,)
    description = models.TextField(blank=True, null=True)
    award = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    contact = models.CharField(max_length=80)
    date_posted = models.DateField(auto_now=True, blank=True, null=True)