from rest_framework import serializers
from .models import Product, Supplier, Category, Desci

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class DesciSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desci
        fields = '__all__'