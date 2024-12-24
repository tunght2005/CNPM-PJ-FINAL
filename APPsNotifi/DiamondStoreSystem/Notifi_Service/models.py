from django.db import models

class Notification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    customer_email = models.EmailField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# Notifi có form có sẳn
# from django.db import models

# class Notification(models.Model):
#     order_code = models.CharField(max_length=10, null=True)
#     status = models.CharField(max_length=50)
#     order_date = models.DateField(null=True)
#     # Thay thế ImageField bằng URLField
#     product_image = models.URLField(max_length=200)  # Lưu đường dẫn URL của ảnh
#     is_read = models.BooleanField(default=False)

#     def __str__(self):
#         return f"Notification {self.order_code}"

