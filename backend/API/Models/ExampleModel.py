from django.db import models

# Create your models here.
class Video(models.Model):
    Title = models.CharField(max_length=256)
    Description = models.TextField()
    URL = models.URLField()
    Category = models.ForeignKey()
