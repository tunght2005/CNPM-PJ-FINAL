from django.db import models

# class Notification(models.Model):
#     title = models.CharField(max_length=255)
#     message = models.TextField()
#     customer_email = models.EmailField()
#     sent_at = models.DateTimeField(auto_now_add=True)
#     is_read = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title

# Notifi có form có sẳn
from django.db import models

class Notification(models.Model):
    STATUS_CHOICES = [
        ('Delivered', 'Đã Giao'),
        ('Processing', 'Đang Xử Lí'),
        ('Cancelled', 'Đã Huỷ'),
        ('Shipping', 'Đang Vận Chuyển'),
        ('Info', 'Thông tin'),
    ]
    title = models.CharField(max_length=255, verbose_name="Mã Đơn Hàng")
    message = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name="Trạng Thái")
    customer_email = models.EmailField(verbose_name="Email khách hàng")
    product_image_url = models.URLField(verbose_name="Link ảnh sản phẩm", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Thông báo"
        verbose_name_plural = "Các thông báo"

