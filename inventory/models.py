# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

# User Model (Extending Django’s built-in user authentication)
class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='staff')

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="inventory_users",  # ✅ Add a unique related_name
        blank=True
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="inventory_user_permissions",  # ✅ Add a unique related_name
        blank=True
    )

    def __str__(self):
        return self.username

# Category Model
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

# Supplier Model
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Product Model
class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# Order Model (Stock In/Out)
class Order(models.Model):
    ORDER_TYPE_CHOICES = (
        ('in', 'Stock In'),
        ('out', 'Stock Out'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_type = models.CharField(max_length=10, choices=ORDER_TYPE_CHOICES)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.order_type}"

# Order Items Model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

# Inventory Logs Model
class InventoryLog(models.Model):
    CHANGE_TYPE_CHOICES = (
        ('added', 'Added'),
        ('removed', 'Removed'),
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    change_type = models.CharField(max_length=10, choices=CHANGE_TYPE_CHOICES)
    quantity_changed = models.IntegerField()
    log_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.change_type} {self.quantity_changed} of {self.product.name}"
