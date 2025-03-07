# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse 
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication 

# Import models
from .models import User, Category, Supplier, Product, Order, OrderItem, InventoryLog, Sale, InventoryPrediction, UserActivityLog

# Import serializers
from .serializers import (
    UserSerializer, CategorySerializer, SupplierSerializer, 
    ProductSerializer, OrderSerializer, OrderItemSerializer, 
    InventoryLogSerializer, SaleSerializer, InventoryPredictionSerializer
)

# ✅ Basic function-based views for testing
def home(request):
    return HttpResponse("Welcome to Inventory Automation")  

def about(request):
    return HttpResponse("Welcome to Inventory Automation")  

# ✅ API ViewSet for managing Users
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ✅ API ViewSet for managing Categories
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# ✅ API ViewSet for managing Suppliers
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

# ✅ API ViewSet for managing Products
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # 🔴 No authentication required (public access)
    authentication_classes = []  # Remove authentication
    permission_classes = []  # Remove permission restrictions

# ✅ API ViewSet for managing Orders
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# ✅ API ViewSet for managing Order Items
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

# ✅ API ViewSet for managing Inventory Logs
class InventoryLogViewSet(viewsets.ModelViewSet):
    queryset = InventoryLog.objects.all()
    serializer_class = InventoryLogSerializer

# ✅ API ViewSet for managing Sales
class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

# ✅ API ViewSet for AI Inventory Predictions
class InventoryPredictionViewSet(viewsets.ModelViewSet):
    queryset = InventoryPrediction.objects.all()
    serializer_class = InventoryPredictionSerializer

# ✅ API to update inventory stock
@api_view(['POST'])
def update_inventory(request):
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity')
    change_type = request.data.get('change_type')  # 'added' or 'removed'

    product = get_object_or_404(Product, id=product_id)

    if change_type == 'added':
        product.stock_quantity += int(quantity)
    elif change_type == 'removed' and product.stock_quantity >= int(quantity):
        product.stock_quantity -= int(quantity)
    else:
        return Response({"error": "Invalid operation"}, status=400)

    product.save()

    # Log the inventory change
    InventoryLog.objects.create(product=product, change_type=change_type, quantity_changed=quantity)

    return Response({"message": "Inventory updated successfully"})

# ✅ API to fetch all inventory items
@api_view(['GET'])
def get_inventory(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# ✅ Function to log user activity
def log_user_activity(user, action, table_name, record_id=None):
    UserActivityLog.objects.create(
        user=user,
        action=action,
        table_name=table_name,
        record_id=record_id
    )



