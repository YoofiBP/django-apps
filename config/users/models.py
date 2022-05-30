from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.
class Image(models.Model):
    data = models.BinaryField()
    content_type = models.CharField(max_length=30)


class User(AbstractBaseUser):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    image = models.OneToOneField(
        Image,
        on_delete=models.CASCADE,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        db_table = 'users'
