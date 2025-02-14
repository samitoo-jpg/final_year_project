from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory import views
from .views import (
    UserViewSet, CategoryViewSet, SupplierViewSet, 
    ProductViewSet, OrderViewSet, OrderItemViewSet, InventoryLogViewSet
)

# Create API Router
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'inventory-logs', InventoryLogViewSet)

urlpatterns=[
    path('',views.home,name='my_home'),
    path('about/',views.about,name='my_about'),
    path('api/', include(router.urls)),
]


