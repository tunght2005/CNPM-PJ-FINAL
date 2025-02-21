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
# Tao order admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display1 = ('order_id', 'customer', 'total', 'created_at', 'updated_at')
    search_fields1 = ('customer', 'total')
    list_filter1 = ('customer', 'total')
    ordering1 = ('-created_at',)  # Sắp xếp theo ngày tạo mới nhất trước
    
    readonly_fields1 = ('created_at', 'updated_at')
    
    fieldsets1 = (
        ('Thông tin đơn hàng', {
            'fields': ('customer', 'total')
        }),
        ('Thời gian', {
            'fields': ('created_at', 'updated_at')
        }),
    )
# Tao order detail admin
from .models import OrderDetail

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display2 = ('order', 'product', 'quantity', 'price', 'created_at', 'updated_at')
    search_fields2 = ('order', 'product', 'quantity', 'price')
    list_filter2 = ('order', 'product', 'quantity', 'price')
    ordering2 = ('-created_at',)
    
    readonly_fields2 = ('created_at', 'updated_at')
    
    fieldsets2 = (
        ('Thông tin chi tiết đơn hàng', {
            'fields': ('order', 'product', 'quantity', 'price')
        }),
        ('Thời gian', {
            'fields': ('created_at', 'updated_at')
        }),
    )
# Tao customer admin

from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display3 = ('customer_id', 'user', 'full_name', 'phone', 'address', 'created_at', 'updated_at')
    search_fields3 = ('user', 'full_name', 'phone', 'address')
    list_filter3 = ('user', 'full_name', 'phone', 'address')
    ordering3 = ('-created_at',)
    
    readonly_fields3 = ('created_at', 'updated_at')
    
    fieldsets3 = (
        ('Thông tin khách hàng', {
            'fields': ('user', 'full_name', 'phone', 'address')
        }),
        ('Thời gian', {
            'fields': ('created_at', 'updated_at')
        }),
    )
