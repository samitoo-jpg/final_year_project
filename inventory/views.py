# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse  
from rest_framework import viewsets
from .models import User, Category, Supplier, Product, Order, OrderItem, InventoryLog
from .models import Product, Sale, InventoryPrediction
from .serializers import UserSerializer, CategorySerializer, SupplierSerializer, OrderSerializer, ProductSerializer
from .serializers import SaleSerializer, InventoryPredictionSerializer
from .serializers import OrderItemSerializer, InventoryLogSerializer

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product, InventoryLog
from .serializers import ProductSerializer


@api_view(['POST'])
def update_inventory(request):
    """ Update inventory stock """
    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity')
    change_type = request.data.get('change_type')  # 'added' or 'removed'
    
    product = get_object_or_404(Product, id=product_id)
    
    if change_type == 'added':
        product.stock_quantity += int(quantity)
    elif change_type == 'removed' and product.stock >= int(quantity):
        product.stock_quantity -= int(quantity)
    else:
        return Response({"error": "Invalid operation"}, status=400)

    product.save()
    
    # Log the inventory change
    InventoryLog.objects.create(product=product, change_type=change_type, quantity_changed=quantity)

    return Response({"message": "Inventory updated successfully"})

@api_view(['GET'])
def get_inventory(request):
    """ Fetch all products in inventory """
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# ✅ Basic function-based view
def home(request):
    return HttpResponse("Welcome to Inventory Automation")  

def about(request):
    return HttpResponse("Welcome to Inventory Automation")  

# ✅ API ViewSet for managing products
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# API Views using Django REST Framework
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class InventoryLogViewSet(viewsets.ModelViewSet):
    queryset = InventoryLog.objects.all()
    serializer_class = InventoryLogSerializer
  



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class InventoryPredictionViewSet(viewsets.ModelViewSet):
    queryset = InventoryPrediction.objects.all()
    serializer_class = InventoryPredictionSerializer

    # Function to log user actions
def log_user_activity(user, action, table_name, record_id=None):
    UserActivityLog.objects.create(
        user=user,
        action=action,
        table_name=table_name,
        record_id=record_id
    )


