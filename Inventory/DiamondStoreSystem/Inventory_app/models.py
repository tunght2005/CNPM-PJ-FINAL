from django.db import models

# Model đại diện cho kim cương
class Diamond(models.Model):
    name = models.CharField(max_length=100)
    carat = models.DecimalField(max_digits=5, decimal_places=2)
    cut = models.CharField(max_length=50)
    color = models.CharField(max_length=10)
    clarity = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.carat} carat)"

# Model đại diện cho nhà cung cấp
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.name

# Model đại diện cho giao dịch bán hàng
class Transaction(models.Model):
    customer_name = models.CharField(max_length=100)
    items = models.JSONField()  # Lưu các sản phẩm đã bán
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction {self.id} - {self.customer_name}"

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)

    def __str__(self):
        return self.name