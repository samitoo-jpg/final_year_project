from django.contrib import admin
from .models import User, Category, Supplier, Product, Order, OrderItem, InventoryLog, Sale, InventoryPrediction, UserActivityLog

# ✅ User Admin
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role', 'is_active')
    search_fields = ('username', 'email', 'role')
    list_filter = ('role', 'is_active')

# ✅ Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)

# ✅ Supplier Admin
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact_person', 'phone', 'email', 'created_at')
    search_fields = ('name', 'contact_person', 'email')
    list_filter = ('created_at',)

# ✅ Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'supplier', 'stock_quantity', 'price', 'last_updated')
    search_fields = ('name',)
    list_filter = ('category', 'supplier')

# ✅ Order Admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'order_type', 'total_amount', 'order_date')
    search_fields = ('user__username',)
    list_filter = ('order_type', 'order_date')

# ✅ Order Item Admin
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity', 'price')
    search_fields = ('product__name',)

# ✅ Inventory Log Admin
@admin.register(InventoryLog)
class InventoryLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'change_type', 'quantity_changed', 'log_date')
    search_fields = ('product__name',)
    list_filter = ('change_type', 'log_date')

# ✅ Sale Admin
@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity_sold', 'date_sold')
    search_fields = ('product__name',)
    list_filter = ('date_sold',)

# ✅ Inventory Prediction Admin
@admin.register(InventoryPrediction)
class InventoryPredictionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'predicted_demand', 'confidence_score', 'prediction_date')
    search_fields = ('product__name',)
    list_filter = ('prediction_date',)

# ✅ User Activity Log Admin
@admin.register(UserActivityLog)
class UserActivityLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'action', 'table_name', 'record_id', 'timestamp')
    search_fields = ('user__username', 'action', 'table_name')
    list_filter = ('timestamp',)

# Register your models here.
