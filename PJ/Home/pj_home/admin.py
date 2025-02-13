# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('ProductID', 'Pname', 'price', 'stock', 'category', 'image', 'created_at', 'updated_at')
    search_fields = ('Pname', 'category', 'origin', 'color')
    list_filter = ('category', 'origin', 'clarity', 'cut', 'color')
    ordering = ('-created_at',)  # Sắp xếp theo ngày tạo mới nhất trước

    readonly_fields = ('created_at', 'updated_at')  # Không cho chỉnh sửa ngày tạo/cập nhật

    fieldsets = (
        ('Thông tin sản phẩm', {
            'fields': ('Pname', 'descPr', 'category', 'origin', 'color', 'cut', 'clarity')
        }),
        ('Chi tiết kỹ thuật', {
            'fields': ('carat_weight', 'price', 'price_sale', 'stock')
        }),
        ('Hình ảnh', {
            'fields': ('image',)
        }),
        ('Thời gian', {
            'fields': ('created_at', 'updated_at')
        }),
    )
