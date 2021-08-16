from django.contrib import admin
from .models import User, Pizza, OrderItem, Order

# Register your models here.
admin.site.register(User)
admin.site.register(Pizza)
admin.site.register(OrderItem)
admin.site.register(Order)