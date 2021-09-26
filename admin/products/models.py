from django.db import models

# Create your models here.
class Product(models.Model):
    # Product will have ID, title, images, likes
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0) # optional field bc default is set

class User(models.Model):
    pass  # User will have only ID