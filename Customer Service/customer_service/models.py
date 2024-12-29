from django.db import models

# Thông tin khách hàng
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name

# Lịch sử mua hàng
class PurchaseHistory(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='purchases')
    product_name = models.CharField(max_length=200)
    date_purchased = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product_name} - {self.customer.name}"

# Chương trình khuyến mãi
class Promotion(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title
