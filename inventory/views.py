# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse  
from rest_framework import viewsets
from .models import User, Category, Supplier, Product, Order, OrderItem, InventoryLog
from .serializers import UserSerializer, CategorySerializer, SupplierSerializer, OrderSerializer, ProductSerializer
from .serializers import OrderItemSerializer, InventoryLogSerializer

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
  



