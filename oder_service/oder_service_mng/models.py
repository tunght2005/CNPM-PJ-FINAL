from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ('NEW', 'Mới tạo'),
        ('IN_PROGRESS', 'Đang giao'),
        ('COMPLETED', 'Giao xong'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='NEW')

    def __str__(self):
        return f"Order {self.id} - {self.get_status_display()}"


class Shipping(models.Model):
    SHIPPING_STATUS_CHOICES = [
        ('PENDING', 'Chờ xử lý'),
        ('IN_TRANSIT', 'Đang giao'),
        ('DELIVERED', 'Đã giao'),
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="shipping")
    address = models.TextField()
    shipping_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=SHIPPING_STATUS_CHOICES, default='PENDING')
    courier = models.CharField(max_length=100, null=True, blank=True)  # Đơn vị vận chuyển

    def __str__(self):
        return f"Shipping for Order {self.order.id} - {self.get_status_display()}"
