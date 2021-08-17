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

class OrderItem(models.Model):
    item = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def final_price(self):
        return self.item.price * self.quantity

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order")
    items = models.ManyToManyField(OrderItem, related_name="orders")
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    placed = models.BooleanField(default=False)

    def final_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.final_price()
        return total