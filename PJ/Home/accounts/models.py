import random
import string
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
from pj_home.models import User

# Hàm sinh ID ngẫu nhiên (6 ký tự)
import uuid

def generate_id():
    return str(uuid.uuid4())[:6] 

class Product(models.Model):
    ProductID = models.CharField(primary_key=True, max_length=6, default=generate_id, editable=False, unique=True)
    Pname = models.CharField(max_length=255)
    descPr = models.TextField()
    carat_weight = models.FloatField()
    origin = models.CharField(max_length=255)
    clarity = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    cut = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    color = models.CharField(max_length=255)
    price_sale = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    search_count = models.IntegerField(default=0)  # Thêm trường theo dõi số lượt tìm kiếm
    sold_count = models.IntegerField(default=0)  # Thêm số lượng đã bán
    def __str__(self):
        return self.Pname

class Customer(models.Model):
    CustomerID = models.CharField(primary_key=True, max_length=6, default=generate_id, editable=False, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer_account")  # Thêm related_name
    size_ni = models.CharField(max_length=50)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee_account")  # Thêm related_name
    position = models.CharField(max_length=100)


class Order(models.Model):
    OrderID = models.CharField(primary_key=True, max_length=6, default=generate_id, editable=False, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class Cart(models.Model):
    CartID = models.CharField(primary_key=True, max_length=6, default=generate_id, editable=False, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.IntegerField()

class Feedback(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class DeliveryStaff(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    date = models.DateField()


class Report(models.Model):
    reportID = models.CharField(primary_key=True, max_length=6, default=generate_id, editable=False, unique=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Warranty(models.Model):
    warrantyID = models.CharField(primary_key=True, max_length=6, default=generate_id, editable=False, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    terms = models.TextField()
    status = models.CharField(max_length=50)
    claim = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Point(models.Model):
    pointID = models.CharField(primary_key=True, max_length=6, default=generate_id, editable=False, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    exchange_point = models.IntegerField()
    point_used = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Sale(models.Model):
    saleID = models.CharField(primary_key=True, max_length=6, default=generate_id, editable=False, unique=True)
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.FloatField()

class Desc(models.Model):
    descID = models.CharField(primary_key=True, max_length=6, default=generate_id, editable=False, unique=True)
    category_desc = models.CharField(max_length=255)
    name_desc = models.CharField(max_length=255)
    image = models.ImageField(upload_to='descriptions/')
    content = models.TextField()

class Wishlist(models.Model):
    wishlistID = models.CharField(primary_key=True, max_length=6, default=generate_id, editable=False, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Notification(models.Model):
    notificationID = models.CharField(primary_key=True, max_length=6, default=generate_id, editable=False, unique=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='notifications/', null=True, blank=True)
    is_read = models.BooleanField(default=False)
