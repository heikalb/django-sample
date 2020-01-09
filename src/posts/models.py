from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=80)
    picture = models.FileField(upload_to='uploads/', blank=True, null=True)
    description = models.TextField()
    contact_1 = models.CharField(max_length=80)
    contact_2 = models.CharField(max_length=80, blank=True, null=True)
    date_posted = models.DateField(auto_now=True)

    def get_absolute_url(self):
        # return f'/posts/{self.id}'
        return reverse('post-detail', kwargs={'id': self.id})


class LostPost(Post):
    award = models.DecimalField(max_digits=100, decimal_places=2, blank=True,
                                null=True, default=0.00)


class FoundPost(Post):
    pass
