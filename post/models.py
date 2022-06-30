from importlib.resources import contents
from django.db import models
from matplotlib.pyplot import title

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
