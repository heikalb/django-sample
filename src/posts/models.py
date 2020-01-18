from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)
    # picture = models.FileField(upload_to='uploads/', blank=True, null=True)
    picture = models.ImageField(upload_to='uploads/', blank=True, null=True)
    description = models.TextField(null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=80, blank=True, null=True)
    date_posted = models.DateField(auto_now=True)
    award = models.DecimalField(max_digits=100, decimal_places=2, blank=True,
                                null=True, default=0.00)
    password = models.CharField(default='password', max_length=100)

    def get_absolute_url(self):
        # return f'/posts/{self.id}'
        return reverse('post-detail', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('post-delete', kwargs={'id': self.id})


class LostPost(Post):
    pass


class FoundPost(Post):
    pass
