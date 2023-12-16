from email.policy import default
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)
    description = models.TextField()
    steps = models.TextField()
    make_time = models.DurationField(default=None)
    image = models.ImageField(upload_to='photo/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
