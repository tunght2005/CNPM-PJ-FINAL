# from django.db import models

# # Create your models here.
# import uuid

# class Notification(models.Model):
#     ORDER_STATUS_CHOICES = [
#         ('pending', 'Chờ xử lý'),
#         ('shipped', 'Đã giao hàng'),
#         ('delivered', 'Đã nhận hàng'),
#         ('canceled', 'Đã hủy'),
#     ]
#      order_id = models.UUIDField(default=uuid.uuid4, editable=False)
#     status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
#     order_date = models.DateTimeField(auto_now_add=True)
#     product_image = models.ImageField(upload_to='media/product_images/', blank=True, null=True)
#     active = models.BooleanField(default=True)
#     def __str__(self):
#         return f"Order {self.order_id} - {self.status}"
import random
import string
from django.db import models

class Notification(models.Model):
    ORDER_STATUS_CHOICES = [
        ('pending', 'Chờ xử lý'),
        ('shipped', 'Đã giao hàng'),
        ('delivered', 'Đã nhận hàng'),
        ('canceled', 'Đã hủy'),
    ]
    def generate_order_id():
        return "DS" + "".join(random.choices(string.digits, k=6))  # Tạo mã DSxxxxxx (8 ký tự)
    order_id = models.CharField(max_length=8, unique=True, default=generate_order_id, editable=False)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
    order_date = models.DateTimeField(auto_now_add=True)
    product_image = models.ImageField(upload_to='media/product_images/', blank=True, null=True)
    active = models.BooleanField(default=True)
    is_read = models.BooleanField(default=False)
    def __str__(self):
        return f"Order {self.order_id} - {self.status}"

