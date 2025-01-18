from django.db import models # type: ignore

# Create your models here.

# User model: Đại diện cho người dùng
class user (models.Model):
    Username = models.CharField(max_length=255)
    Userid = models.IntegerField(unique=True)
    UserPhone = models.CharField(max_length=15, unique=True)
    Address = models.CharField(max_length=255)
    def _str_(self):
        return f"{self.Username} {self.Userid}"
        
# PaymentMethod model: Đại diện cho các phương thức thanh toán
class PaymentMethod (models.Model):
    User = models.ForeignKey(user, on_delete=models.CASCADE, related_name="payment_methods")
    Details = models.TextField()
# TransactionHistory model: Lưu lịch sử giao dịch
class TransactionHistory(models.Model):
    User = models.ForeignKey(user, on_delete=models.CASCADE, related_name="transactions")
    PaymentMethod = models.ForeignKey(PaymentMethod, on_delete=models.SET_NULL, null=True)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)

# NotificationService model: Xử lý thông báo
class Notification(models.Model):
    User = models.ForeignKey(user, on_delete=models.CASCADE, related_name="notifications")
    Message = models.TextField()
    CreatedAt = models.DateTimeField(auto_now_add=True)
    IsRead = models.BooleanField(default=False)