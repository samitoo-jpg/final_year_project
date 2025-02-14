from django.contrib import admin
from .models import User, Category, Supplier, Product, Order, OrderItem, InventoryLog

# Register models to appear in the Django Admin Panel
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(InventoryLog)

# Register your models here.
