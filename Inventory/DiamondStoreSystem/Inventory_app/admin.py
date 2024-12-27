from django.contrib import admin
from .models import Diamond, Supplier, Transaction

# Đăng ký model để hiển thị trong admin site
@admin.register(Diamond)
class DiamondAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'carat', 'cut', 'color', 'clarity', 'price', 'quantity')
    search_fields = ('name', 'cut', 'color')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'contact', 'address')
    search_fields = ('name',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'date', 'total_amount')
    date_hierarchy = 'date'
