from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, CategoryViewSet, SupplierViewSet, ProductViewSet, 
    OrderViewSet, OrderItemViewSet, InventoryLogViewSet, SaleViewSet, 
    InventoryPredictionViewSet, update_inventory, get_inventory, home, about
)

# ✅ Using DefaultRouter for automatic API routing
router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'inventory-logs', InventoryLogViewSet)
router.register(r'sales', SaleViewSet)
router.register(r'inventory-predictions', InventoryPredictionViewSet)

# ✅ Define URL Patterns
urlpatterns = [
    # Home and About Pages
    path('', home, name='home'),
    path('about/', about, name='about'),

    # Inventory Management APIs
    path('update-inventory/', update_inventory, name='update-inventory'),
    path('get-inventory/', get_inventory, name='get-inventory'),

    # ✅ Include all ViewSets
    path('api/', include(router.urls)),

    # ✅ API Authentication (JWT)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login (Returns access + refresh tokens)
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Refresh Token (Returns new access token)
]


