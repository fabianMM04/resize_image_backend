from django.db import models

# Create your models here.

class Images(models.Model):
    imageId = models.AutoField(primary_key=True)
    images = models.ImageField(upload_to="photos")
    