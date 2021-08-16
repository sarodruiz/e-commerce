from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
SIZE = [
    ('s', 'Small'),
    ('l', 'Large')
]

class User(AbstractUser):
    pass

class Pizza(models.Model):
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    size = models.CharField(max_length=1, choices=SIZE, default=SIZE[0][0])
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.URLField()

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order")
    items = models.ManyToManyField(Pizza, related_name="orders")