from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["UserID", "email", "phone", "address", "role", "created_at", "updated_at"]
        read_only_fields = ["UserID", "created_at", "updated_at"]
