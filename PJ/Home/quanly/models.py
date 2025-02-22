from django.db import models
from pj_home.models import User
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
    category = models.CharField(max_length=255,choices=[
        ('kim_cuong', 'Kim Cương'),
        ('vang', 'Vàng'),
        ('bac', 'Bạc'),
        ('day_chuyen', 'Dây chuyền'),
        ('nhan', 'Nhẫn'),
        ('vong', 'Vòng'),
        ('bong_tai', 'Bông tai'),
        ('lac_tay', 'Lắc tay'),
        ('dong_ho', 'Đồng hồ'),
        ('trang_suc_cuoi', 'Trang sức cưới'),
    ])
    cut = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0) # Thêm số lượng tồn kho
    image = models.ImageField(upload_to='products/')
    color = models.CharField(max_length=255)
    price_sale = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    search_count = models.IntegerField(default=0)  # Thêm trường theo dõi số lượt tìm kiếm
    sold_count = models.IntegerField(default=0)  # Thêm số lượng đã bán
    def __str__(self):
        return self.Pname

# class Product(models.Model):
#     ProductID = models.CharField(primary_key=True, max_length=6, default=generate_id, editable=True)
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     carat_weight = models.FloatField()
#     origin = models.CharField(max_length=255)
#     clarity = models.CharField(max_length=255)
#     category = models.CharField(max_length=255)
#     cut = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.IntegerField()
#     image = models.ImageField(upload_to='products/')
#     sold_count = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class Employee(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     position = models.CharField(max_length=100)

# class Customer(models.Model):
#     CustomerID = models.CharField(primary_key=True, max_length=6, default=generate_id, editable=False, unique=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     size_ni = models.CharField(max_length=50)

# class Order(models.Model):
#     STATUS_CHOICES = [
#         ('pending', 'Chờ xác nhận'),
#         ('confirmed', 'Đã xác nhận'),
#         ('shipping', 'Đang giao hàng'),
#         ('completed', 'Hoàn thành'),
#         ('cancelled', 'Đã hủy')
#     ]
#     OrderID = models.CharField(primary_key=True, max_length=6, default=generate_id, editable=False)
#     customer = models.ForeignKey(
#         Customer,
#         on_delete=models.CASCADE,
#         related_name='orders',
#         to_field='CustomerID'
#     )
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class OrderDetail(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='details')
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)

# class Warranty(models.Model):
#     STATUS_CHOICES = [
#         ('active', 'Còn hiệu lực'),
#         ('expired', 'Hết hạn'),
#         ('claimed', 'Đã yêu cầu'),
#         ('processing', 'Đang xử lý'),
#         ('completed', 'Hoàn thành')
#     ]
#     warrantyID = models.CharField(primary_key=True, max_length=6, default=generate_id, editable=False)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     customer = models.ForeignKey(
#         Customer,
#         on_delete=models.CASCADE,
#         to_field='CustomerID'
#     )
#     start_date = models.DateField()
#     end_date = models.DateField()
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
#     notes = models.TextField(blank=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

# class DeliveryStaff(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     status = models.CharField(max_length=50)
#     date = models.DateField()