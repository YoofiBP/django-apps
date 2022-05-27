from django.db import models
from time import time
from math import ceil
from random import random


# Create your models here.
class Image(models.Model):
    data = models.BinaryField()
    content_type = models.CharField(max_length=30)


class User(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    image = models.OneToOneField(
        Image,
        on_delete=models.CASCADE,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'users'
