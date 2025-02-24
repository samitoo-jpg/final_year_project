from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory import views
from .views import (
    UserViewSet, CategoryViewSet, SupplierViewSet,
    ProductViewSet, SaleViewSet, OrderViewSet, OrderItemViewSet, InventoryLogViewSet, InventoryPredictionViewSet
)

from django.urls import path
from .views import get_inventory, update_inventory

# Create API Router
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'inventory-logs', InventoryLogViewSet)
router.register(r'predictions', InventoryPredictionViewSet) 

urlpatterns=[
    path('',views.home,name='my_home'),
    path('about/',views.about,name='my_about'),
    path('api/', include(router.urls)),
]

urlpatterns = [
    path('api/products/', ProductViewSet.as_view({'get': 'list', 'post': 'create'}), name='product-list'),
    path('api/products/<int:pk>/', ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='product-detail'),
    path('api/sales/', SaleViewSet.as_view({'get': 'list', 'post': 'create'}), name='sale-list'),
    path('api/predictions/', InventoryPredictionViewSet.as_view({'get': 'list', 'post': 'create'}), name='prediction-list'), 
]


urlpatterns = [
    path('inventory/', get_inventory, name='get_inventory'),
    path('inventory/update/', update_inventory, name='update_inventory'),
]