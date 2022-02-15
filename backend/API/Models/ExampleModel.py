from django.db import models


class Category(models.Model):
    Name = models.CharField(max_length=50)


# Create your models here.
class Video(models.Model):
    Title = models.CharField(max_length=256)
    Description = models.TextField()
    URL = models.URLField()
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
