from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, SupplierViewSet, CategoryViewSet,DesciViewSet
from .views import inventory_management

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')
router.register(r'desci', DesciViewSet, basename='desci')
router.register(r'suppliers', SupplierViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', inventory_management, name='inventory_management'),
]
