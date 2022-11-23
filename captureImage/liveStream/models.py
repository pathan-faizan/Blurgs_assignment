# Create your models here.
from django.db import models

# Create your models here.
class LiveImage(models.Model):
    image = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image.url