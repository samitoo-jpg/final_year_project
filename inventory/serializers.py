from .models import Product, Sale, InventoryPrediction
from rest_framework import serializers
from .models import User, Category, Supplier, Product, Order, OrderItem, InventoryLog



# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Supplier Serializer
class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    supplier = SupplierSerializer()

    class Meta:
        model = Product
        fields = '__all__'

# Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Order
        fields = '__all__'

# OrderItem Serializer
class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'

# Inventory Log Serializer
class InventoryLogSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = InventoryLog
        fields = '__all__'



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'

class InventoryPredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryPrediction
        fields = '__all__'
