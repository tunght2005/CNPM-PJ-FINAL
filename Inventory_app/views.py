from rest_framework import viewsets
from rest_framework import serializers
from .models import Product, Supplier, Category, Desci
from .serializers import ProductSerializer, SupplierSerializer, CategorySerializer,DesciSerializer 
from django.shortcuts import render

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class DesciViewSet(viewsets.ModelViewSet):
    queryset = Desci.objects.all()
    serializer_class = DesciSerializer  

def inventory_management(request):
    products = Product.objects.all()
    suppliers = Supplier.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'suppliers': suppliers,
        'categories': categories,
    }
    return render(request, 'inventory_management.html', context)