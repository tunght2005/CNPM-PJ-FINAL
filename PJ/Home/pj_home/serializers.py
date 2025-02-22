from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Order, OrderDetail, Product
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["UserID", "email", "phone", "address", "role", "created_at", "updated_at"]
        read_only_fields = ["UserID", "created_at", "updated_at"]

from .models import Order, OrderDetail

class OrderDetailSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source="product.Pname", read_only=True)
    product_image = serializers.ImageField(source="product.image", read_only=True)

    class Meta:
        model = OrderDetail
        fields = ["product", "product_name", "product_image", "quantity", "price"]

class OrderSerializer(serializers.ModelSerializer):
    order_details = OrderDetailSerializer(many=True, source="orderdetail_set", read_only=True)

    class Meta:
        model = Order
        fields = ["OrderID", "customer", "status", "total_amount", "created_at", "order_details"]



