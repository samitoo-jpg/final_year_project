from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    UserViewSet, CategoryViewSet, SupplierViewSet, ProductViewSet, 
    OrderViewSet, OrderItemViewSet, InventoryLogViewSet, SaleViewSet, 
    InventoryPredictionViewSet, update_inventory, get_inventory
)

# ✅ DRF Router Configuration
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)  # <== Make sure this exists
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'inventory-logs', InventoryLogViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'inventory-predictions', InventoryPredictionViewSet)

# ✅ URL Patterns
urlpatterns = [
    path('', include(router.urls)),  # <== This ensures DRF API is correctly exposed

    # ✅ Inventory APIs
    path('update-inventory/', update_inventory, name='update-inventory'),
    path('get-inventory/', get_inventory, name='get-inventory'),

    # ✅ JWT Authentication Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
