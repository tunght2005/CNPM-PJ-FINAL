import random
import string
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Hàm sinh ID ngẫu nhiên (6 ký tự)
import uuid

def generate_id():
    return str(uuid.uuid4())[:6] 

class User(AbstractUser):
    pass
    UserID = models.CharField(primary_key=True, max_length=6, default=generate_id, editable=False, unique=True)
    ROLE_CHOICES = [
        (1, 'Guest'),
        (2, 'Customer'),
        (3, 'SaleStaff'),
        (4, 'Delivery Staff'),
        (5, 'Manager'),
        (6, 'Admin'),
    ]
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Thêm related_name để tránh xung đột với auth.User
    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

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

class Customer(models.Model):
    CustomerID = models.CharField(primary_key=True, max_length=6, default=generate_id, editable=False, unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    size_ni = models.CharField(max_length=50)

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Đang xử lý'),
        ('shipping', 'Đang giao hàng'),
        ('delivered', 'Đã giao hàng'),
        ('canceled', 'Đã hủy'),
    ]
    OrderID = models.CharField(primary_key=True, max_length=6, default=generate_id, editable=False, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Order {self.OrderID} - {self.status}"
    @property
    def get_cart_items(self):
        orderDetails = self.order_details.all()
        total = sum([item.quantity for item in orderDetails])
        return total
    @property
    def get_cart_total(self):
        orderDetails = self.order_details.all()
        total = sum([item.get_total for item in orderDetails])
        return total
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1) # Thêm số lượng sản phẩm
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def save(self, *args, **kwargs):
        # Khi đơn hàng hoàn tất, cập nhật số lượng đã bán
        if self.order.status == 'completed':
            self.product.sold_count += self.quantity
            self.product.stock -= self.quantity
            self.product.save()
        super().save(*args, **kwargs)
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
class Cart(models.Model):
    CartID = models.CharField(primary_key=True, max_length=6, default=generate_id, editable=False, unique=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)  # Liên kết với User
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def total_price(self):
        return sum(item.total_price() for item in self.cart_items.all())  # Tính tổng tiền giỏ hàng

    def __str__(self):
        return f"Giỏ hàng của {self.customer.username} - ID {self.CartID}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")  # Mỗi giỏ có nhiều sản phẩm
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity  # Tổng tiền của sản phẩm này

    def __str__(self):
        return f"{self.quantity} x {self.product.Pname}"

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

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)

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
# class Notification(models.Model):
#     ORDER_STATUS_CHOICES = [
#         ('pending', 'Chờ xử lý'),
#         ('shipped', 'Đã giao hàng'),
#         ('delivered', 'Đã nhận hàng'),
#         ('canceled', 'Đã hủy'),
#     ]
#     def generate_order_id():
#         return "DS" + "".join(random.choices(string.digits, k=6))  # Tạo mã DSxxxxxx (8 ký tự)
#     order_id = models.CharField(max_length=8, unique=True, default=generate_order_id, editable=False)
#     status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
#     order_date = models.DateTimeField(auto_now_add=True)
#     product_image = models.ImageField(upload_to='media/product_images/', blank=True, null=True)
#     active = models.BooleanField(default=True)
#     is_read = models.BooleanField(default=False)
#     def __str__(self):
#         return f"Order {self.order_id} - {self.status}"