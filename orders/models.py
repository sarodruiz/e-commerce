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

    def __str__(self):
        return str(self.title)

class OrderItem(models.Model):
    item = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    #size = models.CharField(max_length=1, choices=SIZE, default=SIZE[0][0])

    def __str__(self):
        return f"{self.item} ({self.quantity})"

    def final_price(self):
        return self.item.price * self.quantity

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="order")
    items = models.ManyToManyField(OrderItem, related_name="orders")
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    placed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.pk}"

    def final_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.final_price()
        return total

    def final_price_cents(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.final_price()
        return f"{int(total * 100)}"

    def description(self):
        description = ""
        for order_item in self.items.all():
            description += f"{order_item}, "
        return description

    def is_empty(self):
        return self.items.all().count() == 0